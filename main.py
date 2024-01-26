from fastapi import FastAPI
from pydantic import BaseModel


class Product(BaseModel):
    prodId:int
    prodName:str
    price:float
    stock:int

app = FastAPI()

# @app.get('./')
# async def welcome():
#     print("Welcome Home")
@app.post("/product/")
async def addnew(product:Product):
    pname =product.prodName

    return pname
