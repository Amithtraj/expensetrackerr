from django.db import models
from django.urls import reverse
from users.models import User



class Category(models.Model):

    name = models.CharField(max_length=1000, null=True)
    type = models.CharField(max_length=30)
    budget = models.FloatField(null=True,blank=True)
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        ordering = ['-id']

    def get_absolute_url(self):
        return reverse('tracker:Category')



class Expense(models.Model):
    name = models.CharField(max_length=1000, null=True)
    date = models.DateField()
    description = models.CharField(max_length=1000, null=True)
    amount = models.FloatField()
    created_at = models.DateField()
    category = models.ForeignKey(Category,on_delete=models.CASCADE, blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE,related_name="User")
    class Meta:
        verbose_name = 'Expense'
        verbose_name_plural = 'Expenses'
        ordering = ['-id']

    def get_absolute_url(self):
        return reverse('tracker:expense')

class sharedexpense(models.Model):
    name = models.CharField(max_length=1000, null=True)
    date = models.DateField()
    total = models.FloatField()
    expenses = models.ManyToManyField(Expense, blank=True, null=True,related_name="expenses")
    users = models.ManyToManyField(User,related_name="users",blank=True, null=True)
    created_by = models.ForeignKey(User,on_delete=models.CASCADE,blank=True, null=True)
    numberofusers = models.IntegerField(blank=True, null=True)
    class Meta:
        verbose_name = 'sharedexpense'
        verbose_name_plural = 'sharedexpenses'
        ordering = ['-id']

    def get_absolute_url(self):
        return reverse('tracker:sharedexpense')
