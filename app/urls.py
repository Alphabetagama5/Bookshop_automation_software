from django.urls import path
from .views import *
urlpatterns = [
    path("home", Home, name="home"),
    path("register", Register, name="register"),
    path("registration", Registration, name="registration"),
    path("", Login_view, name="login"),
    path("logout", signout, name="logout"),
    path("create_book", create_book, name="create_book"),
    path("add", add, name="add"),
    path("show_book", book_list, name="show_book"),
    path("delete/<int:pk>", Delete_data, name="delete"),
    path("updated_data/<int:pk>", updated, name="updated_data"),
]