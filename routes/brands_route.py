from fastapi import APIRouter, HTTPException
from fastapi.templating import Jinja2Templates
from starlette.requests import Request
from starlette.responses import JSONResponse
from config.database import brand_collection
from models.product_model import Product 
from bson import ObjectId

brand_router = APIRouter()
