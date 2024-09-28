import json
import ast

LAPTOP_DICT = {
    "price": "",
    "name": "",
    "url": "",
    "description": "",
    "number_of_reviews": ""
}

class Laptop:
    def __init__(self, price=None, name=None, url=None, description=None, number_of_reviews=None):
        self.price = price
        self.name = name
        self.url = url
        self.description = description
        self.number_of_reviews = number_of_reviews

    def to_dict(self):
        LAPTOP_DICT = {
            "price": str(self.price),
            "name": str(self.name),
            "url": str(self.url),
            "description": str(self.description),
            "number_of_reviews": str(self.number_of_reviews)
        }
        
        return LAPTOP_DICT