from pathlib import Path
from dataclasses import dataclass

@dataclass
class Config:
    # 数据库配置
    DB_NAME: str = 'user_survey.db'
    DB_PATH: Path = Path('data') / DB_NAME
    SQL_PATH: Path = Path('data/sql')
    
    # 数据生成配置
    USER_COUNT: int = 1000
    RESPONSE_COUNT: int = 1500
    RANDOM_SEED: int = 42
    
    # 分析配置
    OUTPUT_PATH: Path = Path('data/output')
    FIGURE_SIZE: tuple = (15, 10)
    
    # 数据选项
    CITIES: list = ['北京', '上海', '广州', '深圳', '杭州']
    OCCUPATIONS: list = ['学生', '上班族', '自由职业者', '企业主']
    FEEDBACK_OPTIONS: list = ['产品很好用', '价格偏高', '体验一般', '需要改进', '非常满意']
    
    @classmethod
    def create_directories(cls):
        """创建必要的目录结构"""
        for path in [cls.DB_PATH.parent, cls.OUTPUT_PATH]:
            path.mkdir(parents=True, exist_ok=True) 