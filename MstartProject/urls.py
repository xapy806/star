from django.conf.urls import url, include
from django.shortcuts import render, redirect

import xadmin as admin


def index(request):
    return redirect('/course/showall/')

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^course/', include('content.urls')),
    url(r'^user/', include('user.urls')),
    url(r'^order/',include('order.urls')),
    url(r'', index)

]
