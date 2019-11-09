from rest_framework import serializers
from .models import Usuario

class UsuarioSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Usuario
        fields = '__all__'
        lookup_fields = "__all__"           