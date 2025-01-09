-- 创建用户表
CREATE TABLE IF NOT EXISTS users (
    user_id INTEGER PRIMARY KEY,
    age INTEGER,
    gender TEXT,
    occupation TEXT,
    city TEXT
);

-- 创建调研响应表
CREATE TABLE IF NOT EXISTS survey_responses (
    response_id INTEGER PRIMARY KEY,
    user_id INTEGER,
    survey_date DATE,
    product_satisfaction INTEGER,
    would_recommend INTEGER,
    price_satisfaction INTEGER,
    feedback TEXT,
    FOREIGN KEY (user_id) REFERENCES users(user_id)
); 