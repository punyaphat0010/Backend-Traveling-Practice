from fastapi import FastAPI
from .routers import registration_router, auth_router
from .models.models import Base
from .database import engine

app = FastAPI()

# Create tables at startup
Base.metadata.create_all(bind=engine)

app.include_router(registration_router.router, tags=["registration"])
app.include_router(auth_router.router, tags=["auth"])

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str | None = None):
    return {"item_id": item_id, "q": q}