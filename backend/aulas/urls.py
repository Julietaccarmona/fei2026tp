from django.urls import path

from .views import CarreraMixin, ProfesorMixinDetail

urlpatterns = [
    path(
        "carreras/",
        CarreraMixin.as_view(),
        name="carreras"
    ),

    path(
        "profesor/<int:pk>/",
        ProfesorMixinDetail.as_view(),
        name="profesor-detail"
    ),
]
