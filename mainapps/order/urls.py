from django.conf.urls import url

from order import views

urlpatterns = [
    url(r'add_order/(\d+)/', views.add_order),
    url(r're_order/', views.re_order),
    url(r're_add/', views.re_add),
    url(r'detail_order/', views.orderinfo),
]