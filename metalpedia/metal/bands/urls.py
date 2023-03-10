from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:id>/',views.specificBand,name='specificBand'),
    path('bands/',views.bands,name='bands'),
    path('about/',views.about,name='about'),
    path('add/',views.add,name='add'),
    path('add/addband/',views.addband,name='addband'),
    path('news/<int:id>/',views.specificNews,name='specificNews'),
    path('login/',views.login,name='loginUser'),
    path('register/',views.register,name='register'),
    path('profile/',views.profile,name='profile'),
    path('logout_user',views.logout_user,name='logoutUser'),
    path('delete_account',views.delete_account,name='delete_account'),
]