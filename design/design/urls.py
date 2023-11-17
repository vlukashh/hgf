from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView
from django.conf.urls.static import static

from django.conf import settings
from django.views.decorators.cache import never_cache
from django.views.static import serve


urlpatterns = [
   path('admin/', admin.site.urls),
   path('', include('main.urls', namespace='')),
   path('main/', include('main.urls')),
   path('', RedirectView.as_view(url='/main/', permanent=True)),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



