from django.db import models

# Create your models here.

class Student(models.Model):

    name = models.CharField(max_length=60)
    student_id = models.IntegerField()
    adress= models.CharField(max_length=120)
    major_interest=models.CharField(max_length=30)
    university_interest=models.CharField(max_length=30)

    class Meta:
        db_table = 'students'

    def __str__(self):
        return self.name