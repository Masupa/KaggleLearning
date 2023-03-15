# Import packages
import numpy as np
import seaborn as sns
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


def plot_box(data, x, y, title, xlabel, ylabel):
    """Plot a boxplot of y vs x where y is a categorical
    feature and x is a numerical feature

    Parameters:
    -----------
    data : pd.DataFrame
        A pandas DataFrame
    x : str
        Variable name
    y : str
        Variable name
    title : str
        Title of box-plot
    xlabel : str
        X-axis label of box-plot
    ylabel : str
        Y-axis label of box-plot

    Returns:
    --------
        None
    """

    fig, ax = plt.subplots(figsize=(10, 10))

    # Boxplot
    sns.boxplot(data=data, x=x, y=y, whis=[0, 100], width=0.6, palette="vlag")

    # Labels
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)

    # Add vertical lines
    plt.grid(linestyle="--", linewidth=0.5, axis="x")


def plot_bar(data, title, ylabel, ticks_range, labels, figsize=(8, 10)):
    """Plot a bar-plot
    Parameters:
    -----------
    data : pd.Series
        A pandas Series
    title : str
        Title of bar-plot
    ylabel : str
        Y-axis label of bar-plot
    ticks_range : list
        A list of ticks
    labels : list
        A list of labels

    Returns:
    --------
        None
    """

    # Draw Axis
    fig, ax = plt.subplots(figsize=figsize)

    # Plot Barplot
    data.plot(kind="barh")

    # Labels
    plt.title(title)
    plt.xlabel("Frequency (%)")
    plt.ylabel(ylabel)

    # Add vertical lines
    plt.grid(linestyle="--", linewidth=0.5, axis="x")

    # Change the x ticks
    ax.set_xticks(ticks_range)
    ax.set_xticklabels(labels)
    


# DISTRIBUTION PLOTS - Helper Functions
# -------------------------------------

def plot_distribution_hist(variable, title_, x_label_, y_label_):
    """Plot a histogram distribution a variable.
    
    Parameters:
    -----------
    variable : pd.Series
        A pandas series contain a variable with it's values
    title_ : str
        Distribution title
    x_label_ : str
        Distribution x-label
    y_label_ : str
        Distribution y-label
        
    Returns:
        None
    """
    
    fig, ax = plt.subplots(figsize=(10, 5))

    # Histogram
    variable.plot(kind='hist', bins=20)

    # Title Properties
    fontdict = {"fontsize": 14, "fontweight": "bold"}

    # Labels
    plt.title(title_, fontdict=fontdict)
    plt.xlabel(x_label_)
    plt.ylabel(y_label_)

    plt.show();

    
def plot_distribution_boxplot(variable, title_, x_label_):
    """Plot a boxplot distribution a variable.
    
    Parameters:
    -----------
    variable : pd.Series
        A pandas series contain a variable with it's values
    title_ : str
        Distribution title
    x_label_ : str
        Distribution x-label
        
    Returns:
    --------
        None
    """
    
    fig, ax = plt.subplots(figsize=(10, 4))

    # Boxplot
    variable.plot(kind='box', vert=False)

    # Labels
    plt.title(title_)
    plt.xlabel(x_label_)
    
    plt.show();