from flask import Flask, Markup, render_template, request
app = Flask(__name__)


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

@app.route('/')
def hello_world():
    html_= draw_pattern(pattern,mode="notebook",height="500").data
    return render_template("skeleton.html",test=Markup(html_))

@app.route("/graph",  methods = ['POST'])
def get_graph():
    json = request.get_json()
    html_ = draw_pattern(json, mode="notebook",height="500").data

    return Markup(html_)

app.run(debug=True)