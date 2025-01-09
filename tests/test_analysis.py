import unittest
import pandas as pd
from src.analysis import SurveyAnalysis
from src.config import Config

class TestSurveyAnalysis(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        cls.config = Config()
        cls.analysis = SurveyAnalysis(cls.config)
    
    def test_trend_analysis(self):
        trend_df = self.analysis.analyze_trends()
        self.assertIsInstance(trend_df, pd.DataFrame)
        self.assertTrue('month' in trend_df.columns)
        self.assertTrue('avg_satisfaction' in trend_df.columns)
    
    def test_correlation_analysis(self):
        corr_df = self.analysis.analyze_correlations()
        self.assertIsInstance(corr_df, pd.DataFrame)
        self.assertEqual(corr_df.shape, (3, 3))  # 3x3 相关性矩阵 