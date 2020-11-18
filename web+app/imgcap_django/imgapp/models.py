from __future__ import unicode_literals
from django.db import models
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill



# Create your models here.
class IMG(models.Model):
    # img = models.ImageField(upload_to='upload')
    img = ProcessedImageField(upload_to='upload',
                              processors=[ResizeToFill(320, 320)],
                              format='JPEG',
                              options={'quality': 60})