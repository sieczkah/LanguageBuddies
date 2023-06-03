from django.urls import path

from . import views

urlpatterns = [
    path("accounts/login/", views.login_view, name="login"),
    path("accounts/register/", views.register_view, name="register"),
    path("accounts/logout/", views.logout_view, name="logout"),
    path("accounts/profile/<str:id>", views.profile_view, name="profile"),
    path("accounts/edit-profile/", views.edit_profile_view, name="edit-profile"),
]
