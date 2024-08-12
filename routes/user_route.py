from fastapi import APIRouter
from starlette.responses import JSONResponse
from config.database import user_collection, dataprofile_collection, address_collection, order_collection, wishlist_collection
from models.user_model import User
from models.user_dataprofile_model import UserDataProfile
from bson import ObjectId

user_router = APIRouter()


@user_router.post("/newUser")
async def new_user(user_details: dict ):
    if user_details:
        exists = user_collection.find_one({'email': user_details['email']})
        if not exists:
            new_user = {
                'name': user_details['name'],
                'email': user_details['email'],
                'userId': user_details['userId']
            }
            created_user = user_collection.insert_one(dict(new_user))
            if created_user:
                blank_address = address_collection.insert_one({'userId': created_user.inserted_id, 'user_addresses': []})
                blank_order = order_collection.insert_one({'userId': created_user.inserted_id, 'orders': []})   
                blank_wishlist = wishlist_collection.insert_one({'userId': created_user.inserted_id, 'wishlist': []})
                return JSONResponse({'message': 'User created'})
            return JSONResponse({'message': 'User not created'})
        return JSONResponse({'message': 'User already exists'})
    return JSONResponse({'message': 'No user details provided'})


@user_router.post('/newQuestionnaire/{id}')
async def post_questionnaire(user_data: UserDataProfile, id: str):
    try:
        object_id = ObjectId(id)
    except Exception as e:
        return JSONResponse({'message': 'Invalid user ID'}, status_code=400)
    user_data.user_id = str(object_id)
    profile = dataprofile_collection.insert_one(user_data.dict())
    if profile:
        return JSONResponse({'message': 'Questionnaire submitted!'})
    return JSONResponse({'message': 'Questionnaire not submitted!'})


@user_router.put('/editQuestionnaire/{id}')
async def edit_questionnaire(new_values: dict, id: str):
    print('new_values', new_values)
    try:
        object_id = ObjectId(id)
    except Exception as e:
        return JSONResponse({'message': 'Invalid user ID'}, status_code=400)
    user_profile = dataprofile_collection.find_one_and_update(
        {'_id': object_id},
        {"$set": new_values}
    )
    if not user_profile:
        return JSONResponse({'message': 'User profile not found!'}, status_code=404)
    return JSONResponse({'message': 'Questionnaire updated!'})

@user_router.put('/editUser/{id}')
async def edit_user(user: User, id: str):
    try:
        object_id = ObjectId(id)
    except Exception as e:
        return JSONResponse({'message': 'Invalid user ID'}, status_code=400)

    existing_user = user_collection.find_one({'_id': object_id})
    if not existing_user:
        return JSONResponse({'message': 'User not found!'}, status_code=404)
    user_data = user.dict(exclude_unset=True)  
    user_collection.find_one_and_update({'_id': object_id}, {"$set": user_data})
    return JSONResponse({'message': 'User updated!'})


