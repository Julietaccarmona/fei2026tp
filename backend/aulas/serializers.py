from rest_framework import serializers

from .models import (
    Carrera,
    Profesor,
    Materia,
    Aula,
)


class CarreraSerializer(serializers.ModelSerializer):
    class Meta:
        model = Carrera
        fields = "__all__"


class ProfesorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profesor
        fields = "__all__"


class MateriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Materia
        fields = "__all__"


class AulaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aula
        fields = "__all__"
