from django.db import models

class dashboard(models.Model):
    # user
    first_name  = models.CharField(max_length=50)
    last_name   = models.CharField(max_length=50)
    age = models.IntegerField(null=True)

    # incident
    fire = models.CharField(max_length=50)
    police = models.CharField(max_length=50)
    medical = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now=True)

    # maps
    getmap = models.URLField(max_length=200)
    pinned_map = models.URLField(max_length=200)
