from pydantic import BaseModel, Field, validator, root_validator
from typing import List, Optional, Dict, Union
from enum import Enum


class GenderEnum(str, Enum):
    male = "men"
    female = "women"
    unisex = "unisex"

class PriceEnum(str, Enum):
    pc1 = "0-599"
    pc2 = "600-1499"
    pc3 = "1500-2499"
    pc4 = "2500-3499"
    pc5 = "3500-4499"
    pc6 = "4500+"

class AgeEnum(str, Enum):
    ac1 = "18-25"
    ac2 = "26-35"
    ac3 = "36-45"
    ac4 = "46+"

class FitEnum(str, Enum):
    fit1 = "Slim"
    fit2 = "True to Size"
    fit3 = "Oversized"


class MaleMeasurement(BaseModel):
    chest: Optional[int] = None
    waist: Optional[int] = None


class FemaleMeasurement(BaseModel):
    hip: Optional[int] = None
    waist: Optional[int] = None
    bust: Optional[int] = None


class UserDataProfile(BaseModel):
    user_id: str
    gender: GenderEnum
    age_group: AgeEnum
    preferred_brands: List[str] = Field(default_factory=list)
    price_range: PriceEnum
    measurements: Optional[Dict[str, Optional[Union[MaleMeasurement, FemaleMeasurement]]]] = Field(default_factory=dict)
    fit: Optional[FitEnum]
    location: Optional[str] = None
    collaborative_filter: Optional[bool] = None  
    preferred_themes: Optional[List[str]] = None  
    preferred_master_categories: Optional[List[str]] = None  
    preferred_sub_categories: Optional[List[str]] = None  
    brand_blacklist: Optional[List[str]] = None  