# todo_list/todo_app/urls.py
from todo_app import views

urlpatterns = [
    path("",
        views.ListListView.as_view(), name="index"),
    path("list/<int:list_id>/",
        views.ItemListView.as_view(), name="list"),
]