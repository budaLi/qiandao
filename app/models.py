from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone

# Create your models here.


class Student(models.Model):
    """
    学生
    """
    Student_id = models.IntegerField(_('id'),unique=True,null=False)
    Student_name=models.CharField(_('姓名'),max_length=200,unique=True,null=False)
    Student_password=models.CharField(_('密码'),max_length=200)
    Student_sex=models.CharField(_('性别'),max_length=200)
    Student_number = models.CharField(_('学号'),max_length=20)
    Student_class=models.CharField(_('班级'),max_length=20)


    def __str__(self):
        return self.Student_name

    class Meta:

        verbose_name = _('学生')
        verbose_name_plural = _('学生')

class QianDao(models.Model):
    """
    签到
    """
    q_id =  models.IntegerField(primary_key=True)
    Student_name=models.ForeignKey('Student',on_delete=models.CASCADE)
    qiandao=models.CharField(_('签到情况'),choices=(('0',_('签到成功')), ('1',_('签到失败')), ('3',_('签到异常'))),default=_('签到成功'),max_length=20)
    qiandao_time=models.DateTimeField(_('签到时间'),default=timezone.now,null=True,blank=True)

    def __str__(self):
        return self.Student_name.Student_name

    class Meta:

        verbose_name = _('签到')
        verbose_name_plural = _('签到')

class Teacher(models.Model):
    """
    老师
    """
    Teacher_id = models.IntegerField(_('id'), unique=True)
    Teacher_name = models.CharField(_('姓名'), max_length=200, unique=True)


    def __str__(self):
        return self.Teacher_name

    class Meta:
        verbose_name = _('老师')
        verbose_name_plural = _('老师')


