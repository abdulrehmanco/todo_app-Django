from django.contrib import admin
from home import views
from django.urls import path

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('updatetask/<str:pk>',views.updatetask,name='updatetask'),
    path('deletetask/<str:pk>',views.deletetask,name='deletetask')
      
]
