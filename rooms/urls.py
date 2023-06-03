from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("room/<str:id>/", views.room, name="room"),
    path("create-room/", views.create_room, name="create-room"),
    path("update-room/<str:id>/", views.update_room, name="update-room"),
    path("delete-room/<str:id>/", views.delete_room, name="delete-room"),
    path("delete-message/<str:id>/", views.delete_message, name="delete-message"),
]
