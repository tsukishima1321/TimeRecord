from django.urls import path, re_path
from django.conf.urls import url
from django.conf.urls.static import static
from django.conf import settings
 
from . import views
 
urlpatterns = [
    re_path('^api/$',views.api),
]


urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)