import numpy as np
import matplotlib.pyplot as plt


def stacked_bars(data, series_labels, category_labels=None, orientation='horizontal', show_values=False,
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


def grouped_bars(df, columns, colours=None, title=None, xlabel=None, ylabel=None):
    """Plot in a single axis multiple bar graphs next to each other"""
    dim = len(columns)
    w = 0.75
    dimw = w / dim

    if not colours:
        colours = [None] * dim
    labels = [k.title() for k in columns]

    xticks = []
    xticks.append(range(0, len(df.index)))
    for k in range(1, dim):
        xticks.append([x + k * dimw for x in xticks[0]])
    xticks_loc = [x + dimw/2 for x in xticks[0]]
    xticks_str = [k.strftime("%Y-%d-%m") for k in df.index]

    fig, ax = plt.subplots(figsize=(18, 8), ncols=1)
    for k in range(dim):
        ax.bar(xticks[k], height=df[columns[k]], width=dimw, bottom=0.001, color=colours[k], label=labels[k])
    ax.grid(color='grey', linestyle='-', linewidth=0.5)
    ax.tick_params(axis='x', rotation=85)
    ax.legend()
    ax.set_xticks(xticks_loc)
    ax.set_xticklabels(xticks_str)
    if xlabel:
        ax.set_xlabel(xlabel, fontsize=16)
    if ylabel:
        ax.set_ylabel(ylabel, fontsize=16)
    if title:
        ax.set_title(title, fontsize=24)


def multi_graph_bar(df, columns, colours=None, title=None, xlabel=None, ylabel=None):
    """Plot a figure with multiple bar graphs stacked up vertically"""
    ncols = len(columns)

    if not colours:
        colours = [None] * ncols
    labels = [k.title() for k in columns]

    fig, ax = plt.subplots(figsize=(18, 12), nrows=ncols)
    fig.tight_layout(pad=7.5)
    for k in range(ncols):
        ax[k].bar(df.index, height=df[columns[k]], width=0.8, bottom=0.001, color=colours[k], label=labels[k])
        ax[k].grid(color='grey', linestyle='-', linewidth=0.5)
        ax[k].tick_params(axis='x', rotation=85)
        ax[k].legend()

        if xlabel:
            ax[k].set_xlabel(xlabel, fontsize=16)
        if ylabel:
            ax[k].set_ylabel(ylabel, fontsize=16)

    if title:
        fig.suptitle(title, fontsize=24)
