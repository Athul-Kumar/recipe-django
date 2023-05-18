from django.urls import path
from accounts import views


urlpatterns = [

    path('register/', views.Register_users, name="register"),
    path('login/', views.login_users, name="login"),
    path('logout/', views.logout_users, name="logout"),

]