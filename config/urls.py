from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/admin/', RedirectView.as_view(url='/admin/', permanent=False)),
    path('accounts/', include('accounts.urls')),
]
