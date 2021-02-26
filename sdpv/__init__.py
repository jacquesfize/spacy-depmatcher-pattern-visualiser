# coding = utf-8

from .draw import *
from .parser import *


def draw_pattern(pattern, mode="matplotlib", **kwargs):
    G = parse_spacy_pattern(pattern)
    if mode == "matplotlib":
        return draw_graph_matplotlib(G,**kwargs)
    else:
        return draw_graph_graphviz(G, **kwargs)
