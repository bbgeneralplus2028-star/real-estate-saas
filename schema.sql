CREATE TABLE IF NOT EXISTS users (
    id SERIAL PRIMARY KEY,
    email TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL,
    plan TEXT DEFAULT 'free',
    created_at TIMESTAMP DEFAULT NOW()
);

CREATE TABLE IF NOT EXISTS leads (
    id SERIAL PRIMARY KEY,
    user_id INT,
    name TEXT,
    email TEXT,
    phone TEXT,
    message TEXT,
    score INT DEFAULT 0,
    stage TEXT,
    ai_response TEXT,
    created_at TIMESTAMP DEFAULT NOW()
);

CREATE TABLE IF NOT EXISTS properties (
    id SERIAL PRIMARY KEY,
    title TEXT,
    price NUMERIC,
    address TEXT,
    description TEXT,
    image TEXT,
    created_at TIMESTAMP DEFAULT NOW()
);

CREATE TABLE IF NOT EXISTS subscriptions (
    id SERIAL PRIMARY KEY,
    user_id INT,
    stripe_customer_id TEXT,
    status TEXT,
    created_at TIMESTAMP DEFAULT NOW()
);
