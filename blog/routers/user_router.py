from fastapi import APIRouter,Depends,status,HTTPException
from typing import List
from sqlalchemy.orm import Session
from blog.repository import user_repository

from blog import database,schemas,models
router=APIRouter(
     prefix="/user",
    tags=["Users"],
)

get_db=database.get_db
from blog.hashing import Hash


@router.post('/',status_code=status.HTTP_201_CREATED,response_model=schemas.ShowUser)
def create_user(request:schemas.User,db:Session=Depends(get_db)):
    return user_repository.create(request,db)
    



@router.get('/{id}',status_code=200,response_model=schemas.ShowUser)
def get_user(id:int,db:Session=Depends(get_db)):
    return user_repository.get(id,db)
