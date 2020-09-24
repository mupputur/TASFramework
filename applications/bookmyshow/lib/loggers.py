import logging




logging.basicConfig(format='%(asctime)s::%(filename)s::%(lineno)s::%(funcName)s\
                    ::%(msg)s', level =logging.INFO , filename='home_info.log', filemode='a')

logger = logging.getLogger(__name__)
class Logger:
    """
    def __init__(self,logger =None):
        self.logger = logger or logging.getLogger(__name__)
    """
    @classmethod
    def log_info(self, msg):
        logger.info(msg)

    @classmethod
    def log_error(self, msg):
        logger.error(msg)

    @classmethod
    def log_warning(self, msg):
        logger.warning(msg)
