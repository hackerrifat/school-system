from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Fee

@login_required
def fee_report(request):
    user = request.user

    if user.role == 'student':
        fees = Fee.objects.filter(student=user)
    else:
        fees = Fee.objects.all()

    return render(request, 'fees/fee_report.html', {
        'fees': fees
    })