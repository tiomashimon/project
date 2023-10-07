from . import views
from django.urls import path

urlpatterns = [
    path('', views.posts, name='posts'),
    path('<int:id>/', views.detail, name='detail'),
]
