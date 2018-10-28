from django.conf.urls import url
from django.shortcuts import render
from content import views


def to_Index(request):
    # cates = Teacher.objects.filter(parent__isnull=True)
    return render(request, 'index.html', locals())


urlpatterns = [
    url(r'^showall/', views.showall),
    url(r'^detail/(\d+)/', views.detail),
]
