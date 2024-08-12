from pydantic import BaseModel
from typing import List, Optional

class Product(BaseModel):
    seller: str
    brand: str
    product_id: str
    product_url: str
    cover_image: str
    images: List[str]
    product_name: str
    sizes_available: Optional[List[str]]
    price: float
    primary_colour: Optional[str]
    secondary_colour: Optional[str] = None
    material: Optional[str] = None
    style: Optional[str] = None  
    occasion: Optional[str] = None
    season: Optional[str] = None
    theme: Optional[str] = None
    gender: Optional[str] = str
    pattern: Optional[str] = None
    master_category: str
    sub_category: Optional[str]
    LLM_desc: Optional[str] = None
    others: Optional[str] = None
