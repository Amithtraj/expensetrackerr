from django.contrib import admin
from .models import Expense,Category,sharedexpense

@admin.register(Expense)
class expenseAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "amount",


    )
@admin.register(Category)
class categoryAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name"
    )

@admin.register(sharedexpense)
class sharedadmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name"
    )
