from baseclasses.response import Response
from requests import codes


def test_can_get_post_negative(get_post_negative):
    """
    In that test we try to get non-existent post and read status code 404
    """
    Response(get_post_negative).assert_status_code(codes.not_found)
    