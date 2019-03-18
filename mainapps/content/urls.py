from django.conf.urls import url
from content import views

urlpatterns = [
    url(r'^showall/', views.showall),
    url(r'^detail/(\d+)/', views.detail),
    url(r'^showone/(\d+)', views.showone),
    url(r'^search/', views.search),
]
