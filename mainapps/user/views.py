import json
from django.contrib.auth.hashers import check_password
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect

# Create your views here.
from django.views.decorators.csrf import csrf_exempt

from content.models import Course
from user.forms import UserForm
from user.models import User, Relation


# 注册
@csrf_exempt
def regist(request):
    if request.method == 'POST':
        # 创建UserForm表单对象
        form = UserForm(request.POST)
        name = request.POST.get('username')
        try:
            User.objects.get(username=name)
            msg = '用户名已存在'
            return render(request,'user/regist.html',locals())
        except:
            if form.is_valid():
                form.save()  # 写入数据库
                return redirect('/user/login/')

        errors = json.loads(form.errors.as_json())
    return render(request, 'user/regist.html', locals())


# 登录
@csrf_exempt
def login(request):
    if request.method == 'POST':
        errors = {'msg': ''}
        username = request.POST.get('username')
        password = request.POST.get('password')

        queryset = User.objects.filter(username=username)
        if not queryset.exists():
            errors['msg'] = '%s 用户不存在，请先注册!' % username
        else:
            user = queryset.first()
            # 验证口令
            if check_password(password, user.password):
                # 将登录后的信息存入到session中
                request.session['login_user'] = {
                    'id': user.id,
                    'nickname': user.nickname,
                }
                return redirect('/course/showall/')
            else:
                errors['msg'] = '登录口令不正确！'

    return render(request, 'user/login.html', locals())


# 退出
def logout(request):
    # 从哪个页面请求过来的
    print('Referer:', request.META.get('Referer'))
    del request.session['login_user']
    return redirect('/course/showall/')


def go_collect(request):
    # 获取登录的用户的id
    user_id = request.session.get('login_user').get('id')
    # 返回用户课程
    courses = User.objects.filter(id=user_id)[0].mycollection.lesson.all()
    return render(request, 'user/collect.html', locals())


def add_course(request, course_id):
    try:
        # 获取登录的用户的id
        user_id = request.session.get('login_user').get('id')
        # 返回用户课程
        courses = User.objects.filter(id=user_id)[0].mycollection.lesson.all()

        # 将收藏的课程添加到数据库中
        aa = Relation.objects.filter(collect=user_id).all()
        if aa.filter(courseName=int(course_id)):
            msg = '已有收藏'
            return HttpResponseRedirect('/course/detail/%s/' % course_id, {'msg': msg})
        else:
            Relation.objects.create(collect_id=int(user_id), courseName_id=int(course_id))
            return render(request, 'user/collect.html', locals())
    except:
        return redirect('/user/login/')


def delete_course(request, course_id):
    q_obj = Relation.objects.filter(courseName=int(course_id))
    q_obj.delete()
    user_id = request.session.get('login_user').get('id')
    courses = User.objects.filter(id=user_id)[0].mycollection.lesson.all()
    return render(request, 'user/collect.html', locals())
