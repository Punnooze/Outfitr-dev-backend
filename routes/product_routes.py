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
    with open('routes/final.json') as file:
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

@product_router.get('/women')
async def get_women():
    women_cursor = products_collection.find({"gender": "female"})
    women_list = list(women_cursor) 
    if not women_list:
        return JSONResponse({'message': 'Products not found!'}, status_code=404)
    women = [serialize_product(product) for product in women_list]
    return JSONResponse({'products': women})
        

# @product_router.get('/scanSame')
# async def get_same():
#     same_cursor = products_collection.find({"productName": "Black Wingman Oversized T-Shirt"})
#     same_list = list(same_cursor)
#     if not same_list:
#         return JSONResponse({'message': 'Products not found!'}, status_code=404)
#     same = [serialize_product(product) for product in same_list]
#     return JSONResponse({'products': same})

@product_router.get('/scan')
async def get_scan():
    product_names = ["Black Wingman Oversized T-Shirt", "Lilac Wingman Oversized T-Shirt", "Orange Wingman Oversized T-Shirt", "J.Cole Oversized T-shirt", "Bonkers Playboy Jersey"]
    same_cursor = products_collection.find({"productName": {"$in": product_names}})
    same_list = list(same_cursor)
    if not same_list:
        return JSONResponse({'message': 'Products not found!'}, status_code=404)
    serialized_products = [serialize_product(product) for product in same_list]
    sorted_products = sorted(serialized_products, key=lambda product: product_names.index(product['productName']))
    return JSONResponse({'products': sorted_products})

# [exact product, different colour, different colour, similar, similar]



@product_router.get('/matchSimilar')
async def get_colour():
    product_names = ["Legacy T-shirt // 002", "Within", "life is better when you paint", "Easy T-shirt", "Legacy T-shirt // 001"]
    
    # Fetch all matching products
    same_cursor = products_collection.find({"productName": {"$in": product_names}})
    same_list = list(same_cursor)
    
    if not same_list:
        return JSONResponse({'message': 'Products not found!'}, status_code=404)
    
    # Serialize the products
    serialized_products = [serialize_product(product) for product in same_list]
    
    # Sort the serialized products based on the order in product_names
    sorted_products = sorted(serialized_products, key=lambda product: product_names.index(product['productName']))
    
    return JSONResponse({'products': sorted_products})




@product_router.get('/allBrands')
async def get_all_brands():
    distinct_brands = products_collection.distinct('brand')
    return JSONResponse({'brands': distinct_brands})


# # filter

# {
#     "brands":{
        
#     }
# }