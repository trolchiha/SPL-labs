"""
Module to set up logging configuration and create a logger instance.

This module configures the logging system with a specific format and level,
and creates a logger instance for use in other modules.

Attributes:
    logger (logging.Logger): The logger instance configured for the module.

Usage:
    Import this module and use the 'logger' instance to log messages with the configured settings.

"""
import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s]: %(message)s',
    datefmt='%d-%m-%Y %H:%M:%S',
    filename='logs/logs.log', 
    filemode='w'
)

logger = logging.getLogger(__name__)
