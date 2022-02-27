from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework_simplejwt.views import TokenObtainPairView, TokenVerifyView, TokenRefreshView, TokenBlacklistView

from .views import RegisterView, MyTokenObtainPairView


urlpatterns = [
    # path('login/', obtain_auth_token, name='login'),
    path('register/', RegisterView.as_view(), name='register'),

    path('login/token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('logout/', TokenBlacklistView.as_view(), name='token_blacklist'),
    path('login/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('login/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

]