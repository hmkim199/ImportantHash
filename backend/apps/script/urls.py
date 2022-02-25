from django.urls import path
from .views import ScriptAPIView

urlpatterns = [
    path('<int:pk>/', ScriptAPIView.as_view(), name='video')
]