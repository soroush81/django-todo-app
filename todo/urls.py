from django.urls import path
from .views import LogoutView,MyTokenObtainPairView
from .api import RegisterApi
from rest_framework.authtoken.views import obtain_auth_token  # <-- Here
from rest_framework_simplejwt.views import (
    TokenRefreshView,
    TokenVerifyView
)

urlpatterns = [
    path("api/register/", RegisterApi.as_view(), name="register"),
    path('api/token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('api/token/logout/', LogoutView.as_view(), name='auth_logout'),

]