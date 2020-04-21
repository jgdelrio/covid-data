import re
import sys
import logging
from datetime import datetime
from traitlets.config.loader import LazyConfigValue

from covid.config import *


remove = [
    re.compile(r'\nNOTA:[\s\w,]+\n\*[\s][\w:\s]+')
]


def clean_text(text: str):
    for r in remove:
        text = r.sub('', text)
    return text


def in_ipynb(verbose: int=VERBOSE):
    """Detects if we are running within ipython (Notebook)"""
    try:
        cfg = get_ipython().config
        if isinstance(cfg['IPKernelApp']['parent_appname'], LazyConfigValue):
            if verbose > 2:
                print("Notebook detected")
            return True
        else:
            if verbose > 2:
                print("Running in script mode")
            return False
    except NameError:
        return False


def get_logger(name: str="covid-data", to_stdout: bool=False, level=LOG_LEVEL):
    """Creates a logger with the given name"""
    logging.basicConfig(format=LOGGER_FORMAT, datefmt="[%H:%M:%S]")
    logger = logging.getLogger(name)
    logger.setLevel(level)

    # File log
    log_filename = "covid_" + datetime.now().strftime("%Y-%m-%d_%H-%M")
    file_handler = logging.FileHandler(f"{LOG_FOLDER}/{log_filename}.log")
    logfile_formatter = logging.Formatter("%(asctime)s [%(threadName)-12.12s] [%(levelname)-5.5s]  %(message)s")
    file_handler.setFormatter(logfile_formatter)
    logger.addHandler(file_handler)
    # logger.addHandler(logging.StreamHandler(log_file))

    if to_stdout or in_ipynb():
        ch = logging.StreamHandler(sys.stdout)
        ch.setLevel(level)
        logger.addHandler(ch)
    return logger


LOG = get_logger()
