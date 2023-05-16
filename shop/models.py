from django.db import models
from django.utils import timezone


class Category(models.Model):

    class Meta:

        verbose_name = 'category'

        verbose_name_plural = 'categories'

    created_at = models.DateTimeField(default=timezone.now)

    title = models.CharField(max_length=128)

    def __str__(self):
        return self.title


class Course(models.Model):

    class Meta:

        verbose_name = 'course'

        verbose_name_plural = 'courses'

    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    created_at = models.DateTimeField(default=timezone.now)

    price = models.FloatField()

    review_quantity = models.IntegerField()

    student_quantity = models.IntegerField()

    title = models.CharField(max_length=256)

    def __str__(self):
        return self.title
