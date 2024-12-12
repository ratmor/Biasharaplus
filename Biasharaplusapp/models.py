from django.db import models

class Images(models.Model):
    description=models.CharField(max_length=20)
    image=models.FileField(upload_to='images/')