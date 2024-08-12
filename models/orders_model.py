from pydantic import BaseModel, Field
from typing import List, Dict, Optional

class OrderProduct(BaseModel):
    product_link: str
    quantity: int

class AllOrders(BaseModel):
    date: Optional[str]
    products: Optional[List[OrderProduct]]


class Orders(BaseModel):
    user_id: str
    orders: Optional[List[AllOrders]] = []
