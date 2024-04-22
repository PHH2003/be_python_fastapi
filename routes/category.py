from fastapi import APIRouter
from bson import ObjectId
from models.model import Category
from config.database import collection_category
from schema.category import list_category, category_serial

router_category = APIRouter()

#get 
@router_category.get("/category/")
async def get_category():
    category = list_category(collection_category.find())
    return category

@router_category.get("/category/{id}")
async def get_one_category(id:str):
    category = category_serial(collection_category.find_one({"_id": ObjectId(id)}))
    return category

#post
@router_category.post("/category/add")
async def create_category(category: Category):
    collection_category.insert_one(dict(category))
    
#put
@router_category.put("/category/edit/{id}")
async def edit_category(id:str, category: Category):
    collection_category.find_one_and_update({"_id": ObjectId(id)}, {"$set": dict(category)})

#delete
@router_category.delete("/category/delete/{id}")
async def delete_category(id:str):
    collection_category.find_one_and_delete({"_id": ObjectId(id)})
    