from django.db import models

# Create your models here.


class Grafic(models.Model):
    title = models.CharField(max_length=255)
    img = models.ImageField(upload_to='seaborn_and_AI_app/templates/images', height_field=480, width_field=640)

    def __str__(self):
        return self.title
