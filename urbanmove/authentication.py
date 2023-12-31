from rest_framework import authentication


class BearerAuthentication(authentication.TokenAuthentication):
    keyword = ["token", "bearer"]

    def authenticate(self, request):
        auth = authentication.get_authorization_header(request).split()
        if not auth:
            return None
        if auth[0].lower().decode() not in self.keyword:
            return None

        if len(auth) == 1:
            msg = "Invalid token header. No credentials provided."
            raise authentication.exceptions.AuthenticationFailed(msg)
        elif len(auth) > 2:
            msg = "Invalid token header. Token string should not contain spaces."
            raise authentication.exceptions.AuthenticationFailed(msg)
        try:
            token = auth[1].decode()
        except UnicodeError:
            msg = "Invalid token header. Token string should not contain invalid characters."
            raise authentication.TokenAuthentication.exceptions.AuthenticationFailed(msg)
        return self.authenticate_credentials(token)
