from pydantic import BaseModel, Field
from typing import List, Optional, Dict

class Wishlist(BaseModel):
    user_id: str
    line1: Optional[str] = None
    line2: Optional[str] = None
    city: Optional[str] = None
    state: Optional[str] = None
    pin_code: Optional[str] = None
    phone= Optional[str] = None
