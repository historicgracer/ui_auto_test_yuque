import logging.handlers

import os

class GetLogger:
    logger = None

    @classmethod
    def get_logger(cls):
        # if cls.logger is None:
            cls.logger = logging.getLogger()
            cls.logger.setLevel(logging.INFO)
            fmt = "%(asctime)s %(levelname)s [%(name)s] [%(filename)s (%(funcName)s:%(lineno)d] - %(message)s"
            fm = logging.Formatter(fmt)
            project_path = os.path.dirname(os.path.abspath(__file__)).replace("common","")
            tf = logging.handlers.TimedRotatingFileHandler(filename=project_path + f'/logs/log.log',
                                                           when="H",
                                                           interval=1,
                                                           backupCount=3,
                                                           encoding='utf-8')
            sh = logging.StreamHandler()
            # logging.basicConfig(level=logging.DEBUG,format=fmt)
            tf.setFormatter(fm)
            sh.setFormatter(fm)
            cls.logger.addHandler(tf)
            cls.logger.addHandler(sh)

            return  cls.logger