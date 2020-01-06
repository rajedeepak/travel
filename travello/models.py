from django.db import models

# Create your models here.
class Destination:
    id : int
    name : str
    img : str
    desc : str
    price : int

    def __init__(self, id=None,name=None,img=None,desc=None,price=None):
        super().__init__()
        self.id = id
        self.name = name
        self.img = img
        self.desc = desc
        self.price = price

