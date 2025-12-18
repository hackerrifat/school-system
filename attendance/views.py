from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from accounts.models import User
from .models import Attendance
from datetime import date

@login_required
def mark_attendance(request):
    students = User.objects.filter(role='student')

    if request.method == 'POST':
        for student in students:
            status = request.POST.get(str(student.id)) == 'on'
            Attendance.objects.create(
                student=student,
                date=date.today(),
                status=status
            )

    return render(request, 'attendance/mark_attendance.html', {
        'students': students
    })
@login_required
def attendance_report(request):
    user = request.user

    if user.role == 'student':
        records = Attendance.objects.filter(student=user)

    elif user.role == 'parent':
        # আপাতত parent সব student দেখবে (later link করবো)
        records = Attendance.objects.all()

    else:
        records = Attendance.objects.all()

    return render(request, 'attendance/attendance_report.html', {
        'records': records
    })