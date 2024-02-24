from django.shortcuts import render
from rest_framework import viewsets, permissions
from rest_framework.exceptions import PermissionDenied
from .serializers import TaskSerializer, CategorySerializer
from .models import Task, Category


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAdminUser]

    def perform_update(self, serializer):
        if not self.request.user.is_superuser:
            raise PermissionDenied("You do not have permission to update this task.")
        serializer.save()

    def perform_delete(self, instance):
        if not self.request.user.is_superuser:
            raise PermissionDenied("You do not have permission to delete this task.")
        instance.delete()

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAdminUser]

    def perform_update(self, serializer):
        if not self.request.user.is_superuser:
            raise PermissionDenied("You do not have permission to update this category.")
        serializer.save()

    def perform_delete(self, instance):
        if not self.request.user.is_superuser:
            raise PermissionDenied("You do not have permission to delete this category.")
        instance.delete()