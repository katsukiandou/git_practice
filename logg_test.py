import logging
from configDict import __config
#logging.basicConfig(filename='example.log',level=logging.INFO, format='%(asctime)s,%(levelname)s,%(message)s')

#configDictの名前空間に存在する__configを呼び出してloggerを設定する。

logging.config.dictConfig(__config)

a = 1213
logging.debug('This message should go to the log file')
logging.info('So should this %s' % a)
logging.warning('And this, too')
