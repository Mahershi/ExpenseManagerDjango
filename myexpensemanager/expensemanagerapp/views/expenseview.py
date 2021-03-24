from rest_framework import viewsets
from ..models import Expense
from ..serializers import ExpenseSerializer
from django.db.models import QuerySet
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.request import Request, QueryDict


class ExpenseViewSet(viewsets.ModelViewSet):
    queryset: QuerySet = Expense.objects.all()
    serializer_class = ExpenseSerializer
    permission_classes = [AllowAny]

    def list(self, request, *args, **kwargs):
        qp: QueryDict = request.query_params
        print(request.query_params)
        if (qp.get('start') is not None):
            self.queryset = self.queryset.filter(expense_date__range=[qp.get('start'), qp.get('end')])

        elif (qp.get('month') is not None):
            print("has month")
            self.queryset = self.queryset.filter(expense_date__month=qp.get('month')).filter(expense_date__year=qp.get('year'))
        if (qp.get('user_id') is not None):
            self.queryset = self.queryset.filter(user_id__exact=qp.get('user_id'))

        self.queryset = self.queryset.order_by('-expense_date')
        return Response(
            {
                "success": "true",
                "data": self.get_serializer(self.queryset, many=True).data
            }
        )


    def partial_update(self, request, *args, **kwargs):
        resp_updated = super(ExpenseViewSet, self).partial_update(request, *args, **kwargs)
        return Response(
            {
                "success": "true",
                "data": resp_updated.data
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
                    }
                }
            )
        except:
            return Response(
                {
                    "success": "false",
                    "data": {
                        'oldest_month': 1,
                        'oldest_year': 2020
                    }
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




