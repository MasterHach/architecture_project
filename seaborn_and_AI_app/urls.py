from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    path('<str:a>/<str:b>/<str:c>/', views.index),
    path('<str:a>/<str:b>/<str:c>/forecast.png', views.index),
]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)

