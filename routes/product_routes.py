from fastapi import APIRouter
from starlette.responses import JSONResponse
from config.database import products_collection
from models.product_model import Product 
from bson import ObjectId

product_router = APIRouter()

@product_router.get('/allProducts')
async def get_all_products():
    products = products_collection.find()
    return JSONResponse({'products': list(products)})

@product_router.post('/newProduct')
async def new_product(product: Product):
    new_product = dict(product)
    created_product = products_collection.insert_one(new_product)
    if created_product:
        return JSONResponse({'message': 'Product created!'})
    return JSONResponse({'message': 'Product not created!'})

@product_router.get('/getProduct/{id}')
async def get_product(id: str):
    try:
        object_id = ObjectId(id)
    except Exception as e:
        return JSONResponse({'message': 'Invalid product ID'}, status_code=400)
    
    product = products_collection.find_one({'_id': object_id})
    if not product:
        return JSONResponse({'message': 'Product not found!'}, status_code=404)
    return JSONResponse({'product': product})

@product_router.get('/allBrands')
async def get_all_brands():
    distinct_brands = products_collection.distinct('brand')
    return JSONResponse({'brands': distinct_brands})

@product_router.get('/brandProducts/{brand}')
async def get_brand_products(brand: str):
    products = products_collection.find({'brand': brand})
    return JSONResponse({'products': list(products)})

@product_router.get('/masterCategories')
async def get_master_categories():
    distinct_master_categories = products_collection.distinct('master_category')
    return JSONResponse({'master_categories': distinct_master_categories})



