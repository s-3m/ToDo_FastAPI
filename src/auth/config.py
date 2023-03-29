from fastapi_users.authentication import CookieTransport, AuthenticationBackend as fastapi_auth_backend
from fastapi_users.authentication import JWTStrategy
import base64
import binascii
from starlette.authentication import AuthCredentials, AuthenticationBackend, AuthenticationError, SimpleUser

from settings import AUTH_TOKEN_SECRET

cookie_transport = CookieTransport(cookie_max_age=3600)


def get_jwt_strategy() -> JWTStrategy:
    return JWTStrategy(secret=AUTH_TOKEN_SECRET, lifetime_seconds=3600)


auth_backend = fastapi_auth_backend(name="jwt", transport=cookie_transport, get_strategy=get_jwt_strategy)


class BasicAuthBackend(AuthenticationBackend):
    async def authenticate(self, conn):
        if "Authorization" not in conn.headers:
            return

        auth = conn.headers["Authorization"]
        try:
            scheme, credentials = auth.split()
            if scheme.lower() != 'basic':
                return
            decoded = base64.b64decode(credentials).decode("ascii")
        except (ValueError, UnicodeDecodeError, binascii.Error) as exc:
            raise AuthenticationError('Invalid basic auth credentials')

        username, _, password = decoded.partition(":")
        # TODO: You'd want to verify the username and password here.
        return AuthCredentials(["authenticated"]), SimpleUser(username)
