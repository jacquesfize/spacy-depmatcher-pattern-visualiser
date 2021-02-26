# SDPV : Spacy Dependency Matcher Visualiser

Python module to visualize the graph built from pattern for Space Dependency Matcher


## Install

In addition to the modules listed in `requirements.txt`, GraphViz have to be installed.

```shell
git clone https://github.com/Jacobe2169/spacy-depmatcher-pattern-visualiser.git
cd spacy-depmatcher-pattern-visualiser
python setup.py install
```

## Use

```python
from sdpv import draw_pattern

pattern = [
  # anchor token: founded
  {
    "RIGHT_ID": "founded",
    "RIGHT_ATTRS": {"ORTH": "founded"}
  },
  # founded -> subject
  {
    "LEFT_ID": "founded",
    "REL_OP": ">",
    "RIGHT_ID": "subject",
    "RIGHT_ATTRS": {"DEP": "nsubj"}
  },
  # "founded" follows "initially"
  {
    "LEFT_ID": "founded",
    "REL_OP": ";",
    "RIGHT_ID": "initially",
    "RIGHT_ATTRS": {"ORTH": "initially"}
  }
]
```

### Draw using matplotlib

Matplotlib is set by default, so just run:

```python
draw_pattern(pattern)
```

You can customize the node color, the label font color and the size of the generated figure.

```python
draw_pattern(pattern, node_color="grey",node_size=20,figsize=(10,5))
```

![image](./examples/matplotlib.png)

### Draw using GraphViz

```python
draw_pattern(pattern,mode="graphviz")
```

![image](./examples/graphviz.png)

### Save the Figure

Use the `filename` parameter 
```python
draw_pattern(pattern,mode="graphviz",filename="graphviz.png")
```



### 
draw_pattern(pattern,mode="graphviz",show="ipynb")