from rest_framework import viewsets
from .models import Evento
from .serializers import EventoSerializer
from rest_framework.permissions import BasePermission, IsAuthenticated, SAFE_METHODS
from rest_framework import permissions
from users.models import Usuario
from django.contrib.auth.models import User

class ReadOnly(BasePermission):
    def has_permission(self, request, view):
        return request.method in SAFE_METHODS

class IsOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        a = obj.id_doador.id
        b = request.user.id
        print(a,b)
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.id_doador.id == request.user.id


class EventoViewSet(viewsets.ModelViewSet):

    serializer_class = EventoSerializer
    queryset = Evento.objects.all()
    permission_classes = [IsOwner] or [ReadOnly]
