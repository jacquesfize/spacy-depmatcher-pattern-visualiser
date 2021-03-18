# coding = utf-8

import networkx as nx

label_rel = {
    "<":"immediately dependant of",
    ">":"immediately head of",
    "<<":"dependant of",
    ">>":"head of",
    ".":"immediately precedes",
    ".*":"precedes",
    ";":"immediately follows",
    ";*":"follows",
    "$+":"immediately right sibling of",
    "$-":"immediately left sibling of",
    "$++":"right sibling of",
    "$--":"left sibling of",
}

def parse_spacy_pattern(pattern):
    """
    Parse Spacy Dependency Pattern format. The function returns a graph that describe
    Parameters
    ----------
    pattern : list
        pattern

    Returns
    -------
    networkx.DiGraph
        pattern graph
    """
    G = nx.DiGraph()
    for node in pattern:
        u = node["RIGHT_ID"]
        u_label = str(u)
        for k, v in node["RIGHT_ATTRS"].items():
            if not k == "DEP":
                u_label += "\n{0}:{1}".format(k, v)
        G.add_node(u, label=u_label)
        if not "LEFT_ID" in node:
            continue
        v = node["LEFT_ID"]
        edge_attr = dict()
        edge_attr["label"] = label_rel[node["REL_OP"]]
        if "DEP" in node["RIGHT_ATTRS"]:
            edge_attr["label"] = edge_attr["label"] + "\n TYPE : " + str(node["RIGHT_ATTRS"]["DEP"])

        if node["REL_OP"] in "< << . .* $+ $++".split():
            G.add_edge(u, v, **edge_attr)
        elif node["REL_OP"] in "> >> ; ;* $- $--".split():
            G.add_edge(v, u, **edge_attr)
    return G