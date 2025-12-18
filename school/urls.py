from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

urlpatterns = [
    path('', lambda request: redirect('/accounts/login/')),
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('attendance/', include('attendance.urls')),
    path('fees/', include('fees.urls')),
]
urlpatterns = [
    path('admin/', admin.site.urls),

    # Django auth (login, logout)
    path('accounts/', include('django.contrib.auth.urls')),

    # Our app urls
    path('accounts/', include('accounts.urls')),

    path('attendance/', include('attendance.urls')),

    path('fees/', include('fees.urls')),
]