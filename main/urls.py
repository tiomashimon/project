from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('services', views.services, name='services'),
    path('lawyers/', views.lawyers, name='lawyers'),
    path('tv', views.tv, name='tv'),
    path('certificates/', views.certificates, name='certificates'),
    path('help/', views.contact, name='contacts'),
    path('memo/', views.memo, name='memo'),
    path('lawyers/<int:id>/', views.lawyer_detail, name='lawyer'),
]
