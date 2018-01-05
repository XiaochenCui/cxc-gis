import json


class JsonMixin():
    @property
    def json(self):
        return json.dumps(self.serializable_representation)
