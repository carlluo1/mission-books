from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=255)
    #bookName = models.CharField(max_length=255)
    #email = models.CharField(max_length=255)
    #bookType = models.CharField(max_length=255)
    #academicSubject = models.CharField(max_length=255)
    #year = models.CharField(max_length=255)
    #price = models.CharField(max_length=255)
    #phonenumber = models.CharField(max_length=255)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
