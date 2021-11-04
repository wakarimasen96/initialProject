from rest_framework import serializers
from django.contrib.auth.models import User

# Serializers define the API representation.
from endpoints.models import Student, Topic


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'is_staff']


class StudentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Student
        fields = ['name', 'surname', 'age']


class TopicSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Topic
        fields = ['name', 'course', 'students_count', 'students']
