from django.urls import path

from . import views

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('faq/', views.FAQPageView.as_view(), name='faq'),
    path('check/', views.checkpageview, name='check'),
    path('success/', views.SuccessPageView.as_view(), name='success'),
    path('test/', views.test, name='test'),
]