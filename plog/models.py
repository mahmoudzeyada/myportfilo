from django.db import models

# Create your models here.
class plog(models.Model):
    title=models.CharField(max_length=200)
    pub_date=models.DateField(auto_now=True)
    body=models.CharField(max_length=500)
    image = models.ImageField(upload_to="images/")
