from django.db import models

# Create your models here.
class media(models.Model):
    name=models.CharField(max_length=100)
    date_added=models.DateTimeField(auto_now_add=True)
    file=models.FileField()

    def __str__(self):
        return self.name