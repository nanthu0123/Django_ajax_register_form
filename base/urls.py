from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.create_user, name='register'),
    path('view/',views.view_user,name='view_user')
]
