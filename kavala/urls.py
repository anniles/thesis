"""thesis URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.urls import reverse
from django.conf.urls.static import static
from django.conf import settings

from django.contrib import admin
from django.views.generic import TemplateView
from registration.backends.simple.views import RegistrationView


class MyRegistrationView(RegistrationView):
    def get_success_url(self, user):
        return reverse('user_profile:profile', current_app=self.request.resolver_match.namespace)

urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name='homepage.html'), name='homepage'),
    url(r'^hotels/',include('hotels.urls')),
    url(r'^rentals/',include('rentals.urls')),
    url(r'^contact/',include('contact.urls')),
    url(r'^sights/',include('sights.urls')),
    url(r'^transport/',include('transport.urls')),
    url(r'^search/',include('booking.urls')),
    url(r'^settings/',include('user_profile.urls')),
    url(r'^accounts/register/$', MyRegistrationView.as_view(), name='registration_register'),
    url(r'^accounts/', include('registration.backends.simple.urls')),
    url(r'^admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

