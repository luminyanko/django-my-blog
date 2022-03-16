from django.urls import path
from . import views

urlpatterns = [
    path('', views.showblog, name='blog'),
    path('<int:post_id>/', views.post_view, name='post'),

]