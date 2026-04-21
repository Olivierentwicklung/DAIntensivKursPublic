from django.db import models

# Create your models here.


class Student(models.Model):
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    matriculation_number = models.CharField(max_length=18)

    def __str__(self):
        return f"{self.first_name} {self.last_name} {self.matriculation_number}"
