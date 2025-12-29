from pydantic import BaseModel
from typing import Optional

class Product(BaseModel):
    id:int
    name:str
    description:Optional[str] = None
    price:float
    quantity:int

    # def __init__(self,id,name,description,price,quantity):
    #     self.id=id 
    #     self.name=name
    #     self.description=description
    #     self.price=price
    #     self.quantity=quantity