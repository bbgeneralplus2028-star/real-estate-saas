import stripe
import os

stripe.api_key = os.getenv("STRIPE_SECRET_KEY")

def create_checkout(email: str):
    session = stripe.checkout.Session.create(
        mode="subscription",
        payment_method_types=["card"],
        line_items=[{
            "price": os.getenv("STRIPE_PRICE_ID"),
            "quantity": 1
        }],
        success_url="https://yourapp.com/success",
        cancel_url="https://yourapp.com/cancel",
        customer_email=email
    )
    return session.url
