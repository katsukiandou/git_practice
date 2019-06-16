import logging.config

__config = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'simpleFormatter': {
            'format': '%(asctime)s %(levelname)-8s %(module)-16s %(lineno)4s: %(message)s'
        }
    },
    'handlers': {
        'fileHandler': {
            'level': 'DEBUG',
            'formatter': 'simpleFormatter',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': 'logging.log',
            'maxBytes': 1000000,
            'backupCount': 3,
            'encoding': 'utf-8',
        }
    },
    'loggers': {
        '': {
            'handlers': ['fileHandler'],
            'level': "DEBUG",
        }
    }
}

#logging.config.dictConfig(_config)
#logging.info('hello')
