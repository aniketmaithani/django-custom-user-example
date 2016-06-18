#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest


pytestmark = pytest.mark.django_db


def test_urls(client):
	url = '/admin'
	response = client.get(url, follow=True)
	assert response.status_code == 200	