from django.contrib import admin
from student.models import Student
from django.conf import settings
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password

class StudentAdmin(admin.ModelAdmin):
    list_display = ('student_num','name', 'gender', 'phone', 'dba')
    list_filter = ('name', 'student_num')
    search_fields = (['name', 'student_num'])
    #readonly_field = ('teacher',)
    ordering = ('-created_at',)
    fieldsets = (
        (None, {
            'fields':('student_num','name','gender', 'phone', 'dba')
        }),
    )

    def save_model(self, request, obj, form, change):
        user = User.objects.create(
            username = request.POST.get('student_num'),
            password = make_password(settings.STUDENT_INIT_PASSWORD)
        )
        obj.user_id = user.id
        obj.dba_id = request.user.id
        super().save_model(request, obj, form, change)
        return

    def delete_queryset(self, request, queryset):
        for obj in queryset:
            obj.user.delete()
        super().delete_model(request, obj)
        return

    def delete_model(self, request, obj):
        super().delete_model(request, obj)
        if obj.user:
            obj.user.delete()
        return

admin.site.site_header = '管理系统后台'
admin.site.site_title = '管理系统后台'
admin.site.register(Student, StudentAdmin)