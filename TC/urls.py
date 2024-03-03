from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
path('signup/', views.signup, name = "sign up"),
path('createaccount/', views.prueba, name = "ingreso"),
path('', views.homeTC, name = "TC home"),
path('logout/', views.signout, name = 'log out'),
path('login/', views.signin, name = "login"),
path('youarenotlogged/', views.ingresa, name = "no")
]