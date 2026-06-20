from django.test import TestCase
from .models import Subject, Student, Homework
from datetime import date


class HomeworkModelTest(TestCase):

    def test_create_homework(self):

        subject = Subject.objects.create(
            name="Informatyka"
        )

        student = Student.objects.create(
            first_name="Jan",
            last_name="Kowalski"
        )

        homework = Homework.objects.create(
            description="Przygotować prezentację",
            due_date=date.today(),
            status="TODO",
            subject=subject,
            student=student
        )

        self.assertEqual(
            homework.description,
            "Przygotować prezentację"
        )