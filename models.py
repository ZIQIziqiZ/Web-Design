from django.db import models
from utils.base_models import CreateUpdateMixin

class PassRate(CreateUpdateMixin):
    title = models.CharField(max_length=20,help_text='title/考试名称',verbose_name='考试名称')
    date = models.DateField(help_text="date/考试日期",verbose_name='考试日期')
    subject = models.CharField(max_length=20,help_text='subject/考试科目',verbose_name='考试科目')
    rate = models.DecimalField(max_digits=5,decimal_places=2,help_text='rate/通过率',verbose_name='通过率')

    class Meta:
        db_table = "PassRate"
        verbose_name_plural = "考试通过率"
        verbose_name = "考试通过率"

class Distribution(CreateUpdateMixin):
    title = models.CharField(max_length=20,help_text='title/考试名称',verbose_name='考试名称')
    date = models.DateField(help_text="date/考试日期",verbose_name='考试日期')
    score = models.CharField(max_length=20,help_text='score/分数',verbose_name='分数')
    percentage = models.DecimalField(max_digits=5,decimal_places=2,help_text='percentage/占比',verbose_name='占比')

    class Meta:
        db_table = "Distribution"
        verbose_name_plural = "成绩分布"
        verbose_name = "成绩分布"

