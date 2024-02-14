from django.urls import re_path
from . import views

urlpatterns = [
    re_path(r'^$', views.index, name='index'),
    re_path(r'^product/(?P<product_id>\d+)/(?P<product_slug>[-\w]+)/$', views.show_product, name='product_detail'),
    re_path(r'^cart/$', views.show_cart, name='show_cart'),
    re_path(r'^checkout/$', views.checkout, name='checkout'),
]
