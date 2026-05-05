CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    email TEXT UNIQUE NOT NULL,
    password_hash TEXT NOT NULL,
    is_premium BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP DEFAULT NOW()
);

CREATE TABLE properties (
    id SERIAL PRIMARY KEY,
    title TEXT,
    price NUMERIC,
    location TEXT,
    description TEXT,
    created_at TIMESTAMP DEFAULT NOW()
);

CREATE TABLE subscriptions (
    id SERIAL PRIMARY KEY,
    user_id INT REFERENCES users(id),
    stripe_customer_id TEXT,
    stripe_subscription_id TEXT,
    status TEXT,
    created_at TIMESTAMP DEFAULT NOW()
);
