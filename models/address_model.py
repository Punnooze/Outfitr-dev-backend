from pydantic import BaseModel, Field
from typing import List, Optional, Dict

class AddressObject(BaseModel):
    line1: str = None
    line2: str = None
    city: str = None
    state: str = None
    pin_code: str = None
    phone: str = None

class Address(BaseModel):
    user_id: str
    user_addresses: Optional[List[AddressObject]] = []
   
