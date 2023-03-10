from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('', views.profile,name='profile'),
    path('logout/', views.logout,name='logout'),
    path('projects', views.projects,name='projects'),
    path('request_leaves', views.request_leaves,name='request_leaves'),
    path('addResponse/',views.addResponse,name="addResponse"),
    path('query', views.query,name='query')
] 