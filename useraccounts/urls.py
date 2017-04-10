from django.conf.urls import url,include
from django.contrib.auth.views import password_reset
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
	url(r'^reg/', views.regisration, name='registration'),
	url(r'^login/', views.login, name='login'),
	url(r'^logout/', views.logout, name='logout'),
	url(r'^update/', views.updateProfile, name='update'),
	url(r'^todos/', views.todos_view.as_view(), name='view_todos'),
	url(r'^newtodo/', views.AddTaskView.as_view(), name='new_todo'),
	url(r'^updatetodo/(?P<pk>[0-9]+)/$', views.UpdateTodo, name='todo-update'),
	url(r'^del_todo/(?P<pk>[0-9]+)/$', views.DeleteTodo, name='todo-delete'),
	url(r'^todo_status/(?P<pk>[0-9]+)/$', views.ChangeTodoStatus, name='todo-status'),
	url(r'^hide_completed_todos/$', views.HideTodos, name='todo-hide'),
	url(r'^reset_password/', views.password_reset, name='reset_password'),
]

