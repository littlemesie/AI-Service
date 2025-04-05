# -*- coding:utf-8 -*-

"""
@date: 2025/4/5 下午8:25
@summary: 自定义日志输出
"""
import os
import logging
from logging.handlers import RotatingFileHandler, TimedRotatingFileHandler

project_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def configure_logging(path=None, log_instance='root'):
    if path:
        log_file = os.path.join(project_dir, 'log/{}.log'.format(path))
    else:
        log_file = os.path.join(project_dir, 'log/root.log')

    # 创建 Logger 实例
    logger = logging.getLogger(log_instance)
    logger.setLevel(logging.INFO)

    # 创建 FileHandler 并设置级别
    file_handler = logging.FileHandler(log_file)
    file_handler.setLevel(logging.INFO)

    # 定义日志格式
    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S'
    )
    file_handler.setFormatter(formatter)

    # 将 Handler 添加到 Logger
    logger.addHandler(file_handler)

    # 按大小分割（最多保留3个备份，每个最大10MB）
    rotating_handler = RotatingFileHandler(
        log_file, maxBytes=10 * 1024 * 1024, backupCount=10
    )
    logger.addHandler(rotating_handler)