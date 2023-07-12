from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("categories/", views.categories, name="categories"),
    path("terms_by_category/<str:category_name>/", views.terms_by_category, name="terms_by_category"),
]
