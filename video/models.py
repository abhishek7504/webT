from django.db import models
import datetime
# Create your models here.

class Video(models.Model):
    title = models.CharField(max_length=255)
    Embed_code = models.TextField()
    Description = models.TextField()
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.title


class VideoUpload(models.Model):
    name= models.CharField(max_length=500)
    videofile= models.FileField(upload_to='videos/', null=True, verbose_name="")

    def __str__(self):
        return self.name + ": " + str(self.videofile)

class Banner(models.Model):

    img1 = models.ImageField(upload_to='banner/',null=True , verbose_name="image 1")
    img2 = models.ImageField(upload_to='banner/', null=True, verbose_name="image 2")
    img3 = models.ImageField(upload_to='banner/', null=True, verbose_name="image 3")
    img4 = models.ImageField(upload_to='banner/', null=True, verbose_name="image 4")

    # def __str__(self):
    #     return self.img1