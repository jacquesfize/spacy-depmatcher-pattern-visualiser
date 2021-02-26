# coding = utf-8

from nxpd import draw
from matplotlib.figure import Figure
import networkx as nx


def draw_graph_matplotlib(G, nodesize=400, node_color="blue", font_color="white", figsize=(8, 5), filename=None,
                          **fig_kwargs):
    """
    Draw the pattern graph using matplotlib.
    Parameters
    ----------
    G : nx.Digraph
        pattern graph
    nodesize : int
        node size on the plot
    node_color: str
        node color
    font_color : str
        color of the node label
    figsize : List[float]
        size of the figure
    filename: str or None
        if not None, indicate the output filename
    fig_kwargs: dict
        matplotlib Figure args

    Returns
    -------
    Figure
        figure instance
    """
    fig = Figure(figsize=figsize)
    ax = fig.add_subplot(1, 1, 1)

    pos = nx.spring_layout(G, scale=5)
    nx.draw(G, pos, with_labels=True, node_shape="s",
            node_size=[len(G.nodes[v]["label"]) * nodesize for v in G.nodes()],
            font_color=font_color, labels=nx.get_node_attributes(G, "label"), ax=ax, node_color=node_color,
            arrowsize=20)
    nx.draw_networkx_edge_labels(G, pos, edge_labels=nx.get_edge_attributes(G, "label"), ax=ax)
    ax.set_axis_off()
    if filename:
        fig.savefig(filename)
    return fig


def draw_graph_graphviz(G, filename=None, show=True):
    """
    Draw the pattern graph using Graphviz
    Parameters
    ----------
    G: nx.Digraph
        pattern graph
    filename : str or None
        output filename if the figure is to be saved(default is None)
    show:bool or str
        display modality (True:system, "ipynb" : notebook).

    """
    if filename:
        draw(G, filename=filename)
    return draw(G, show=show)
