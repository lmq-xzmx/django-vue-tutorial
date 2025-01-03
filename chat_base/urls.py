# urls.py

from django.urls import path
from .views import OpenAIChatAPIView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('api/openai/chat_base/', OpenAIChatAPIView.as_view(), name='openai_chat_base_api'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
