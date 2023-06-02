from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="homepage"),
    path("room/<str:id>/", views.room, name="room"),
    #
    path("accounts/login/", views.login_view, name="login"),
    path("accounts/register/", views.register_view, name="register"),
    path("accounts/logout/", views.logout_view, name="logout"),
    path("accounts/profile/<str:id>", views.profile_view, name="profile"),
    path("accounts/edit-profile/", views.edit_profile_view, name="edit-profile"),
    #
    path("create-room/", views.create_room, name="create-room"),
    path("update-room/<str:id>/", views.update_room, name="update-room"),
    path("delete-room/<str:id>/", views.delete_room, name="delete-room"),
    #
    path("delete-message/<str:id>/", views.delete_message, name="delete-message"),
]
