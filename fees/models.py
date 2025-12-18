from django.db import models
from accounts.models import User

class Fee(models.Model):
    student = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        limit_choices_to={'role': 'student'}
    )
    month = models.CharField(max_length=20)
    amount = models.IntegerField()
    paid = models.BooleanField(default=False)

    def _str_(self):
        return f"{self.student.username} - {self.month}"