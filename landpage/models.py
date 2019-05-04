from django.db import models
from django.shortcuts import reverse
from django.core.validators import FileExtensionValidator

# Create your models here.
class landpage(models.Model):    
    
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})

class Device(models.Model):
    image =  models.ImageField(upload_to = 'media/', default = 'media/default_dev.jpg')
    manual = models.FileField(upload_to='media/',
                            default = 'media/default_manual.pdf',
                            validators = [FileExtensionValidator(allowed_extensions=['pdf'])],
                            blank = True,
                            null = True)