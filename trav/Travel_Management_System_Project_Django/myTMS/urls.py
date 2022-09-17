from django.contrib import admin
from django.urls import include, re_path
urlpatterns = [
    re_path(r'^admin/', admin.site.urls),
    re_path(r'^loginmodule/', include('loginmodule.urls')),
    re_path(r'^SignupApp/', include('SignupApp.urls')),
    re_path(r'^BookTicketApp/', include('BookTicketApp.urls')),
    re_path(r'^PaymentApp/', include('PaymentApp.urls')),
]
