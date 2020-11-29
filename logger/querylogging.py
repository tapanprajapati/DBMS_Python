import logging

#Returns the logger object which can be used for general logging
def get_general_logger():
    logger = logging.getLogger("GeneralLogger")
    logger.setLevel(logging.INFO)
    file_handler = logging.FileHandler('general.log')
    file_formatter=logging.Formatter(
        "{'time':'%(asctime)s', 'name': '%(name)s','level': '%(levelname)s', 'message': '%(message)s'}"
    )
    file_handler.setFormatter(file_formatter)
    logger.addHandler(file_handler)
    return logger

#Returns the logger object which can be used for event logging
def get_event_logger():
    logger = logging.getLogger("EventLogger")
    logger.setLevel(logging.INFO)
    file_handler = logging.FileHandler('event.log')
    file_formatter = logging.Formatter(
        "{'time':'%(asctime)s', 'name': '%(name)s','level': '%(levelname)s', 'message': '%(message)s'}"
    )
    file_handler.setFormatter(file_formatter)
    logger.addHandler(file_handler)
    return logger
