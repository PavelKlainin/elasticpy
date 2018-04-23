import logging
import logging.config
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'standard': {
            'format': '%(levelname)s:%(name)s: %(message)s '
                    '(%(asctime)s; %(filename)s:%(lineno)d)',
            'datefmt': "%Y-%m-%d %H:%M:%S",
        }
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'formatter': 'standard',
            'class': 'logging.StreamHandler',
        },
        'rotate_file': {
            'level': 'DEBUG',
            'formatter': 'standard',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': 'rotated.log',
            'encoding': 'utf8',
            'maxBytes': 100000,
            'backupCount': 1,
        }
    },
    'loggers': {
        '': {
            'handlers': ['console', 'rotate_file'],
            'level': 'DEBUG',
        },
    }
}
logging.config.dictConfig(LOGGING)
logging.debug("debug message")

# def test():
#     print('test')
#     #pass