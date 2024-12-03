# todo_list/todo_app/urls.py
from django.urls import path
from todo_app import views

urlpatterns = [
    path("",
        views.ListListView.as_view(), name="index"),
    path("list/<int:list_id>/",
        views.ItemListView.as_view(), name="list"),
    # CRUD patterns for ToDoLists
    path(
        "list/<int:pk>/delete/", views.ListDelete.as_view(), name="list-delete"
    ),
    # CRUD patterns for ToDoItems
    path(
        "list/<int:list_id>/item/<int:pk>/delete/",
        views.ItemDelete.as_view(),
        name="item-delete",
    )
]