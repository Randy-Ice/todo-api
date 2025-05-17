from django.shortcuts import render
from rest_framework import request
from rest_framework.viewsets import ModelViewSet

#* sorting filtering and pagination
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.pagination import PageNumberPagination
# Create your views here.

from .models import Task
from .serializers import TodoSerializer
from .permissions import TodoPermission

class TodoViewSet(ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TodoSerializer
    permission_classes = [TodoPermission]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    search_fields = ['description__istartswith', 'time_sensitive']
    ordering_fields = ['created_at', 'updated_at', 'time_sensitive']
    pagination_class = PageNumberPagination
    def get_queryset(self):
        user = self.request.user
        return Task.objects.filter(author=user).order_by('-created_at')

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
