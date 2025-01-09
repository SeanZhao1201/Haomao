from dataclasses import dataclass
from typing import List, Dict
import pandas as pd

@dataclass
class DataValidator:
    """数据验证类"""
    
    @staticmethod
    def validate_survey_data(df: pd.DataFrame) -> Dict[str, List[str]]:
        """验证调研数据的有效性"""
        errors = {
            'missing_values': [],
            'invalid_ranges': [],
            'inconsistent_data': []
        }
        
        # 检查缺失值
        for col in df.columns:
            if df[col].isnull().any():
                errors['missing_values'].append(f"列 {col} 存在缺失值")
        
        # 检查数值范围
        if 'product_satisfaction' in df.columns:
            invalid_satisfaction = df[
                ~df['product_satisfaction'].between(1, 5)
            ]['product_satisfaction']
            if not invalid_satisfaction.empty:
                errors['invalid_ranges'].append(
                    f"产品满意度存在无效值: {invalid_satisfaction.values}"
                )
        
        return errors 