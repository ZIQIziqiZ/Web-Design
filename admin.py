from django.contrib import admin
from dba.models import DBA
from django.conf import settings
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password

class dbaAdmin(admin.ModelAdmin):
    list_display = ('tid', 'name', 'email', 'duty', 'gender', 'phone')
    list_filter = ('duty', 'name')
    search_fields = (['duty', 'name'])
    list_per_page = 30
    ordering = ('-created_at',)
    fieldsets = (
        (None, {
            'fields':('tid', 'name','email','duty', 'gender','phone')
        }),
    )

    def save_model(self, request, obj, form, change):
        user = User.objects.create(
            email = request.POST.get('email'),
            username = request.POST.get('email'),
            password = make_password(settings.DBA_INIT_PASSWORD),
            is_staff = 1
        )
        obj.tid = obj.user_id = user.id
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
admin.site.register(DBA, dbaAdmin)