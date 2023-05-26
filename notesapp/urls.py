"""notesproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path('',views.index,name="index"),
    path('login/',views.login,name="login"),
    path('logout/',views.logout,name="logout"),
    path('registration/',views.registration,name="registration"),
    path('forgot_password/',views.forgot_password,name="forgot_password"),
    path('save/',views.save,name="save"),
    path('home/',views.home,name="home"),
    path('view_content/',views.view_content,name="view_content"),
    path('login_verification/',views.login_verification,name="login_verification"),
    path('aboutus/',views.aboutus,name="aboutus"),
    path('editcontent/<id>',views.edit_content,name="edit_content"),
    path('contactus/',views.contactus,name="contactus"),
    path('add_notes/',views.add_notes,name="addnotes"),
    path('savecontent/',views.savecontent,name="savecontent"),
    path('view/<id>',views.view,name="view"),
    path('delete/<id>',views.delete,name="delete"),
    path('update/<id>',views.update,name="update"),
    path('feedback/',views.feedback,name="feedback"),
    path('give_feedback/',views.give_feedback,name="give_feedback"),
    path('change_password/',views.change_password,name="change_password"),
    path('admin_login/',views.admin_login,name="admin_login"),
    path('admin_login_verification/',views.admin_login_verification,name="admin_login_verification"),
    path('admin_home/',views.admin_home,name="admin_home"),
    path('save_admin/',views.save_admin,name="save_admin"),
    path('admin_users/',views.admin_users,name="admin_users"),
    path('deleteuser/<id>',views.deleteuser,name="deleteuser"),
    path('admin_feedback/',views.admin_feedback,name="admin_feedback"),
    path('deletefeedback/<id>',views.deletefeedback,name="deletefeedback"),
]
