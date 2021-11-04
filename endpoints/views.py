from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from rest_framework import viewsets
from django.contrib.auth.models import User
from endpoints.serializers import UserSerializer, StudentSerializer, TopicSerializer
from django.views import View
from .models import Student, Topic


# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class TopicViewSet(viewsets.ModelViewSet):
    queryset = Topic.objects.all()
    serializer_class = TopicSerializer








class StudentView(View):
    def get(self, request):
        students = list(Student.objects.values())
        if len(students) > 0:
            datos = {'message': "Success", 'students': students}
        else:
            datos = {'message': "students not found..."}
            return JsonResponse(datos)

    def post(self, request):
        pass

    def put(self, request):
        pass

    def delete(self, request):
        pass


def status(request):
    method = request.method
    path = request.path
    context = {"method": method,
               "path": path}
    response = JsonResponse(context)
    return response
