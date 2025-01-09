import pandas as pd
from pathlib import Path
from typing import Dict
import json
import yaml

class DataExporter:
    """数据导出类"""
    
    def __init__(self, output_path: Path):
        self.output_path = output_path
        self.output_path.mkdir(parents=True, exist_ok=True)
    
    def export_to_excel(self, results: Dict[str, pd.DataFrame], filename: str):
        """导出结果到Excel文件"""
        with pd.ExcelWriter(self.output_path / filename) as writer:
            for sheet_name, df in results.items():
                df.to_excel(writer, sheet_name=sheet_name, index=False)
    
    def export_to_json(self, results: Dict[str, pd.DataFrame], filename: str):
        """导出结果到JSON文件"""
        json_results = {
            name: df.to_dict(orient='records')
            for name, df in results.items()
        }
        with open(self.output_path / filename, 'w', encoding='utf-8') as f:
            json.dump(json_results, f, ensure_ascii=False, indent=2) 