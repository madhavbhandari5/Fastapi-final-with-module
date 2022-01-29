from fastapi import APIRouter,Depends,status,HTTPException
from typing import List
from sqlalchemy.orm import Session
from blog.repository import blog_repository
from blog import database,schemas,models,oauth2

router=APIRouter(
     prefix="/blog",
    tags=["Blogs"],
)
get_db=database.get_db


@router.get('/',response_model=List[schemas.ShowBlog])
def show_all(db:Session=Depends(get_db),current_user:schemas.User=Depends(oauth2.get_current_user)):
    return blog_repository.get_all(db)



@router.post('/',status_code=status.HTTP_201_CREATED)
def create_post(blog: schemas.Blog,db:Session=Depends(get_db),current_user:schemas.User=Depends(oauth2.get_current_user)):
    return blog_repository.create(blog,db)



@router.get('/{id}',status_code=200,response_model=schemas.ShowBlog)
def show(id:int,db:Session=Depends(get_db),current_user:schemas.User=Depends(oauth2.get_current_user)):
    return blog_repository.show(id,db)




@router.delete('/{id}',status_code=status.HTTP_204_NO_CONTENT)
def destroy(id:int,db:Session=Depends(get_db),current_user:schemas.User=Depends(oauth2.get_current_user)):
    return blog_repository.destroy(id,db)
    



@router.put('/{id}',status_code=status.HTTP_202_ACCEPTED)
def update(id:int,blog:schemas.Blog,db:Session=Depends(get_db),current_user:schemas.User=Depends(oauth2.get_current_user)):
    return blog_repository.update(id,blog,db)

