from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token  # <-- Here
from rest_framework_simplejwt.views import (
    TokenRefreshView,
    TokenVerifyView
)
from . import views

urlpatterns = [
    path("register/", views.register, name="register"),
    # path("api/todos/today/", views.isTodayTodo, name="today"),
    path('api/token/', views.MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]