from pydantic import BaseModel, Field
from typing import List, Optional, Dict

class UserDataProfile(BaseModel):
    user_id: str
    gender: str = None 
    age_group: str = None 
    location: str = None
    preferred_brands: List[str] = Field(default_factory=list)
    budget_range: str = None 
    preferred_sizes: Dict[str, int] = Field(default_factory=dict)  
    style_preferences: Optional[str] = None 
    collaborative_filter: Optional[bool] = False
    preferred_fits: str=None
    preferred_themes: List[str] = Field(default_factory=list)
    preferred_master_categories: List[str] = Field(default_factory=list)
    preferred_sub_categories: List[str] = Field(default_factory=list)
    brand_blacklist: Optional[List[str]] = Field(default_factory=list)  