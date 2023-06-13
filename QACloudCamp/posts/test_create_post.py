from baseclasses.response import Response
from schemas.post import Post
from requests import codes
from enums.posts_enums import POSTS

def test_can_create_post(create_post, post_generator):
    """
    In that test we try to create post and validate it, read status code 201
    """
    object_to_send = post_generator.set_id(POSTS.COUNT_POSTS.value + 1).build()
    Response(create_post(object_to_send)).assert_status_code(codes.created).validate(Post)
