from django.urls import path
from .views import UserListView

urlpatterns = [
    path('all/', UserListView, name='user_list'),
]
