from django.urls import path

from .views import CarreraMixin

urlpatterns = [
    path(
        "carreras/",
        CarreraMixin.as_view(),
        name="carreras"
    ),
]
