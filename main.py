from fastapi import FastAPI

from blog  import database,models
from blog.routers import  blog_router,user_router, authentication_router
app=FastAPI()

models.Base.metadata.create_all(database.engine)


app.include_router(authentication_router.router)
app.include_router(blog_router.router)
app.include_router(user_router.router)

