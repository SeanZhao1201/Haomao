import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path
from src.exporters import DataExporter

class SurveyAnalysis:
    def __init__(self, config):
        self.config = config
        self.db_path = config.DB_PATH
        self.sql_path = config.SQL_PATH
        self.output_path = config.OUTPUT_PATH
        self.exporter = DataExporter(self.output_path)
        
        plt.rcParams['font.sans-serif'] = ['SimHei']
        plt.rcParams['axes.unicode_minus'] = False
    
    def analyze_trends(self):
        """分析时间趋势"""
        conn = sqlite3.connect(self.db_path)
        trend_query = """
        SELECT 
            strftime('%Y-%m', survey_date) as month,
            AVG(product_satisfaction) as avg_satisfaction,
            COUNT(*) as response_count
        FROM survey_responses
        GROUP BY month
        ORDER BY month
        """
        trend_df = pd.read_sql_query(trend_query, conn)
        conn.close()
        return trend_df
    
    def analyze_correlations(self):
        """分析不同指标之间的相关性"""
        conn = sqlite3.connect(self.db_path)
        correlation_query = """
        SELECT 
            product_satisfaction,
            price_satisfaction,
            would_recommend
        FROM survey_responses
        """
        corr_df = pd.read_sql_query(correlation_query, conn)
        conn.close()
        return corr_df.corr() 