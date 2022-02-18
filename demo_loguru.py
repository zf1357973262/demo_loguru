#  导包
from loguru import logger



#  日志级别

# debug
# info
# success
# warning
# error


logger.debug("这是一条debug日志")
logger.info("这是一条info日志")
logger.warning("这是一条warning日志")
logger.success("这是一条success日志")

logger.error("这是一条{}日志", "error")
logger.error("这是一条{}日志".format("error"))

logger.info("小明今年{}岁", 12)
logger.info("小明今年{}岁".format(12))

