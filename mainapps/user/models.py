from django.contrib.auth.hashers import make_password
from django.db import models

# Create your models here.
from content.models import Course


class User(models.Model):
    username = models.CharField(max_length=50,
                                verbose_name='账户')
    password = models.CharField(max_length=100,
                                verbose_name='口令')

    nickname = models.CharField(max_length=50,
                                verbose_name='昵称')

    phone = models.CharField(max_length=11,
                             verbose_name='手机号')

    add_time = models.DateTimeField(verbose_name='注册时间',
                                    auto_now_add=True)

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        self.password = make_password(self.password)
        super().save()

    def __str__(self):
        return self.username

    class Meta:
        db_table = 't_user'
        verbose_name = '用户'
        verbose_name_plural = verbose_name


class MyCollection(models.Model):
    person = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='用户')
    lesson = models.ManyToManyField(Course, through='Relation', verbose_name='课程')


class Relation(models.Model):
    collect = models.ForeignKey(MyCollection, on_delete=models.CASCADE)
    courseName = models.ForeignKey(Course, on_delete=models.CASCADE)
