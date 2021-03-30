from django.db import models

class Date(models.Model):
    date = models.DateTimeField(auto_now=False, auto_now_add=False)