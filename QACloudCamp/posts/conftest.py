import pytest
import requests

from configuration import ENDPOINT_POSTS, ENDPOINT_FIRST_POST
from generators.post import Post
from enums.posts_enums import POSTS

@pytest.fixture
def get_posts():
    response = requests.get(ENDPOINT_POSTS)
    return response


@pytest.fixture
def get_post_negative(id=101):
    response = requests.get(ENDPOINT_POSTS + f"{id}")
    return response


def _create_post(data):
    response = requests.post(ENDPOINT_POSTS, data=data)
    return response


@pytest.fixture
def create_post():
    return _create_post


def _create_post_bad(data):
    response = requests.post(ENDPOINT_FIRST_POST, data=data)
    return response


@pytest.fixture
def create_post_bad():
    return _create_post_bad


def _delete_posts(id=POSTS.COUNT_POSTS.value + 1):
    response = requests.delete(ENDPOINT_POSTS + f"{id}")
    return response


@pytest.fixture
def delete_posts():
    return _delete_posts


@pytest.fixture
def post_generator():
    return Post()
