import logging
import inspect
logging.basicConfig(filename='stackTraceLog.log', encoding='utf-8', level=logging.DEBUG)

def a(x):
    logging.info(f"starting function {inspect.stack()[0][3]}")
    #b(x+1)
    print(__name__)
    print(inspect.stack()[0][3])
    logging.info("end of function a")

def b(x):
    logging.info("starting function b")
    c(x+1)
    logging.info("end of function b")

def c(x):
    logging.info("starting function c")
    raise Exception("exception occure")
    

a(19)