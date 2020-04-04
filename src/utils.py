import re
import sys
import logging
from datetime import datetime
import numpy as np
import matplotlib.pyplot as plt
from traitlets.config.loader import LazyConfigValue

from src.config import *


remove = [
    re.compile(r'\nNOTA:[\s\w,]+\n\*[\s][\w:\s]+')
]


def clean_text(text):
    for r in remove:
        text = r.sub('', text)
    return text


def in_ipynb(verbose=VERBOSE):
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


def get_logger(name="covid-data", to_stdout=False, level=LOG_LEVEL):
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


def plot_stacked_bar(data, series_labels, category_labels=None, orientation='horizontal', show_values=False,
                     value_format="{}", y_label=None, x_label=None, colors=None, grid=True, plotsize=None,
                     title=None, reverse=False, rotation="horizontal"):
    """Plots a stacked bar chart with the data and labels provided.

    Keyword arguments:
    data            -- 2-dimensional numpy array or nested list
                       containing data for each series in rows
    series_labels   -- list of series labels (these appear in
                       the legend)
    category_labels -- list of category labels (these appear
                       on the x-axis)
    show_values     -- If True then numeric value labels will
                       be shown on each bar
    value_format    -- Format string for numeric value labels
                       (default is "{}")
    y_label         -- Label for y-axis (str)
    colors          -- List of color labels
    grid            -- If True display grid
    reverse         -- If True reverse the order that the
                       series are displayed (left-to-right
                       or right-to-left)
    """

    ny = len(data[0])
    ind = list(range(ny))

    axes = []
    cum_size = np.zeros(ny)

    data = np.array(data)
    if plotsize:
        plt.figure(figsize=plotsize)

    if orientation == 'horizontal':
        pltfunc = plt.barh
    elif orientation == 'vertical':
        pltfunc = plt.bar

    if reverse:
        data = np.flip(data, axis=1)
        category_labels = reversed(category_labels)

    for i, row_data in enumerate(data):
        if orientation == 'vertical':
            axes.append(plt.bar(ind, row_data, bottom=cum_size, label=series_labels[i], color=colors[i]))
        else:
            axes.append(plt.barh(ind, row_data, left=cum_size, height=0.7, label=series_labels[i], color=colors[i]))
        cum_size += row_data

    if category_labels:
        if orientation == 'vertical':
            plt.xticks(ind, category_labels, rotation=rotation)
        else:
            plt.yticks(ind, category_labels, fontsize=8)

    if x_label:
        plt.xlabel(x_label)

    if y_label:
        plt.ylabel(y_label)

    if title:
        plt.title(title, fontsize=24);

    plt.legend()

    if grid:
        plt.grid()

    if show_values:
        for axis in axes:
            for bar in axis:
                w, h = bar.get_width(), bar.get_height()
                plt.text(bar.get_x() + w/2, bar.get_y() + h/2,
                         value_format.format(h), ha="center",
                         va="center")


LOG = get_logger()
