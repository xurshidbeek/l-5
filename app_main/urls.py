from django.urls import path

from . import views


urlpatterns = [
    path('', views.home_page, name='home'),
    path('detail/<int:product_id>/', views.product_detail, name='detail')
]
