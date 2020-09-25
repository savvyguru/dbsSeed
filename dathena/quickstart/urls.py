from django.conf.urls import url
from . import views
from .views import RegisterUsers,LoginView,FileUploadView,ListFile,updateScore,validateFormView
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
    path('auth/register/', RegisterUsers.as_view(), name="auth-register"),
    path('auth/login/', LoginView.as_view(), name="auth-login"),
    path('upload/', FileUploadView.as_view()),
    path('validateForm/', validateFormView.as_view()),
    path('listfile/', ListFile.as_view(), name="listfile"),
    path('login/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('updateScore/', updateScore.as_view()),
]
if settings.DEBUG:
  urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)