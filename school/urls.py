from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    # Django auth (login, logout)
    path('accounts/', include('django.contrib.auth.urls')),

    # Our app urls
    path('accounts/', include('accounts.urls')),

    path('attendance/', include('attendance.urls')),

    path('fees/', include('fees.urls')),
]