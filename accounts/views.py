from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

@login_required
def dashboard(request):
    user = request.user

    if not hasattr(user, 'role') or not user.role:
        return render(request, 'accounts/school_dashboard.html')

    if user.role == 'school':
        return render(request, 'accounts/school_dashboard.html')

    elif user.role == 'teacher':
        return render(request, 'accounts/teacher_dashboard.html')

    elif user.role == 'student':
        return render(request, 'accounts/student_dashboard.html')

    elif user.role == 'parent':
        return render(request, 'accounts/parent_dashboard.html')

    else:
        return redirect('/accounts/login/')