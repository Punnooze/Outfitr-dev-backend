from pydantic import BaseModel
from typing import List, Optional

class Product(BaseModel):
    brand_name: str
    brand_logo: str
    list_of_products: List[dict]
    category_links: List[dict]
    
