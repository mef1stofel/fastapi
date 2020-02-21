from fastapi import FastAPI

from .api import users, items
from . import models
from .database import engine


app = FastAPI()
app.include_router(users.router)
app.include_router(items.router)


@app.on_event("startup")
def startup_event():
    models.Base.metadata.create_all(bind=engine)
