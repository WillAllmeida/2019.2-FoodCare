from rest_framework import serializers
from .models import Usuario
from django.contrib.auth.models import User
class UsuarioSerializer(serializers.ModelSerializer):
    user =  serializers.SerializerMethodField()
    class Meta:
        model = Usuario
        fields = "__all__"
    def get_user(self,obj):
        return obj.user.username
        