from django.contrib import admin
from django.urls import include,path
from . import views

app_name ="aptcoder"

urlpatterns = [
    path("",views.index,name="index"),
    path("login/",views.login_view,name="login"),
    path("logout/",views.logout_view,name="logout"),
    path("register_tech/",views.register_teach,name="register_teach"), 
    path("register_student/",views.register_student,name="register_student"), 
    path("<int:userid>/reg_course",views.reg_course,name="reg_course"),
    path("<int:userid>/reg_courseSt",views.reg_courseSt,name="reg_courseSt"),

]