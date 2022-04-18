from django.db import models

class Customer(models.Model):
    name = models.CharField(max_length=200, null=True)
    password = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    department = models.CharField(max_length=200, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name



class Product(models.Model):
    CATEGORY = (
        ('Food', 'Food'),
        ('Clothing', 'Clothing'),
        ('Home Appliances', 'Home Appliances'),
        ('Groceries', 'Groceries'),
        ('Medical Aids', 'Medical Aids'),
    )
    name = models.CharField(max_length=200, null=True)
    user = models.ForeignKey(Customer, null=True, on_delete=models.SET_NULL)
    quantity = models.PositiveSmallIntegerField(null=True)
    category = models.CharField(max_length=200, null=True, choices=CATEGORY)
    description = models.CharField(max_length=200, null=True, blank=True)
    budget_amount = models.FloatField(null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.name

class Order(models.Model):
    STATUS = (
        ('Pending', 'Pending'),
        ('Out for delivery', 'Out for delivery'),
        ('Delivered', 'Delivered'),

    )
    CATEGORY = (
        ('Food', 'Food'),
        ('Clothing', 'Clothing'),
        ('Home Appliances', 'Home Appliances'),
        ('Groceries', 'Groceries'),
        ('Medical Aids', 'Medical Aids'),
    )
    category = models.CharField(max_length=30, null=False)
    product = models.CharField(max_length=30, null=False)
    date_created =models.DateTimeField(auto_now_add=True, null=True)
    status = models.CharField(max_length=200, null=True, choices=STATUS)
    quantity = models.PositiveSmallIntegerField(null=True)

    def __str__(self):
        return self.product












