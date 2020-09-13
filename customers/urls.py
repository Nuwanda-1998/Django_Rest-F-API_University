from django.urls import path, include
from rest_framework_simplejwt import views as jwt_views
from .views import registration, ManageUserView







urlpatterns = [
    # Your URLs...
    path('token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', registration, name='register'),
    path('edit/', ManageUserView.as_view(), name='edit'),
]
