from django.db import models
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill
# Create your models here.
class Album(models.Model):
    content = models.CharField(max_length=20)
    image = ProcessedImageField(upload_to='', processors=[ResizeToFill(500, 250)], format='JPEG',options={'quality': 60})
    # image = models.ImageField(upload_to='', blank=True)