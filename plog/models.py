from django.db import models


# Create your models here.
class plog(models.Model):
    title=models.CharField(max_length=200)
    pub_date=models.DateField(auto_now=True)
    body=models.TextField(max_length=500)
    image = models.ImageField(upload_to="images/")
    def __str__(self):
        return self.title
    def pretty_time(self):
        return self.pub_date.strftime("%Y %m %-d")
    def small_body(self):
        return self.body[:10]
