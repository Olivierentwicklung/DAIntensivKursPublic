from django.db import models

# Create your models here.


class Student(models.Model):
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    matriculation_number = models.CharField(max_length=18)

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.matriculation_number})"


class Studentenausweis(models.Model):
    card_number = models.CharField(max_length=50)
    issued_at = models.DateField()

    student = models.OneToOneField(
        Student,
        on_delete=models.CASCADE,
        related_name="studentenausweis",
    )

    def __str__(self):
        return f"Ausweis {self.card_number} - {self.issued_at} - {self.student}"


class Professor(models.Model):
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    employee_number = models.CharField(max_length=18)

    def __str__(self):
        return f"Prof. {self.first_name} {self.last_name} ({self.employee_number})"
