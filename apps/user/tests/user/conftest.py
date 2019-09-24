import pytest
from rest_auth.app_settings import TokenSerializer, create_token
from rest_auth.models import TokenModel

from utils.factories import UserFactory


@pytest.fixture
def user():
    return UserFactory.create()


@pytest.fixture
def token(user):
    return create_token(TokenModel, user, TokenSerializer)
