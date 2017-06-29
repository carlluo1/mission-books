from django.db import models
from django.utils import timezone


class Book(models.Model):
    seller = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    email = models.CharField(max_length=255)
    booktype = models.CharField(max_length=255)
    academicsubject = models.CharField(max_length=255)
    year = models.CharField(max_length=255)
    price = models.CharField(max_length=255)
    phonenumber = models.CharField(max_length=255)
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
