from django.db import models
from django.utils import timezone


class Category(models.Model):

    title = models.CharField(max_length=255)

    created_at = models.DateTimeField(default=timezone.now)


class Course(models.Model):

    title = models.CharField(max_length=512)

    price = models.FloatField()

    student_quantity = models.IntegerField()

    review_quantity = models.IntegerField()

    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    created_at = models.DateTimeField(default=timezone.now)
