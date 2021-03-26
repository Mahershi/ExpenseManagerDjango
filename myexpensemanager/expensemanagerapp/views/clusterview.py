from rest_framework import viewsets
from rest_framework.permissions import AllowAny, IsAuthenticated
from ..models import Cluster
from django.db.models import QuerySet
from ..serializers import ClusterSerializer
from rest_framework.request import Request, QueryDict
from rest_framework.response import Response



class ClusterViewSet(viewsets.ModelViewSet):
    queryset: QuerySet = Cluster.objects.all()
    serializer_class = ClusterSerializer
    permission_classes = [AllowAny]

    def destroy(self, request, *args, **kwargs):
        resp = super(ClusterViewSet, self).destroy(request, *args, **kwargs)
        return Response(
            {
                "success": "true",
                "message": "Cluster Deleted"
            }
        )

    def list(self, request, *args, **kwargs):
        qp: QueryDict = request.query_params
        print(request.query_params)

        if qp.get('user_id') is not None:
            self.queryset = self.queryset.filter(user_id__exact=qp.get('user_id'))

        self.queryset = self.queryset.order_by('-last_added')
        return Response(
            {
                "success": "true",
                "data": self.get_serializer(self.queryset, many=True).data,
                "message": "Clusters Fetched"
            }
        )

    def partial_update(self, request, *args, **kwargs):
        resp_data: Response = super(ClusterViewSet, self).partial_update(request, *args, **kwargs)
        return Response(
            {
                "success": "true",
                "data": resp_data.data,
                "message": "Cluster Updated"
            }
        )

    def create(self, request, *args, **kwargs):
        resp_data: Response = super(ClusterViewSet, self).create(request, *args, **kwargs)
        return Response(
            {
                "success": "true",
                "data": resp_data.data,
                "message": "Cluster Created"
            }
        )