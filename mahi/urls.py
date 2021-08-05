
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_view

urlpatterns = [
    path('',views.home, name='home-page'),
    path('filter-page/<str:type_of_pic>/', views.filterPage, name='filter-page'),
    path('login/', auth_views.LoginView.as_view(template_name='mahi/login.html') , name='login-page'),
    path('logout/',auth_views.LogoutView.as_view(template_name='mahi/logout.html'),name='logout-page'),
    path('about-me', views.aboutMe, name='about-me'),
    path('contact-me', views.contactPage, name='contact-me'),

]
