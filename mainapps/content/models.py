from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=30, verbose_name='名称')

    def __str__(self):
        return self.title

    class Meta:
        db_table = 't_category'
        verbose_name = '分类'
        verbose_name_plural = verbose_name


class Tag(models.Model):
    title = models.CharField(max_length=20, verbose_name='名称')

    def __str__(self):
        return self.title

    class Meta:
        db_table = 't_tag'
        verbose_name = '标签'
        verbose_name_plural = verbose_name


class Teacher(models.Model):
    name = models.CharField(max_length=50, verbose_name='教师名')
    image = models.CharField(max_length=300, verbose_name='教师头像url')
    intro = models.CharField(max_length=200, verbose_name='教师简介')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 't_teacher'
        verbose_name = '教师表'
        verbose_name_plural = verbose_name


class Course(models.Model):
    title = models.CharField(max_length=200, verbose_name='课程名')

    summary = models.CharField(max_length=200, verbose_name='课程简介')

    cover = models.CharField(verbose_name='封面url', max_length=200)

    favor = models.IntegerField(verbose_name='点赞人数', default='0')

    price = models.DecimalField(decimal_places=2, max_digits=5, verbose_name='课程价格')

    detail = models.CharField(max_length=300, verbose_name='课程详情url')

    teachers = models.ForeignKey(Teacher, on_delete=models.CASCADE, verbose_name='主讲老师')

    tags = models.ForeignKey(Tag, on_delete=models.CASCADE, verbose_name='标签')

    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='分类')

    def __str__(self):
        return self.title

    class Meta:
        db_table = 't_course'
        verbose_name = '课程'
        verbose_name_plural = verbose_name
