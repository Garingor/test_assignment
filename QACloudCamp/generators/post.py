import random
from faker import Faker

fake = Faker()


class Post:

    def __init__(self):
        self.result = {}
        self.reset()

    def set_userid(self, userid=random.randrange(1, 10000)):
        self.result['userId'] = userid
        return self

    def set_id(self, id=random.randrange(1, 10000)):
        self.result['id'] = id
        return self

    def set_title(self, title=fake.sentence(nb_words=5, variable_nb_words=True)):
        self.result['title'] = title
        return self

    def set_body(self, body=fake.sentence(nb_words=150, variable_nb_words=True)):
        self.result['body'] = body
        return self

    def reset(self):
        self.set_userid()
        self.set_id()
        self.set_title()
        self.set_body()
        return self

    def build(self):
        return self.result