import logging

logger = logging.getLogger(__name__ + "_parameter_log")
logger.setLevel(logging.INFO)
logger.addHandler(logging.FileHandler("./decorator.log","a")) 

def logger_decorator(func):
    def wrapper(*args, **kwargs):   
        name = func.__name__
        logger.log(logging.INFO, f"function: {name}")
        logger.log(logging.INFO, f"positional parameters: {args if args else 'none'}")
        logger.log(logging.INFO, f"keyword parameters: {kwargs if kwargs else 'none'}")

        value = func(*args, **kwargs)
        logger.log(logging.INFO, f"return: {value}")   
        return value
    return wrapper

@logger_decorator
def greet():
    print("Hello, World")


@logger_decorator
def pos(*args):
    return True

@logger_decorator
def no_pos(**kwargs):
    return logger_decorator

greet()
pos(False)
no_pos(True)
    






