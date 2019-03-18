from django.conf.urls import url

from user import views

urlpatterns = [
    url(r'^regist/', views.regist),
    url(r'^login/', views.login),
    url(r'^logout/', views.logout),
    url(r'^add/(\d+)/',views.add_course),
    url(r'^delete/(\d+)/', views.delete_course),
    url(r'^gocollect/',views.go_collect)
]
