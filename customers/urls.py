from django.urls import path
from rest_framework_simplejwt import views as jwt_views
from .views import registration, ManageUserView







urlpatterns = [
    # Your URLs...
    path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('api/register/', registration, name='register'),
    path('api/edit/', ManageUserView.as_view(), name='edit'),
]
