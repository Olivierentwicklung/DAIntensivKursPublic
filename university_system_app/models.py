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


class Semester(models.Model):
    name = models.CharField(max_length=150)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return f"Semester: {self.name} ({self.start_date} - {self.end_date})"


class Kurs(models.Model):
    title = models.CharField(max_length=150)
    code = models.CharField(max_length=18)

    # Professor 1:n Kurs
    professor = models.ForeignKey(
        Professor,
        on_delete=models.CASCADE,
        related_name="kurse",
    )

    # Semester 1:n Kurs
    semester = models.ForeignKey(
        Semester,
        on_delete=models.CASCADE,
        related_name="kurse",
    )

    # Student m:n Kurs
    students = models.ManyToManyField(
        Student,
        related_name="kurse",
    )

    def __str__(self):
        return f"{self.code} - {self.title}"


class Kursbeschreibung(models.Model):
    description = models.TextField()

    kurs = models.OneToOneField(
        Kurs,
        on_delete=models.CASCADE,
        related_name="kursbeschreibung",
    )

    def __str__(self):
        return f"Beschreibung für {self.kurs}"
