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


# @user_router.post('/newQuestionnaire/{id}')
# async def post_questionnaire(id: str, user_data: UserDataProfile):
#     try:
#         object_id = ObjectId(id)
#     except Exception as e:
#         return JSONResponse({'message': 'Invalid user ID'}, status_code=400)
#     print(user_data)
#     form_data = {
#         "user_id": str(object_id),
#         "gender": user_data.gender,
#         "age_group": user_data.age_group,
#         "preferred_brands": user_data.preferred_brands,
#         "price_range": user_data.price_range,
#         "measurements": user_data.measurements,
#         "fit": user_data.fit,
#         "location": user_data.location,
#         "collaborative_filter": True,
#         "preferred_themes": user_data.preferred_themes or [],
#         "preferred_master_categories": user_data.preferred_master_categories or [],
#         "preferred_sub_categories": user_data.preferred_sub_categories or [],
#         "brand_blacklist": user_data.brand_blacklist or []
#     }
#     print('form_data', form_data)
#     try:
#         profile = dataprofile_collection.insert_one(form_data)
        
#         if profile:
#             return JSONResponse({'message': 'Questionnaire submitted!'})
#         # object_id = ObjectId(id)
#     except Exception as e:
#         print(e)
#     return JSONResponse({'message': 'Questionnaire not submitted!'})


@user_router.post('/newQuestionnaire/{id}')
async def post_questionnaire(id: str, user_data: UserDataProfile):
    try:
        object_id = ObjectId(id)
    except Exception as e:
        return JSONResponse({'message': 'Invalid user ID'}, status_code=400)

    # Convert Pydantic model to dictionary
    form_data = user_data.dict()
    form_data["user_id"] = str(object_id)
    form_data["collaborative_filter"] = True
    
    # Handle optional fields
    form_data["preferred_themes"] = form_data.get("preferred_themes", [])
    form_data["preferred_master_categories"] = form_data.get("preferred_master_categories", [])
    form_data["preferred_sub_categories"] = form_data.get("preferred_sub_categories", [])
    form_data["brand_blacklist"] = form_data.get("brand_blacklist", [])

    print('form_data', form_data)
    
    try:
        result = dataprofile_collection.insert_one(form_data)
        
        if result:
            return JSONResponse({'message': 'Questionnaire submitted!'})
    except Exception as e:
        print(e)

    return JSONResponse({'message': 'Questionnaire not submitted!'})


# {
#     "user_id":"string", 
#     "age_group": "18-25", 
#     "fit": "True to Size", 
#     "gender": "men", 
#     "location": "klr", 
#     "measurements": {
#         "men": 
#         {
#             "chest": 40, 
#             "waist": 32
#         },
#         "women": None
#         }, 
#         "preferred_brands": ["Veg Non Veg"], "price_range":"600-1499"
#         }


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


