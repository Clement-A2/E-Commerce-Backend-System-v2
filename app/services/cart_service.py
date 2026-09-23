from app.schemas.cart import CartCreate, CartResponse
from sqlalchemy.orm import Session
from sqlalchemy import and_
from app.models.cart import Cart
from app.exceptions.cart import (
    CartAlreadyExistsError,
    CartNotFoundError
)
from app.services.user_service import UserService

class CartService:

    def create_cart(self, db: Session, data: CartCreate):

        user_service = UserService()

        user = user_service.get_user(db, data.user_id)

        existing_cart = db.query(Cart).filter(Cart.user_id == data.user_id).first()

        if existing_cart:
            raise CartAlreadyExistsError("User is Already Assigned a Cart...!!")

        cart = Cart(
            user_id = data.user_id
        )

        db.add(cart)
        db.commit()
        db.refresh(cart)

        return cart

    def get_cart(self, db: Session, cart_id: int):

        found_cart = db.query(Cart).get(cart_id)

        if found_cart is None:
            raise CartNotFoundError("Cart Not Found in Records...!!")

        return found_cart

    def update_cart(self, db: Session, cart_id: int, data: CartCreate):

        found_cart = self.get_cart(db,cart_id)

        cart_availability = db.query(Cart).filter(and_(Cart.user_id == data.user_id, Cart.id != cart_id)).first()

        if cart_availability:
            raise CartAlreadyExistsError("Cart Already Assigned to Another User...!!")

        found_cart.user_id = data.user_id

        db.commit()
        db.refresh(found_cart)

        return found_cart

    def delete_cart(self, db: Session, cart_id: int):

        found_cart = self.get_cart(db,cart_id)

        db.delete(found_cart)
        db.commit()

        return "Cart Deleted From Records Successfully...!!"

    def get_all_carts(self, db: Session):

        carts = db.query(Cart).all()

        if not carts:
            raise CartNotFoundError("No Carts Found in Database Records...!!")

        return carts