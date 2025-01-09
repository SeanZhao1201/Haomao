import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['SimHei']  # 设置中文显示
plt.rcParams['axes.unicode_minus'] = False

def analyze_survey_data():
    conn = sqlite3.connect('user_survey.db')
    
    # 1. 总体满意度分析
    satisfaction_query = '''
    SELECT 
        AVG(product_satisfaction) as avg_product_satisfaction,
        AVG(price_satisfaction) as avg_price_satisfaction,
        AVG(would_recommend) as avg_recommendation
    FROM survey_responses
    '''
    satisfaction_df = pd.read_sql_query(satisfaction_query, conn)
    
    # 2. 按城市分组的满意度分析
    city_satisfaction_query = '''
    SELECT 
        u.city,
        AVG(sr.product_satisfaction) as avg_satisfaction
    FROM users u
    JOIN survey_responses sr ON u.user_id = sr.user_id
    GROUP BY u.city
    '''
    city_satisfaction_df = pd.read_sql_query(city_satisfaction_query, conn)
    
    # 3. 年龄段分析
    age_analysis_query = '''
    SELECT 
        CASE 
            WHEN age < 25 THEN '18-24岁'
            WHEN age BETWEEN 25 AND 34 THEN '25-34岁'
            WHEN age BETWEEN 35 AND 44 THEN '35-44岁'
            ELSE '45岁以上'
        END as age_group,
        AVG(sr.product_satisfaction) as avg_satisfaction,
        COUNT(*) as response_count
    FROM users u
    JOIN survey_responses sr ON u.user_id = sr.user_id
    GROUP BY age_group
    '''
    age_analysis_df = pd.read_sql_query(age_analysis_query, conn)
    
    # 可视化结果
    plt.figure(figsize=(15, 10))
    
    # 城市满意度对比
    plt.subplot(2, 1, 1)
    plt.bar(city_satisfaction_df['city'], city_satisfaction_df['avg_satisfaction'])
    plt.title('各城市用户满意度对比')
    plt.ylabel('平均满意度')
    
    # 年龄段分析
    plt.subplot(2, 1, 2)
    plt.bar(age_analysis_df['age_group'], age_analysis_df['avg_satisfaction'])
    plt.title('不同年龄段用户满意度对比')
    plt.ylabel('平均满意度')
    
    plt.tight_layout()
    plt.savefig('survey_analysis.png')
    
    # 打印基本统计信息
    print("\n=== 调研数据分析结果 ===")
    print("\n1. 总体满意度指标:")
    print(satisfaction_df.round(2))
    
    print("\n2. 各城市满意度:")
    print(city_satisfaction_df.round(2))
    
    print("\n3. 年龄段分析:")
    print(age_analysis_df.round(2))
    
    conn.close()

if __name__ == '__main__':
    analyze_survey_data() 