import logging
import logging.config



def config_root_logger(log_file):

    
    formatter = "%(asctime)-15s" \
                "| %(levelname)-5s" \
                "| %(message)s"

    logging.config.dictConfig({
        'version': 1,
        'formatters': {
            'root_formatter': {
                'format': formatter
            }
        },
        'handlers': {
            'log_file': {
                'class': 'logging.FileHandler',
                'level': 'DEBUG',
                'filename': log_file,
                'formatter': 'root_formatter',
            }
        },
        'loggers': {
            '': {
                'handlers': [
                    'log_file',
                ],
                'level': 'DEBUG',
                'propagate': True
            }
        }
    })