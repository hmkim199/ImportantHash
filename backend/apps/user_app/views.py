# Create your views here.

from .serializers import RegistrationSerializer
from rest_framework.permissions import IsAuthenticated

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.token_blacklist.models import OutstandingToken, BlacklistedToken

class LogoutView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        if self.request.data.get('all'):
            token: OutstandingToken
            for token in OutstandingToken.objects.filter(user=request.user):
                _, _ = BlacklistedToken.objects.get_or_create(token=token)
            return Response({"status": "OK, goodbye, all refresh tokens blacklisted"})
        refresh_token = self.request.data.get('refresh_token')
        token = RefreshToken(token=refresh_token)
        token.blacklist()
        return Response({"status": "OK, goodbye"})

class RegisterView(APIView):

    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            serializer = RegistrationSerializer(data=request.data)
        
            data = {}
        
            if serializer.is_valid():
                account = serializer.save()
                
                data['response'] = "Registration Successful!"
                data['username'] = account.username
                data['email'] = account.email

                # token = Token.objects.get(user=account).key
                # data['token'] = token

                # refresh = RefreshToken.for_user(account)
                # data['token'] = {
                #                     'refresh': str(refresh),
                #                     'access': str(refresh.access_token),
                #                 }
        
            else:
                data = serializer.errors
        
            return Response(data, status=status.HTTP_201_CREATED)