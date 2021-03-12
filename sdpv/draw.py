# coding = utf-8
import copy

from IPython.core.display import HTML

from .nxpd import draw
from matplotlib.figure import Figure
import networkx as nx
import matplotlib.pyplot as plt
from .template_visjs import vis_js_template

def draw_graph_matplotlib(G, nodesize=400, node_color="blue",node_shape="s", font_color="white", figsize=(8, 5), filename=None,ax=None,
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
    if not ax :
        fig = Figure(figsize=figsize)
        ax = fig.add_subplot(1, 1, 1)
    else:
        fig = plt.gcf()

    pos = nx.spring_layout(G, k=0.30,iterations=20)
    nx.draw(G, pos, with_labels=True, node_shape=node_shape,
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


def draw_graph_notebook(G,height=600,node_distance=200):
    nodes_str = ""
    edges_str = ""
    for node in G.nodes(data=True):
        nodes_str = nodes_str + "{" + "id: \"{0}\",label: \"{1}\"".format(node[0], node[1]["label"].replace("\n",
                                                                                                            "\\n")) + "},\n"
    for edge in G.edges(data=True):
        edges_str = edges_str + "{" + "from: \"{0}\", to: \"{1}\", label: \"{2}\"".format(edge[0], edge[1],
                                                                                          edge[2]["label"].replace("\n",
                                                                                                                   "\\n")) + "},\n"
    html_ = copy.copy(vis_js_template)
    html_ = html_.replace("%%nodes", nodes_str.strip(",\n"))
    html_ = html_.replace("%%edges", edges_str.strip(",\n"))
    html_ = html_.replace("%%node_distance", str(node_distance))
    html_ = html_.replace("%%height", str(height))
    return HTML(html_)

