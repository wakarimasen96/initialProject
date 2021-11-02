from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from rest_framework import viewsets
from django.contrib.auth.models import User
from endpoints.serializers import UserSerializer


# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


def status(request):
    method = request.method
    path = request.path
    context = {"method": method,
               "path": path}
    response = JsonResponse(context)
    return response
