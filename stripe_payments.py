import stripe
import os

stripe.api_key = os.getenv("STRIPE_SECRET_KEY")

def create_checkout_session(user_id):
    session = stripe.checkout.Session.create(
        payment_method_types=["card"],
        line_items=[{
            "price_data": {
                "currency": "usd",
                "product_data": {"name": "Real Estate AI SaaS"},
                "unit_amount": 2900,
            },
            "quantity": 1,
        }],
        mode="subscription",
        success_url="https://your-app.onrender.com/dashboard.html",
        cancel_url="https://your-app.onrender.com",
    )

    return session.url
