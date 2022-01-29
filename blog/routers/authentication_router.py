from fastapi import APIRouter,Depends,status,HTTPException
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

from typing import List
from sqlalchemy.orm import Session
from blog.hashing import Hash
from blog import database,schemas,models,token_generate

get_db=database.get_db
router=APIRouter(
     prefix="/login",
    tags=["Authentication"],
)



@router.post('/')
def login(request:OAuth2PasswordRequestForm = Depends(),db:Session=Depends(get_db)):
    user=db.query(models.User).filter(models.User.email==request.username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'Invalid Credential')

    if not Hash.verify(user.password,request.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'Invalid Password')


    access_token = token_generate.create_access_token(data={"sub": user.email})
    return {"access_token": access_token, "token_type": "bearer"}