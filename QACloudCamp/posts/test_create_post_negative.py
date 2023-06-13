from baseclasses.response import Response
from requests import codes


def test_can_create_post_negative(create_post_bad, post_generator):
    """
    In that test we try to create post on unresolved place, read status code 404
    """
    object_to_send = post_generator.build()
    Response(create_post_bad(object_to_send)).assert_status_code(codes.not_found)
