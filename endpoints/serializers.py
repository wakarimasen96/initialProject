from rest_framework import serializers
from django.contrib.auth.models import User


# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'is_staff']

    # SE ENCARGA DE CONVERTIR PYTHON EN JSON

    def create(self, validated_data):
        instance = User()
        instance.Meta = validated_data
        return instance

