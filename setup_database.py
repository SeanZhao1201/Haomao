import sqlite3
import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# 创建数据库连接
def create_database():
    conn = sqlite3.connect('user_survey.db')
    cursor = conn.cursor()
    
    # 创建用户表
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        user_id INTEGER PRIMARY KEY,
        age INTEGER,
        gender TEXT,
        occupation TEXT,
        city TEXT
    )
    ''')
    
    # 创建调研响应表
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS survey_responses (
        response_id INTEGER PRIMARY KEY,
        user_id INTEGER,
        survey_date DATE,
        product_satisfaction INTEGER,
        would_recommend INTEGER,
        price_satisfaction INTEGER,
        feedback TEXT,
        FOREIGN KEY (user_id) REFERENCES users(user_id)
    )
    ''')
    
    # 生成模拟数据
    np.random.seed(42)
    
    # 生成用户数据
    users_data = []
    for i in range(1000):
        users_data.append((
            i,
            np.random.randint(18, 65),
            np.random.choice(['男', '女']),
            np.random.choice(['学生', '上班族', '自由职业者', '企业主']),
            np.random.choice(['北京', '上海', '广州', '深圳', '杭州'])
        ))
    
    cursor.executemany('INSERT INTO users VALUES (?,?,?,?,?)', users_data)
    
    # 生成调研响应数据
    responses_data = []
    start_date = datetime(2023, 1, 1)
    
    for i in range(1500):
        responses_data.append((
            i,
            np.random.randint(0, 1000),
            (start_date + timedelta(days=np.random.randint(0, 365))).strftime('%Y-%m-%d'),
            np.random.randint(1, 6),
            np.random.randint(0, 11),
            np.random.randint(1, 6),
            np.random.choice(['产品很好用', '价格偏高', '体验一般', '需要改进', '非常满意'])
        ))
    
    cursor.executemany('INSERT INTO survey_responses VALUES (?,?,?,?,?,?,?)', responses_data)
    
    conn.commit()
    conn.close()

if __name__ == '__main__':
    create_database() 