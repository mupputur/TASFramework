import logging




logging.basicConfig(format='%(asctime)s::%(filename)s::%(lineno)s::%(funcName)s\
                    ::%(msg)s', level =logging.INFO , filename='home_info.log', filemode='a')

logger = logging.getLogger(__name__)
class Logger():

    def __init__(self,logger =None):
        self.logger = logger or logging.getLogger(__name__)

    def log_info(self, msg):
        self.logger.info(msg)
    def log_error(self, msg):
        self.logger.error(msg)
    def log_warning(self, msg):
        self.logger.warning(msg)

L = Logger()