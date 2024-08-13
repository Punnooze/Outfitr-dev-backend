from fastapi import APIRouter
from starlette.responses import JSONResponse
from config.database import products_collection
from models.product_model import Product 
from bson import ObjectId
import json

product_router = APIRouter()

@product_router.get('/search')
async def search_products():
    try:
        products_cursor = products_collection.find({'sub_category': 'Oversized T-shirt'})
        products_list = [serialize_product(product) for product in products_cursor]
        if not products_list:
            return JSONResponse({'message': 'No products found!'}, status_code=404)
        return JSONResponse({'products': products_list}, status_code=200)
    except Exception as e:
        return JSONResponse({'message': str(e)}, status_code=500)

@product_router.get('/feed')
async def get_all_products():
    try:
        projection = {
            'productName': 1,
            'price': 1,         
            'cover_image': 1,      
            'brand': 1,            
            'fit': 1,               
            'sub_category': 1        
        }
        products_cursor = products_collection.find({}, projection)
        products_list = [serialize_product(product) for product in products_cursor]
        if not products_list:
            return JSONResponse({'message': 'No products found!'}, status_code=404)
        return JSONResponse({'products': products_list}, status_code=200)
    except Exception as e:
        return JSONResponse({'message': str(e)}, status_code=500)

def serialize_product(product):
    product['_id'] = str(product['_id'])
    return product


@product_router.post('/uploadProduct')
async def new_product():
    with open('routes/men_oversized_tshirt_details.json') as file:
        products = json.load(file)
    result = products_collection.insert_many(products)
    print(f'{len(result.inserted_ids)} products were inserted.')

@product_router.get('/getProduct/{id}')
async def get_product(id: str):
    try:
        object_id = ObjectId(id)
    except Exception as e:
        return JSONResponse({'message': 'Invalid product ID'}, status_code=400)
    product = products_collection.find_one({'_id': object_id})
    if not product:
        return JSONResponse({'message': 'Product not found!'}, status_code=404)
    product = serialize_product(product)
    return JSONResponse({'product': product})

@product_router.get('/allBrands')
async def get_all_brands():
    distinct_brands = products_collection.distinct('brand')
    return JSONResponse({'brands': distinct_brands})


