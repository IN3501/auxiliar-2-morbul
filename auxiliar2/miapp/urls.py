from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [ 
	path('',views.index, name='index'),
	path('pestaña/',views.pestaña, name='pestaña'),
	path('edocente/',views.edocente, name='edocente'),
	path('extra/', views.extra, name='extra')
	]