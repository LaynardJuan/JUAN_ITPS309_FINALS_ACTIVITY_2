from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    path("", RedirectView.as_view(url="/accounts/login/", permanent=False)),
    path("admin/", admin.site.urls),
    path("accounts/admin/", RedirectView.as_view(url="/admin/", permanent=False)),
    path("accounts/", include("accounts.urls")),
    path("students/", include("students.urls")),
]