# SDPV : Spacy DependencyMatcher Pattern Visualiser

SDPV is Python library designed to visualize Spacy DependencyMatcher Pattern and thus ease your pattern design.

## 1. Install


```shell
git clone https://github.com/Jacobe2169/spacy-depmatcher-pattern-visualiser.git
cd spacy-depmatcher-pattern-visualiser
python setup.py install
```

**In addition to the modules listed in `requirements.txt`, GraphViz must be installed!**
## 2. Use

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

### 2.1 Draw using matplotlib

Matplotlib is set by default, so just run:

```python
draw_pattern(pattern)
```

You can customize the node color, the label font color and the size of the generated figure.

```python
draw_pattern(pattern, node_color="grey",node_size=20,figsize=(10,5))
```

![image](./examples/matplotlib.png)

### 2.2 Draw using GraphViz

```python
draw_pattern(pattern,mode="graphviz")
```

![image](./examples/graphviz.png)

#### 2.2.1Display in Jupyter Notebook
Compared to Matplotlib, you need to set the parameter `show` to `ipynb`

```python
draw_pattern(pattern,mode="graphviz",show="ipynb")
```

### 2.3 Draw using vis.js (only in Notebook)

```python
draw_pattern(pattern,mode="notebook")
```

![image](./examples/notebook.png)
### 2.4 Save the Figure

Use the `filename` parameter 
```python
draw_pattern(pattern,mode="graphviz",filename="graphviz.png")
```

**Attention** As of today, the export of vis.js plot is only available in PNG.

## Use the GUI

If you wish to use SDPV in a better fashion, you can use the webapp

```shell
cd webapp
python server.py
```

## 3. Authors

This library was programmed by Jacques Fize.