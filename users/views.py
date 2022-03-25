from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from .models import User
from .serializers import UserSerializer
from rest_framework.response import Response


class UserViewSet(viewsets.ViewSet):
    """
    A simple ViewSet for listing and retrieving users
    """
    def list(self, request):
        queryset = User.objects.all()
        serializer = UserSerializer(queryset, many=True)
        return Response(serializer.data)

    def retreive(self, request, pk=None):
        queryset = User.objects.all()
        user = get_object_or_404(queryset, pk=pk)
        serializer = UserSerializer(user)
        return Response(serializer.data)
