from django.http import HttpResponse
# from myauth.models import APIKey
import base64
import binascii
from django.contrib.auth import authenticate, get_user_model
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.authentication import BaseAuthentication
from rest_framework import HTTP_HEADER_ENCODING, exceptions

def get_authorization_header(request):
    """
    Return request's 'Authorization:' header, as a bytestring.

    Hide some test client ickyness where the header can be unicode.
    """
    auth = request.META.get('HTTP_AUTHORIZATION', b'')
    if isinstance(auth, str):
        # Work around django test client oddness
        auth = auth.encode(HTTP_HEADER_ENCODING)
    return auth

class CustomAPIKeyAuthentication(BaseAuthentication):
    keyword = 'Api-Key'  # The header key for sending the API key

    def authenticate(self, request):
        api_key = request.META.get('HTTP_API_KEY')
        secret_key = request.META.get('HTTP_SECRET_KEY')

        
        auth = get_authorization_header(request).split()

        # print(auth)

        if not auth or auth[0].lower() != b'basic':
            return None

        if len(auth) == 1:
            msg = 'Invalid basic header. No credentials provided.'
            raise exceptions.AuthenticationFailed(msg)
        elif len(auth) > 2:
            msg = 'Invalid basic header. Credentials string should not contain spaces.'
            raise exceptions.AuthenticationFailed(msg)

        try:
            try:
                auth_decoded = base64.b64decode(auth[1]).decode('utf-8')
            except UnicodeDecodeError:
                auth_decoded = base64.b64decode(auth[1]).decode('latin-1')

            userid, password = auth_decoded.split(':', 1)
        except (TypeError, ValueError, UnicodeDecodeError, binascii.Error):
            msg = 'Invalid basic header. Credentials not correctly base64 encoded.'
            raise exceptions.AuthenticationFailed(msg)

        credentials = {
            get_user_model().USERNAME_FIELD: userid,
            'password': password
        
        }



        user = authenticate(request=request, **credentials)

        # print(user)

        if not api_key or not secret_key:
            return None
         
        # try:
        #     apikey = APIKey.objects.get(api_key=api_key, secret_key=secret_key)
        # except APIKey.DoesNotExist:
        #     raise AuthenticationFailed('No such API key or secret key')
        
        if not user or not user.is_active:
            return None

        self.enforce_csrf(request)

        # CSRF passed with authenticated user
        return (user, None)

        
        # return Response({
        #     'api_key': apikey.user.apikey.api_key,
        #     'secret_key': apikey.user.apikey.secret_key,
        #     'user_id': apikey.user.pk,
        #     'email': apikey.user.email
        # })
        