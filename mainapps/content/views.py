from django.core.paginator import Paginator
from django.shortcuts import render
from content.models import Category, Course, Teacher


# Create your views here.
def showall(request):
    categorys = Category.objects.all()
    cate_id = int(request.GET.get('cid', 0))
    if cate_id:
        courses = Course.objects.filter(category__parent_id=cate_id).all()
    else:
        courses = Course.objects.filter().all()
    paginator = Paginator(courses, per_page=20)
    pager = paginator.page(request.GET.get('page', 1))
    show = 'showall'
    return render(request, 'category/show.html', locals())


def showone(request, category_id):
    categorys = Category.objects.all()
    cate_id = int(request.GET.get('cid', 0))
    if cate_id:
        courses = Course.objects.filter(category=category_id, category__parent_id=cate_id)
    else:
        courses = Course.objects.filter(category=category_id)
    paginator = Paginator(courses, per_page=20)
    pager = paginator.page(request.GET.get('page', 1))
    show = 'showone/%s' % category_id
    return render(request, 'category/show.html', locals())


def detail(request, id):
    course_all = Course.objects.all()
    course = Course.objects.filter(id=id)
    teacher = Teacher.objects.filter(id=id)
    list = []
    favor_list = sorted([i.favor for i in course_all])[:-11:-1]
    for favor_count in favor_list:
        course_list = Course.objects.filter(favor=favor_count)
        course_obj = (course_list[0].favor, course_list[0].title, course_list[0].id)
        list.append(course_obj)
    return render(request, 'course/detail.html', locals())


def search(request):
    q = request.GET.get('q')
    try:
        course_list = Teacher.objects.filter(name=q)[0].course_set.all()
    except Exception as e:
        # print(e)
        # __icontains 是django的查询表达式，实际上是模糊查询SELECT `column` FROM `table` WHERE `field` like '%keyword%';
        course_list = Course.objects.filter(title__icontains=q)
    if not course_list:
        msg = '查无数据'

    return render(request, 'category/result.html', locals())
