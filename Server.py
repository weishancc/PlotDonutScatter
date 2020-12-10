import bottle
import json
import App

@bottle.route("/")
def serve_html() :
  return bottle.static_file("index.html", root= "")

@bottle.route("/front_end.js")
def serve_front_end_js() :
  return bottle.static_file("front_end.js", root= "")

@bottle.route("/ajax.js")
def serve_AJAX() :
  return bottle.static_file("ajax.js", root= "")

@bottle.post("/donut")
def serve_donut():
  donut_chart = bottle.request.body.read().decode()
  donut_chart = json.loads(donut_chart)
  donut_data = App.data_by_subject(ALL_DATA, donut_chart)  
    
  return json.dumps(donut_data)


@bottle.post("/scatter")
def serve_scatter():
  scatter_plot = bottle.request.body.read().decode()
  scatter_plot = json.loads(scatter_plot)
  scatter_plot["year"] = str(scatter_plot["year"])

  data = App.data_by_subject_duration(ALL_DATA, scatter_plot)
  result = {'year':scatter_plot["year"], 'data':data}
  
  return json.dumps(result)

ALL_DATA = App.readCSV('311_Service_Requests_Abbreviated.csv')
bottle.run(host="localhost", port=8000, debug=True)
