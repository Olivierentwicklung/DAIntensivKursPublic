from django.db import models

# Create your models here.


class Student(models.Model):
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    matriculation_number = models.CharField(max_length=18)

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.matriculation_number})"


class StudentID(models.Model):
    card_number = models.CharField(max_length=50)
    issued_at = models.DateField()

    # Student 1:1 StudentID
    student = models.OneToOneField(
        Student,
        on_delete=models.CASCADE,
        related_name="studentID",
    )

    def __str__(self):
        return f"ID card {self.card_number} - {self.issued_at} - {self.student}"


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


class Course(models.Model):
    title = models.CharField(max_length=150)
    code = models.CharField(max_length=18)

    # Professor 1:n Course
    professor = models.ForeignKey(
        Professor,
        on_delete=models.CASCADE,
        related_name="courses",
    )

    # Semester 1:n Course
    semester = models.ForeignKey(
        Semester,
        on_delete=models.CASCADE,
        related_name="courses",
    )

    # Student m:n Course
    students = models.ManyToManyField(
        Student,
        related_name="courses",
    )

    def __str__(self):
        return f"{self.code} - {self.title}"


class Course_description(models.Model):
    description = models.TextField()

    # Course 1:1 Course_description
    Course = models.OneToOneField(
        Course,
        on_delete=models.CASCADE,
        related_name="course_description",
    )

    def __str__(self):
        return f"Course description of {self.Course}"
