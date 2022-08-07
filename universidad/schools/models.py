from django.db import models

# Create your models here.

class School(models.Model):

    name = models.CharField(max_length=60)
    school_id = models.IntegerField()
    adress= models.CharField(max_length=120)
    areas=models.CharField(max_length=30)
    majors=models.CharField(max_length=30)
    schedule=models.CharField(max_length=30)

    class Meta:
        db_table = 'schools'

    def __str__(self):
        return self.name

# Create your models here.
