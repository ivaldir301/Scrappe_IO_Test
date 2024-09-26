import json

class Laptop:
    def __init__(self, price=None, name=None, url=None, description=None, number_of_reviews=None):
        self.price = price
        self.name = name
        self.url = url
        self.description = description
        self.number_of_reviews = number_of_reviews

    def to_dict(self):
        return json.dumps({
            "price": self.price,
            "name": self.name,
            "url": self.url,
            "description": self.description,
            "number_of_reviews": self.number_of_reviews
        })