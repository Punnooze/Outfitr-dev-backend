from pydantic import BaseModel, Field
from typing import List, Dict, Optional

class OrderProduct(BaseModel):
    product_link: str
    quantity: int

class Orders(BaseModel):
    user_id: str
    date: Optional[str]
    products: Optional[List[OrderProduct]]