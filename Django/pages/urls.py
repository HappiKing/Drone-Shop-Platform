from django.urls import path
from . import views

urlpatterns = [
    path('', views.mainpage),
    path('company/', views.company),
    path('product/', views.product),
    path('product/option/', views.product_option),
    path('product/option/detail/', views.product_detail),
    path('product/option/detail/sucsess/', views.product_sucsess),
    path('support/', views.support),

]