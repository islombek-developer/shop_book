from django.urls import path
from .views import ClientProduct,DetailView,Categoryes,CartDetailView,delete,LoginView,ClientCategory,ProfileView,EditProfileView,LogautView,RegisterView,ResetPasswordView,sallr,ProfileViewAdmin,Delete,Deletes,RegisterView2

app_name = 'client'

urlpatterns = [

   
    path('login/',LoginView.as_view(),name='login'),
    path('',ClientProduct.as_view(),name='products'),
    path('batafsil/<int:id>/',DetailView.as_view(),name='batafsil'),
    path('cart/',DetailView.as_view(),name='cart'),
    path('carts/',CartDetailView.as_view(),name='carts'),
    path('categories/<int:id>/',Categoryes.as_view(),name='categories'),
    path('delete/<int:id>/',delete,name='delete'),
    path('deletec/<int:id>/',Delete.as_view(),name='deletec'),
    path('deletes/<int:id>/',Deletes.as_view(),name='deletes'),
    path('category/<int:id>/',ClientCategory.as_view(),name='categor'),
    path('edit/<int:id>/',EditProfileView.as_view(),name='edit'),
    path('profil/',ProfileView.as_view(),name='profil'),
    path('dashboard/',ProfileViewAdmin.as_view(),name='dashboard'),
    path('logout/', LogautView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('register2/', RegisterView2.as_view(), name='register2'),
    path('sallar/',sallr, name='sallar'),
    path('resed-password', ResetPasswordView.as_view(), name='resed_password'),


]
