from pydantic import BaseModel, Field
from typing import List, Optional, Dict


class Wishlist(BaseModel):
    user_id: str
    items: Optional[List[str]] = []
