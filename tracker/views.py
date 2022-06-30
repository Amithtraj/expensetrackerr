
from .models import Expense,Category,sharedexpense
from django_filters.rest_framework import DjangoFilterBackend
from rest_flex_fields import FlexFieldsModelViewSet, is_expanded
from rest_framework.filters import OrderingFilter, SearchFilter
from . serializers import CategorySerializer,expenseSerializer,sharedexpenseSerializer
from rest_framework.decorators import action
from rest_framework.response import Response




class categoryViewSet(FlexFieldsModelViewSet):

    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter)
    search_fields = ["name", "code", "id"]
    # filterset_fields = (
    #     "is_active",
    #     "is_percent",
    #     "is_limited",
    # )
    ordering_fields = [
        "name",
        "id",
    ]

class ExpenseViewSet(FlexFieldsModelViewSet):

    queryset = Expense.objects.all()
    serializer_class = expenseSerializer
    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter)
    search_fields = ["name", "id"]
    filterset_fields = (
        "date",
        "category",
        "amount",
        "created_at",
        "user",
    )
    ordering_fields = [
        "name",
        "id",
    ]

    @action(detail=False, methods=["GET"], name="total")
    def total(self, request, *args, **kwargs):
        # objects = self.paginate_queryset(self.get_queryset())
        # serializer = self.get_serializer(objects, many=True)
        total=0
        exp = Expense.objects.all()
       # .filter(user=request.user)
        for s in exp:
            total=total+s.amount
        return Response({"total":total})

class sharedexpenseViewSet(FlexFieldsModelViewSet):

    queryset = sharedexpense.objects.all()
    serializer_class = sharedexpenseSerializer
    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter)
    search_fields = ["name", "id"]
    filterset_fields = (
        "date",
        "total",
        "created_by",
    )
    ordering_fields = [
        "name",
        "id",
    ]