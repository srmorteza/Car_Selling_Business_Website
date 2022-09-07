from django.db import models

# Create your models here.
class Team(models.Model):
    fisrt_name=models.CharField(max_length= 255)
    last_name=models.CharField(max_length= 255)
    designation=models.CharField(max_length= 255)
    photo = models.ImageField(upload_to='photos/%Y/%M/%D/')
    facebook_link=models.URLField(max_length=100)
    twitter_link=models.URLField(max_length=100)
    googlePlus_link=models.URLField(max_length=100)
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.fisrt_name


