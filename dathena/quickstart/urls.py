from django.conf.urls import url
from . import views
from .views import RegisterUsers,LoginView,FileUploadView,ListFile
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('auth/register/', RegisterUsers.as_view(), name="auth-register"),
    path('auth/login/', LoginView.as_view(), name="auth-login"),
    path('upload/', FileUploadView.as_view()),
    path('dathena/listfile/', ListFile.as_view(), name="listfile"),
]
if settings.DEBUG:
  urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)