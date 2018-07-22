# coding=utf-8
import logging

logger = logging.getLogger(__name__)
logger.setLevel(level = logging.INFO)
# rq = time.strftime('%Y%m%d', time.localtime(time.time()))
handler = logging.FileHandler("stock_basic.log")
handler.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)

def logError(*args):
    logger.error(args)


def logWarning(*arg):
    logger.warning(arg)
