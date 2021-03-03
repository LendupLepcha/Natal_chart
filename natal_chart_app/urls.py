from django.contrib import admin
from django.urls import path, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib.staticfiles.urls import static
from . import views
from chart import views as chart_view
from accounts import views as account_view
from django.conf import settings
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', account_view.view_login),
    path('accounts/', include('accounts.urls')),
    path('chart/', include('chart.urls'))
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

