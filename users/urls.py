from django.urls import path
from django.contrib.auth import views as auth_views
from . import views


urlpatterns = [
    path("", views.HomeView.as_view(), name="home"),
    path(
        "login/",
        auth_views.LoginView.as_view(
            redirect_authenticated_user=True, template_name="users/login.html"
        ),
        name="login",
    ),
    path("register/", views.register_view, name="register"),
    path("logout/", views.logout_view, name="logout"),
    path("profile/account/", views.user_account_view, name="user_account"),
    path("profile/edit/", views.update_account_view, name="update"),
]
