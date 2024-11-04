from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from ninja import Schema, Router
from ninja.security import HttpBearer
from django.conf import settings
import jwt
from datetime import datetime, timedelta
from zoneinfo import ZoneInfo

user_router = Router()


class TokenSchema(Schema):
    token: str


class AuthSchema(Schema):
    username: str
    password: str


# Choose a European time zone. You can replace 'Europe/Berlin' with any other European city if needed.
european_tz = ZoneInfo("Europe/Berlin")


def create_token(user_id: int) -> str:
    current_time = datetime.now(european_tz)
    payload = {
        "user_id": user_id,
        "exp": current_time + timedelta(days=1),
        "iat": current_time,
    }
    return jwt.encode(payload, settings.SECRET_KEY, algorithm="HS256")


@user_router.post("/login", response=TokenSchema)
def login(request, auth: AuthSchema):
    user = authenticate(username=auth.username, password=auth.password)
    if user is not None:
        token = create_token(user.id)
        return {"token": token}
    return {"error": "Invalid credentials"}


class AuthBearer(HttpBearer):
    def authenticate(self, request, token):
        try:
            payload = jwt.decode(token, settings.SECRET_KEY, algorithms=["HS256"])
            user_id = payload.get("user_id")
            if user_id:
                user = User.objects.get(id=user_id)
                return user
        except jwt.ExpiredSignatureError:
            return None
        except (jwt.DecodeError, User.DoesNotExist):
            return None


@user_router.post("/logout", auth=AuthBearer())
def logout(request):
    # In a token-based system, typically the client-side handles logout
    # by removing the token. Here we'll just return a success message.
    return {"message": "Successfully logged out"}


@user_router.get("/me", auth=AuthBearer())
def protected(request):
    return {"id": request.auth.id, "username": request.auth.username}
