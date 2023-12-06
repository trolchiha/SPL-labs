import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s]: %(message)s',
    datefmt='%d-%m-%Y %H:%M:%S',
    filename='logs.log', 
    filemode='w'
)

logger = logging.getLogger(__name__)
