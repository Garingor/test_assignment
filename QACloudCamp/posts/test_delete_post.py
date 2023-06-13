from baseclasses.response import Response
from requests import codes

def test_can_delete_posts(delete_posts):
    """
    In that test we try to delete post and read status code 200
    """
    Response(delete_posts()).assert_status_code(codes.ok)
