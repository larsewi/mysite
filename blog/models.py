from django.db import models

# Create your models here.

class BlogPost(models.Model):
    content = models.CharField(max_length=240)
    pub_date = models.DateTimeField("date published")
