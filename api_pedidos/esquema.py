from nturl2path import url2pathname
from pydantic import BaseModel

class Item(BaseModel):
    sku: str
    description: str
    image_url: str 
    reference: str
    quantity: int