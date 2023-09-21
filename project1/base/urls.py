from django.urls import path
from . import views

urlpatterns = [
    path('login/',views.loginPage, name="login"),
    path('logout/',views.logoutUser, name="logout"),
    path('register/',views.registerUser, name="register"),
    path('',views.home, name="home"),
    path('room/<str:primarykey>/',views.room, name="room"),
    path('create_room/',views.create_room,name = "create-room"),
    path('update_room/<str:pk>/',views.update_room,name = "update-room"),
    path('delete_room/<str:pk>/',views.delete_room,name = "delete-room"),
    path('delete_message/<str:pk>/<str:room_pk>/',views.delete_message,name = "delete-message"),
    path('user/<str:pk>/',views.user,name = "user"),

]