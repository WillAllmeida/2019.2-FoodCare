from rest_framework import serializers
from .models import Evento

class EventoSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Evento
        fields = '__all__'
        lookup_fields = "__all__"


