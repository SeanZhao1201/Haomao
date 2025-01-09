import logging
from pathlib import Path

def setup_logging():
    """设置日志配置"""
    log_path = Path('data/logs')
    log_path.mkdir(parents=True, exist_ok=True)
    
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler(log_path / 'survey_analysis.log'),
            logging.StreamHandler()
        ]
    ) 