import plotly.graph_objects as go


def bar_graph(kmer_distribution):
    # Create a bar graph of the kmer distribution
    # x-axis = kmer
    # y-axis = count

    x = list()
    y = list()

    for kmer in kmer_distribution:
        x.append(kmer[0])
        y.append(kmer[1])

    fig = go.Figure(data=[go.Bar(x=x, y=y)])
    fig.show()


def pie_chart(kmer_distribution):
    # Create a pie chart of the kmer distribution
    # x-axis = kmer
    # y-axis = count

    x = list()
    y = list()

    for kmer in kmer_distribution:
        x.append(kmer[0])
        y.append(kmer[1])

    fig = go.Figure(data=[go.Pie(labels=x, values=y)])
    fig.show()
