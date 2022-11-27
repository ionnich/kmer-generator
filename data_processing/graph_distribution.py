import plotly.graph_objects as go
from matplotlib import pyplot as plt
from collections import Counter
from prettytable import PrettyTable


def print_hashing_statistics(tabulated_data, title):
    """
    Creates and prints the tabulated performance data for the hash table
    """

    table = PrettyTable(
        ["Hash Function", "Insertion Time", "Parsing Time", "Collisions"])

    table.title = title

    table.add_row([tabulated_data["Hash Function"][0], tabulated_data["Insertion Time"]
                  [0], tabulated_data["Parsing Time"][0], tabulated_data["Collisions"][0]])
    table.add_row([tabulated_data["Hash Function"][1], tabulated_data["Insertion Time"]
                  [1], tabulated_data["Parsing Time"][1], tabulated_data["Collisions"][1]])

    print(table)


def py_bar_graph(kmer_distribution):
    """
    Creates a bar graph using matplotlib
    """

    kmer_len = len(kmer_distribution[0][0])
    kmer_count = len(kmer_distribution)

    title = str(kmer_count) + " Kmer Distribution for " + \
        str(kmer_len) + "-mers"

    x_title = "Kmer"
    y_title = "Count"

    x = list()
    y = list()

    for kmer in kmer_distribution:
        x.append(kmer[0])
        y.append(kmer[1])

    plt.bar(x, y)
    plt.title(title)
    plt.xlabel(x_title)
    plt.ylabel(y_title)
    plt.show()


def bar_graph(kmer_distribution):
    """
    Creates a bar graph using plotly
    """

    kmer_len = len(kmer_distribution[0][0])
    kmer_count = len(kmer_distribution)

    title = str(kmer_count) + " Kmer Distribution for " + \
        str(kmer_len) + "-mers"

    x_title = "Kmer"
    y_title = "Count"

    x = list()
    y = list()

    for kmer in kmer_distribution:
        x.append(kmer[0])
        y.append(kmer[1])

    fig = go.Figure(data=[go.Bar(x=x, y=y)])
    fig = fig.update_layout(
        title=title,
        xaxis_title=x_title,
        yaxis_title=y_title,
    )
    fig.show()


def pie_chart(kmer_distribution):
    """
    Creates a pie chart using plotly
    """

    x = list()
    y = list()

    for kmer in kmer_distribution:
        x.append(kmer[0])
        y.append(kmer[1])

    fig = go.Figure(data=[go.Pie(labels=x, values=y)])
    fig.show()


def histogram(kmer_distribution):
    """
    Prints the kmer distribution as a primitive vertical histogram
    """

    histogram = Counter([kmer[0] for kmer in kmer_distribution])
    for key in sorted(histogram):
        count = histogram[key]
        padding = (max(histogram.values()) - count) * " "
        print(f"{key:3} {'■' * count}{padding} ({count})")
