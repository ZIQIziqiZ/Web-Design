from django.db import models
from utils.base_models import CreateUpdateMixin
from django.core import validators
from dba.models import DBA

TYPE_CHOICES = (
    (1, '学生信息'),
    (2, '成绩信息'),
)

class FileUpload(CreateUpdateMixin):
    file_name = models.FileField(validators=[validators.FileExtensionValidator(['xls', 'xlsx'], message='必须为xls或xlsx文件')],
                                help_text='file_type/上传文件名',verbose_name='上传文件名')
    file_type = models.IntegerField(choices=TYPE_CHOICES, default=1, help_text='file_type/文件类型',verbose_name='文件类型')
    dba = models.ForeignKey(DBA, on_delete=models.CASCADE)  # 设置外键

    class Meta:
        db_table = "file"
        verbose_name_plural = "上传文件"
        verbose_name = "上传文件"