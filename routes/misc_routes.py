from fastapi import APIRouter
from starlette.responses import JSONResponse
from config.database import address_collection, order_collection, wishlist_collection
from models.user_model import User
from models.user_dataprofile_model import UserDataProfile
from bson import ObjectId

misc_router = APIRouter()

@misc_router.put('/editAddress/{id}')
async def edit_address(new_address: dict, id: str):
    try:
        object_id = ObjectId(id)
    except Exception as e:
        return JSONResponse({'message': 'Invalid user ID'}, status_code=400)
    address =  address_collection.find_one({'userId': object_id})
    if not address:
        return JSONResponse({'message': 'Address not found!'}, status_code=404)
    
    updated_address = address.get('user_addresses')
    if updated_address == None:
        updated_address = new_address
    else:
        updated_address=[updated_address, new_address]
    
    new_addrs = address_collection.find_one_and_update(
        {'_id': address.get('_id')},
        {"$set": {'user_addresses': updated_address}},
        return_document=True
    )
    if not new_addrs:
        return JSONResponse({'message': 'Address could not be edited'}, status_code=404)
    return JSONResponse({'message': 'Address updated!'})
