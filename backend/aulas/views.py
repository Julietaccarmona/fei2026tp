from rest_framework.generics import GenericAPIView
from rest_framework.mixins import (
    ListModelMixin,
    CreateModelMixin,
    RetrieveModelMixin,
    UpdateModelMixin,
    DestroyModelMixin
)

from .models import Carrera, Profesor
from .serializers import CarreraSerializer, ProfesorSerializer


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


class ProfesorMixinDetail(
    GenericAPIView,
    RetrieveModelMixin,
    UpdateModelMixin,
    DestroyModelMixin
):

    queryset = Profesor.objects.all()
    serializer_class = ProfesorSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
