from enums.posts_enums import POSTS

class Response:
    def __init__(self, response):
        self.response = response
        self.response_json = response.json()
        self.response_status = response.status_code

    def validate(self, schema):
        if isinstance(self.response_json, list):
            for item in self.response_json:
                schema.parse_obj(item)
        else:
            schema.parse_obj(self.response_json)
        return self

    def count_posts(self):
        assert len(self.response_json) == POSTS.COUNT_POSTS.value, self
        return self

    def assert_status_code(self, status_code):
        if isinstance(status_code, list):
            assert self.response_status in status_code, self
        else:
            assert self.response_status == status_code, self
        return self

    def __str__(self):
        return f"\nStatis code: {self.response_status}" \
               f"\nRequested url: {self.response.url}" \
               f"\nResponse body: {self.response_json}"

