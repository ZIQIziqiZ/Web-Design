from django.db import models
from utils.base_models import CreateUpdateMixin
from dba.models import DBA
from django.contrib.auth.models import User


class Student(CreateUpdateMixin):
    student_num = models.CharField(max_length=10,unique=True,verbose_name='账号')
    name = models.CharField(max_length=20,help_text='name/姓名',verbose_name='姓名')
    gender = models.CharField(max_length=32, choices=(('male','男'),('female','女')), default='女',help_text='gender/性别',verbose_name='性别')
    phone = models.CharField(max_length=11,help_text='phone/联系电话',verbose_name='联系电话')
    # user表一对一关联
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # dba表一对多关联
    dba = models.ForeignKey(DBA, on_delete=models.CASCADE)  # 设置外键

    def __str__(self):
        return self.name

    def dba_id(self):
        """
        获取dba名称
        """
        self.verbose_name = 'DBA_ID'
        return self.dba.tid
    dba_id.short_description = 'DBA_ID'

    class Meta:
        db_table = "student"
        verbose_name_plural = "学生信息"
        verbose_name = "学生信息"




