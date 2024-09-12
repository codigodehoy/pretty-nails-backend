from fastapi import FastAPI

from .routes import category

app = FastAPI()
app.include_router(category, prefix="/category")

@app.get("/")
def hello_world():
    return {"message": "Pretty nails version 1.0"}
