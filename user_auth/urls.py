from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns=[
    path('',views.landing_page,name="home"),
    path('signup/', views.register, name='signup'),
    path('nav/', views.nav, name='nav'),
    path('about/', views.about, name='about'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    
]