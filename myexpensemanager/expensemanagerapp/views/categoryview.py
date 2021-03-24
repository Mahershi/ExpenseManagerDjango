from rest_framework import viewsets
from rest_framework.permissions import AllowAny, IsAuthenticated
from ..models import Category
from django.db.models import QuerySet
from ..serializers import CategorySerializer
from rest_framework.response import Response



class CategoryViewSet(viewsets.ModelViewSet):
    queryset: QuerySet = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [AllowAny]

    def list(self, request, *args, **kwargs):
        return Response(
            {
                "success": "true",
                "data": self.get_serializer(self.queryset, many=True).data
            }
        )