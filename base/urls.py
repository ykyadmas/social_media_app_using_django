from django.contrib import admin
from django.urls import path,include


from . import views 

urlpatterns= [
     path('', views.home,name="home"),
     path('room/<str:pk>/', views.room, name="room"),
     path('create_room/',views.create_room, name="create_room"),
      path('create_room/<str:pk>',views.update_room, name="update_room"),
      path('delete_room/<str:pk>',views.delete_room, name="delete_room")
    
]

