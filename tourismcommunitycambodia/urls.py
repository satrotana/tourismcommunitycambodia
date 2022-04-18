
from django.urls import path, include
from django.conf.urls.i18n import i18n_patterns


urlpatterns = [
    path('', include('webpage.urls')),
]

urlpatterns += i18n_patterns(
    path('', include('webpage.urls')),
)
