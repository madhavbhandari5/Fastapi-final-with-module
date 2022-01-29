from sqlalchemy.orm import Session
from blog import schemas,models
from fastapi import APIRouter,Depends,status,HTTPException

def get_all(db:Session):
    blogs=db.query(models.Blog).all()
    return blogs

def create(blog:schemas.Blog,db:Session):
    new_blog=models.Blog(title=blog.title,body=blog.body,user_id=2)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog


def destroy(id:int,db:Session):
    blog=db.query(models.Blog).filter(models.Blog.id==id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'Blog with id {id} is not available')
    blog.delete(synchronize_session=False)
    db.commit()
    return 'Done'



def update(id:int,blog:schemas.Blog,db:Session):
    up_blog=db.query(models.Blog).filter(models.Blog.id==id)
    if not up_blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with id {id} is not available")
    up_blog.update(blog.dict())
    db.commit()
    return 'Updated Successfully'



def show(id:int, db:Session):
    blog=db.query(models.Blog).filter(models.Blog.id==id).first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with the id {id} is not available")
    return blog