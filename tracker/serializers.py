from rest_flex_fields import FlexFieldsModelSerializer
from . models import Category,Expense,sharedexpense
from users.serializers import UserlistSerializer
class CategorySerializer(FlexFieldsModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"

class expenseSerializer(FlexFieldsModelSerializer):
    class Meta:
        model = Expense
        fields = "__all__"

        expandable_fields = {
            "category": CategorySerializer ,
            "user": UserlistSerializer,
        }
class sharedexpenseSerializer(FlexFieldsModelSerializer):
    class Meta:
        model = sharedexpense
        fields = "__all__"

        expandable_fields = {
            "expenses": (expenseSerializer, {"many":True}),
            "created_by": UserlistSerializer,
            "users": (UserlistSerializer, {"many":True} ),
        }