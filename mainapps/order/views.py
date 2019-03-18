from django.http import JsonResponse
from django.shortcuts import render, redirect

# Create your views here.
from content.models import Course
from user.models import User


def add_order(request,num):
    # 验证当前用户是否登录
    login_user = request.session.get('login_user')
    if not login_user:
        return redirect('/user/login/')
    else:
        course = Course.objects.filter(id=num)
        user_id = request.session.get('login_user').get('id')
        userQset = User.objects.filter(id=user_id)

    return render(request,'order/order.html',locals(), {'title':'我的订单'})

def re_order(request):
        return render(request, 'order/order.html', locals(),
                  {'title': '我的订单'})

def re_add(request,):
    return render(request, 'order/order.html',
                  {'title': '我的订单'})


def orderinfo(request,):
    return render(request,'order/orderinfo.html',locals())

