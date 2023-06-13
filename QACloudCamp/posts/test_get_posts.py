from baseclasses.response import Response
from schemas.post import Post
from requests import codes


def test_can_get_posts(get_posts):
    """
    In that test we try to get posts and validate it, read status code 200, count posts = 100
    """
    Response(get_posts).assert_status_code(codes.ok).validate(Post).count_posts()
