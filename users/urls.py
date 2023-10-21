from django.urls import path
from .views import *

urlpatterns = [
    path("", profiles, name="profiles"),
    path("account/", account, name="my_account"),
    path("account/edit/", account_edit, name="account_edit"),
    path("profile/<uuid:id>/", get_profile, name="get_profile"),
    path("register/", register_user, name="register_user"),
    path("login/", login_user, name="login_user"),
    path("logout/", logout_user, name="logout_user"),
    path("malaka/add/", add_malaka, name="add_malaka"),
    path("malaka/edit/<uuid:id>/", edit_malaka, name="edit_malaka"),
    path("malaka/delete/<uuid:id>/", delete_malaka, name="delete_malaka"),
]
