from rest_framework import viewsets
from rest_framework.permissions import AllowAny, IsAuthenticated
from ..models import Cluster
from django.db.models import QuerySet
from ..serializers import ClusterSerializer


class ClusterViewSet(viewsets.ModelViewSet):
    queryset: QuerySet = Cluster.objects.all()
    serializer_class = ClusterSerializer
    permission_classes = [AllowAny]