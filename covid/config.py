import pathlib
from os import getenv
from logging import INFO


# Logging settings
LOG_LEVEL = INFO
LOGGER_FORMAT = "%(asctime)s %(message)s"

# Path refs
ROOT = pathlib.Path(__file__).parents[1]
DATA_FOLDER = ROOT.joinpath("data")
LOG_FOLDER = ROOT.joinpath("log")

# Crawler
QUERY_RETRY_LIMIT = 3
SEMAPHORE_LIMIT = 10
SEMAPHORE_WAIT = 5
HEADERS = {
    'user-agent': ('Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) '
                   'AppleWebKit/537.36 (KHTML, like Gecko) '
                   'Chrome/45.0.2454.101 Safari/537.36'),
}

VERBOSE = int(getenv("VERBOSE", "2"))
