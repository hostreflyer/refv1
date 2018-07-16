from django.urls import path

from . import views

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('faq/', views.FAQPageView.as_view(), name='faq'),
    path('check/', views.CheckPageView.as_view(), name='check'),
    path('test/', views.test, name='test'),
    path('test2/', views.test2, name='test2'),
]