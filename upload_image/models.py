from django.db import models


# Create your models here.
from upload_image.utility import image_path


class Images(models.Model):
    title = models.CharField(max_length=32, verbose_name='Title')
    image = models.ImageField(upload_to=image_path, verbose_name='Image')
