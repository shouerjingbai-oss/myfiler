"""
Global Logger
Author: Your Name
"""
from pathlib import Path
import sys
from loguru import logger
LOG_DIR = Path("logs")
LOG_DIR.mkdir(exist_ok=True)
logger.remove()
# Console
logger.add(
    sys.stdout,
    level="INFO",
    colorize=True,
    enqueue=True,
)
# File
logger.add(
    LOG_DIR / "app.log",
    level="DEBUG",
    rotation="10 MB",
    retention="10 days",
    encoding="utf-8",
    enqueue=True,
)
__all__ = ["logger"]
