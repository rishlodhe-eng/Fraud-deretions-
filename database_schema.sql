CREATE TABLE users (
    user_id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    password_hash TEXT NOT NULL,
    role VARCHAR(20),
    created_at TIMESTAMP DEFAULT NOW()
);

CREATE TABLE transactions (
    txn_id BIGSERIAL PRIMARY KEY,
    user_id INT REFERENCES users(user_id),
    amount NUMERIC(12,2) NOT NULL,
    merchant_id VARCHAR(50),
    txn_time TIMESTAMP NOT NULL,
    payment_method VARCHAR(50),
    status VARCHAR(20),
    created_at TIMESTAMP DEFAULT NOW()
);

CREATE TABLE fraud_scores (
    score_id BIGSERIAL PRIMARY KEY,
    txn_id BIGINT REFERENCES transactions(txn_id),
    ml_score FLOAT,
    rule_score FLOAT,
    final_score FLOAT,
    risk_level VARCHAR(20),
    flagged BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP DEFAULT NOW()
);

CREATE TABLE fraud_rules (
    rule_id SERIAL PRIMARY KEY,
    rule_name VARCHAR(100),
    condition TEXT,
    threshold FLOAT,
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT NOW()
);

CREATE TABLE audit_logs (
    log_id SERIAL PRIMARY KEY,
    user_id INT REFERENCES users(user_id),
    action TEXT,
    details TEXT,
    created_at TIMESTAMP DEFAULT NOW()
);
