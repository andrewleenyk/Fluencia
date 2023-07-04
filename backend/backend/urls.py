from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("cards/", include("cards.urls")),
    path("admin/", admin.site.urls),
]