-- 总体满意度分析
SELECT 
    AVG(product_satisfaction) as avg_product_satisfaction,
    AVG(price_satisfaction) as avg_price_satisfaction,
    AVG(would_recommend) as avg_recommendation
FROM survey_responses;

-- 城市满意度分析
SELECT 
    u.city,
    AVG(sr.product_satisfaction) as avg_satisfaction
FROM users u
JOIN survey_responses sr ON u.user_id = sr.user_id
GROUP BY u.city;

-- 年龄段分析
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
GROUP BY age_group; 