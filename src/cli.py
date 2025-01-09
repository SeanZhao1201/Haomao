import click
from src.database import SurveyDatabase
from src.analysis import SurveyAnalysis
from src.config import Config
from src.utils import setup_logging
import logging

@click.group()
def cli():
    """用户调研数据分析工具"""
    pass

@cli.command()
def init_db():
    """初始化数据库并生成示例数据"""
    setup_logging()
    config = Config()
    db = SurveyDatabase(config)
    db.create_database()
    logging.info("数据库初始化完成")

@cli.command()
@click.option('--export-format', type=click.Choice(['excel', 'json']), default='excel')
def analyze(export_format):
    """运行数据分析"""
    setup_logging()
    config = Config()
    analysis = SurveyAnalysis(config)
    results = analysis.run_analysis()
    
    if export_format == 'excel':
        analysis.exporter.export_to_excel(results, 'analysis_results.xlsx')
    else:
        analysis.exporter.export_to_json(results, 'analysis_results.json')
    
    logging.info(f"分析完成，结果已导出为{export_format}格式")

if __name__ == '__main__':
    cli() 