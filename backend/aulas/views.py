from rest_framework.generics import GenericAPIView
from rest_framework.mixins import (
    ListModelMixin,
    CreateModelMixin
)

from .models import Carrera
from .serializers import CarreraSerializer


class CarreraMixin(
    GenericAPIView,
    ListModelMixin,
    CreateModelMixin
):

    queryset = Carrera.objects.all()
    serializer_class = CarreraSerializer

    def get(self, request):
        return self.list(request)

    def post(self, request):
        return self.create(request)
