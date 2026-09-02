from fastapi import FastAPI
from app.database.database import Base, engine
from app.models.user import User
from app.models.product import Product
from app.models.cart import Cart
from app.models.cart_item import CartItem
from app.models.order import Order
from app.models.order_item import OrderItem
from app.models.category import Category
from app.models.payment import Payment

Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.get("/")

def first_run():
    return {"message" : "E-Commerce Backend is running!"}