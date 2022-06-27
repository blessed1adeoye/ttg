
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from b.admin import church_site


urlpatterns = [
    path('admin/', admin.site.urls),
    path('CHURCH/', church_site.urls),
    path('', include('b.urls')),
    # path('c', include('c.urls')),
    # path('accounts/', include('django.contrib.auth.urls'))
]
# if settings.DEBUG:
#     urlpatterns +=  static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)