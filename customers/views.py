from django.contrib.auth import get_user_model
from rest_framework import permissions, generics
from rest_framework import response, decorators, permissions, status
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import UserSerializer

User = get_user_model()

@decorators.api_view(["POST"])
@decorators.permission_classes([permissions.AllowAny])
def registration(request):
    serializer = UserSerializer(data=request.data)
    if not serializer.is_valid():
        return response.Response(serializer.errors, status.HTTP_400_BAD_REQUEST)        
    user = serializer.save()
    refresh = RefreshToken.for_user(user)
    res = {
        "refresh": str(refresh),
        "access": str(refresh.access_token),
    }
    return response.Response(res, status.HTTP_201_CREATED)
    



class ManageUserView(generics.RetrieveUpdateAPIView):
    "Manage The Authennticated User"
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_object(self):
        "retrieve And return authenticated User"
        return self.request.user