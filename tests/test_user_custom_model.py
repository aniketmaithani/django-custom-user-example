#!/usr/bin/env python
# -*- coding: utf-8 -*-

from .factories import UserFactory
from customuser.accounts.models import CustomUser
import pytest


pytestmark = pytest.mark.django_db


def test_user_custom_model():
    user = UserFactory.create(username="sampleuser")
    assert user.username == "sampleuser"
    assert user.is_staff is False
    assert user.is_superuser is False

# You Can Add More Test Case w.r.t to your custom model


def test_custom_model_required_fields():
    user = CustomUser(username="user", full_name="john doe", short_name="jd", email="jd@jd.com")
    assert user.username == "user"
    assert user.full_name == "john doe"
    assert user.short_name == "jd"
    assert user.email == "jd@jd.com"
    assert user.is_staff is False
    assert user.is_active is True
    assert str(user) == "user"
    assert user.get_full_name() == "john doe"
    assert user.get_absolute_url() == "/users/user/"
    assert user.get_short_name() == "jd"
    # assert user.is_valid() is False
