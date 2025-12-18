from django.db import models
from accounts.models import User

class Attendance(models.Model):
    student = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        limit_choices_to={'role': 'student'}
    )
    date = models.DateField()
    status = models.BooleanField(default=True)  # Present=True, Absent=False

    def _str_(self):
        return f"{self.student.username} - {self.date}"