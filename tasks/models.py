from django.core.validators import MinLengthValidator
from django.db import models


class Subject(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Student(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Homework(models.Model):

    STATUS_CHOICES = [
        ('TODO', 'Do zrobienia'),
        ('IN_PROGRESS', 'W trakcie'),
        ('DONE', 'Zrobione'),
    ]

    description = models.TextField(
    verbose_name="Opis zadania",
    validators=[
        MinLengthValidator(
            5,
            message="Opis musi zawierać co najmniej 5 znaków."
        )
    ]
)
    
    due_date = models.DateField(
        verbose_name="Termin wykonania"
    )
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='TODO'
    )

    subject = models.ForeignKey(
        Subject,
        on_delete=models.CASCADE
    )

    student = models.ForeignKey(
        Student,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.description