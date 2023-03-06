# Import packages
import numpy as np
import matplotlib.pyplot as plt

def plot_scatter_plot(x, y, title, xlabel, ylabel):
    """Plot a Scatter plot

    Parameters:
    -----------
    x : pd.Series
        A pandas series
    y : pd.Series
        A pandas series
    title : str
        Title of plot
    xlabel : str
        X label of plot
    ylabel : str
        Y label of plot

    Returns:
    --------
        None
    """

    fig, ax = plt.subplots(figsize=(8, 6))

    # Scatter Plot
    plt.scatter(x=x, y=y)

    # Labels
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)

    # Adding x ticks
    labels = ["$0", "$100,000", "$200,000", "$300,000", "$400,000", "$500,000", "$600,000", "$700,000"]
    ax.set_yticks(list(range(0, 800_000, 100_000)))
    ax.set_yticklabels(labels)\

    plt.show()
