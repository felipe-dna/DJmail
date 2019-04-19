from django.contrib import admin
from django.urls import path, include

# settings
from django.conf import settings
from django.conf.urls.static import static

# local
from apps.accounts import urls as accounts_urls

# URLS.
urlpatterns = [
    path('admin/', admin.site.urls),

    # accounts urls
    path('accounts/', include(accounts_urls, namespace="accounts")),
]

# Media and Static configs.
# https://docs.djangoproject.com/pt-br/2.2/howto/static-files/
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


# Django debug toolbar configs.
# https://django-debug-toolbar.readthedocs.io/en/latest/
if settings.DEBUG:
    import debug_toolbar

    urlpatterns += [
        path('__debug__/', include(debug_toolbar.urls)),
    ]