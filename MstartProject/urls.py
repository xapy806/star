from django.conf.urls import url, include
from django.shortcuts import render

import xadmin as admin



def to_Index(request):
    # cates = Teacher.objects.filter(parent__isnull=True)
    return render(request, 'index.html',locals())

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^course/', include('content.urls')),
    # url(r'^teacher/', include('teacher.urls')),
    # url(r'^user/', include('user.urls')),
    url(r'^', to_Index),
]
