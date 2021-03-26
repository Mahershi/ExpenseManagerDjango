from rest_framework import viewsets
from ..models import Expense, Cluster
from ..serializers import ExpenseSerializer, ClusterSerializer
from django.db.models import QuerySet
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.request import Request, QueryDict
from django.utils import timezone



class ExpenseViewSet(viewsets.ModelViewSet):
    queryset: QuerySet = Expense.objects.all()
    serializer_class = ExpenseSerializer
    permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs):
        clusterId = request.data.get('cluster')
        print("Cluster:" + str(clusterId))

        try:
            if clusterId is not None:
                qs: QuerySet = Cluster.objects.all()
                cluster: Cluster = qs.filter(id__exact=clusterId).get()
                print(type(cluster))
                cluster.expenses = cluster.expenses + 1
                cluster.last_added = timezone.now()
                cluster.save()

            creat_res: Response = super(ExpenseViewSet, self).create(request, *args, **kwargs)

            # clusterId = creat_res.data.get('cluster')


            return Response(
                {
                    "success": "true",
                    "data": creat_res.data,
                    "message": "Expense Added"
                }
            )
        except:
            return Response(
                {
                    "success": "false",
                    "error": "Error Adding Expense"
                }
            )


    def list(self, request, *args, **kwargs):
        qp: QueryDict = request.query_params
        print(request.query_params)

        if (qp.get('cluster') is not None):
            self.queryset = self.queryset.filter(cluster_id__exact=qp.get('cluster'))

        if (qp.get('start') is not None):
            self.queryset = self.queryset.filter(expense_date__range=[qp.get('start'), qp.get('end')])

        elif (qp.get('month') is not None):
            print("has month")
            self.queryset = self.queryset.filter(expense_date__month=qp.get('month')).filter(expense_date__year=qp.get('year'))
        if (qp.get('user_id') is not None):
            self.queryset = self.queryset.filter(user_id__exact=qp.get('user_id'))

        # self.queryset = self.queryset.order_by('-expense_date', '-id', )
        self.queryset = self.queryset.order_by('-expense_date',)
        return Response(
            {
                "success": "true",
                "data": self.get_serializer(self.queryset, many=True).data,
                "message": "Expenses Fetched"
            }
        )


    def partial_update(self, request, *args, **kwargs):
        print(str(request.data))
        clusterId = request.data.pop('cluster')
        print("removed cluster: " + str(clusterId))
        print(str(request.data))
        resp_updated = super(ExpenseViewSet, self).partial_update(request, *args, **kwargs)
        return Response(
            {
                "success": "true",
                "data": resp_updated.data,
                "message": "Expense Updated"
            }
        )

    @action(detail=False, methods=['GET'])
    def date_span(self, request: Request, pk=None):
        qp: QueryDict = request.query_params
        if (qp.get('user_id') is not None):
            self.queryset = self.queryset.filter(user_id__exact=qp.get('user_id'))

        try:
            expense_latest: Expense = self.queryset.latest('expense_date')
            expense_oldest: Expense = self.queryset.earliest('expense_date')

            print(expense_oldest)
            serializer_oldest = ExpenseSerializer(expense_oldest, many=False)
            serializer_latest = ExpenseSerializer(expense_latest, many=False)

            date_latest: str = serializer_latest.data.pop('expense_date')
            date_oldest: str = serializer_oldest.data.pop('expense_date')

            return Response(
                {
                    "success": "true",
                    "data": {
                        'latest_month': date_latest[5:7],
                        'oldest_month': date_oldest[5:7],
                        'latest_year': date_latest[0:4],
                        'oldest_year': date_oldest[0:4]
                    },
                    "message": "Fetched Date Span"
                }
            )
        except:
            return Response(
                {
                    "success": "false",
                    "data": {
                        'oldest_month': 1,
                        'oldest_year': 2020
                    },
                    "error": "Default Date Span"
                }
            )



    @action(detail=False, methods=['GET'])
    def latest(self, request: Request, pk=None):
        qp: QueryDict = request.query_params

        if qp.get('user_id') is not None:
            self.queryset = self.queryset.filter(user_id__exact=qp.get('user_id'))

        self.queryset = self.queryset.latest('expense_date')
        serializer = ExpenseSerializer(self.queryset, many=False)

        return Response(
            {
                "success": "true",
                "data": serializer.data
            }
        )

    @action(detail=False, methods=['GET'])
    def oldest(self, request: Request, pk=None):
        qp: QueryDict = request.query_params

        if qp.get('user_id') is not None:
            self.queryset = self.queryset.filter(user_id__exact=qp.get('user_id'))

        self.queryset = self.queryset.earliest('expense_date')
        serializer = ExpenseSerializer(self.queryset, many=False)

        return Response(
            {
                "success": "true",
                "data": serializer.data
            }
        )

    @action(detail=False, methods=['POST'])
    def change_cluster(self, request: Request, pk=None):
        data = request.data
        try:
            new_cluster_id = data.get('new_cluster_id')
            old_cluster_id = data.get('old_cluster_id')
            expense_id = data.get('expense_id')

            if old_cluster_id != 0:
                old_cluster: Cluster = Cluster.objects.all().filter(id__exact=old_cluster_id).get()
                if old_cluster.expenses > 0:
                    old_cluster.expenses = old_cluster.expenses - 1
                old_cluster.save()
            new_cluster: Cluster = Cluster.objects.all().filter(id__exact=new_cluster_id).get()
            expense: Expense = Expense.objects.all().filter(id__exact=expense_id).get()

            expense.cluster = new_cluster

            new_cluster.expenses = new_cluster.expenses + 1
            new_cluster.last_added = timezone.now()
            new_cluster.save()

            expense.save()

            return Response(
                {
                    "success": "true",
                    "message": "Cluster Changed"
                }
            )

        except:
            return Response(
                {
                    "success": "false",
                    "error": "Error Changing Cluster"
                }
            )

    @action(detail=False, methods=['POST'])
    def remove_cluster(self, request: Request, pk=None):
        data = request.data
        try:
            expense_id = data.get('expense_id')
            expense: Expense = Expense.objects.all().filter(id__exact=expense_id).get()

            expense.cluster = None

            old_cluster_id = data.get('cluster_id')
            old_cluster: Cluster = Cluster.objects.all().filter(id__exact=old_cluster_id).get()
            if old_cluster.expenses > 0:
                old_cluster.expenses = old_cluster.expenses - 1

            old_cluster.save()
            expense.save()

            return Response(
                {
                    "success": "true",
                    "message": "Removed from Cluster"
                }
            )

        except:
            return Response(
                {
                    "success": "false",
                    "error": "Error Removing from Cluster"
                }
            )


    def destroy(self, request, *args, **kwargs):
        instance: Expense = self.get_object()
        print(instance.pk)
        cluster: Cluster = instance.cluster

        if cluster is not None:
            print(cluster.pk)
            if cluster.expenses > 0:
                cluster.expenses = cluster.expenses - 1
            cluster.save()

        resp = super(ExpenseViewSet, self).destroy(request, *args, *kwargs)

        return Response(
            {
                "success": "true",
                "message": "Expense Deleted"
            }
        )


