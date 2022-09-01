from django.db import models

# Create your models here.
class Speciality(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length = 100)
    icon = models.CharField(max_length=400)
    date_created = models.DateField(auto_created=True)

    def __str___(self):
        return self.id