from django.shortcuts import render
from content.models import Category, Course, Teacher


# Create your views here.
def showall(request):
    categorys = Category.objects.all()
    courses = Course.objects.all()
    print('----------')
    print(categorys)
    return render(request, 'category/show.html', locals())


def detail(request,id):
    course = Course.objects.filter(id=id)
    teacher = Teacher.objects.filter(id=id)
    print('*'*50)


    return render(request,'course/detail.html',locals())