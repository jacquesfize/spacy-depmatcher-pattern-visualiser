# coding = utf-8
vis_js_template = """
<html>
<head>
    <script type="text/javascript" src="https://unpkg.com/vis-network/standalone/umd/vis-network.min.js"></script>
    <link rel="preconnect" href="https://fonts.gstatic.com"> 
<link href="https://fonts.googleapis.com/css2?family=Roboto:ital,wght@0,100;0,300;0,400;0,700;1,100&display=swap" rel="stylesheet">    <style type="text/css">

        #mynetwork {
            width: %%widthpx !important;
            height: %%heightpx !important;
        }
        .btn{
            color:white !important;
            background-color:rgb(53,150,243);
            padding:0.5em;
            border-radius:5px;
        }
    </style>
</head>
<body>
<div style="padding-top:2em">
<a href="#" class="btn" id="btn-download" download="output.png">Download</a>
<div id="mynetwork"></div>
</div>
<script type="text/javascript">
    // create an array with nodes
    var nodes = new vis.DataSet([
        %%nodes
    ]);

    // create an array with edges
    var edges = new vis.DataSet([
        %%edges
    ]);

    // create a network
    var container = document.getElementById('mynetwork');

    // provide the data in the vis format
    var data = {
        nodes: nodes,
        edges: edges
    };
    var options = {
    nodes:{
        shape:"box",
        borderWidth : 3,
        shapeProperties: {
              borderDashes: false, // only for borders
              borderRadius: 6
          },
          color: {
              border: 'rgb(51,170,204)',
              background: 'rgb(195,230,241)'
          },
          font:{
              face:"Roboto",
              multi: true,
              bold: {
                color: '#343434',
                face: 'Roboto',
                mod: 'bold'
              }
          }
    },
    edges:{
        arrows: {

          to: {
            enabled: true
            }
        },
      color: {
          color:'#848484',
          highlight:'#848484',
          hover: '#848484'},

        widthConstraint: 200,
        },
    physics:{
        enabled: true,
        solver: "repulsion",
        forceAtlas2Based: {centralGravity:0.01},
        repulsion: {nodeDistance:%%node_distance}
    }
    };

    // initialize your network!
    var network = new vis.Network(container, data, options);

    network.on("afterDrawing", function (ctx) {

        var button = document.getElementById('btn-download');
        button.addEventListener('click', function (e) {
            var dataURL = ctx.canvas.toDataURL('image/png');
            button.href = dataURL;
        });

  });
</script>
</body>
</html>"""