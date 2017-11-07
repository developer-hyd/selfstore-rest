from django.db import models

class Link(models.Model):

    title = models.CharField(max_length=200, blank=True, default='')
    subject = models.CharField(default='python', max_length=100)
    link = models.CharField(default='python', max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    description = models.TextField()
