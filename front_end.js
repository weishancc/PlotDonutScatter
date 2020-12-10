function callback_donut(response){
  let donuts = JSON.parse(response); 
  
  let s = donuts[0]["name"]
  let f = donuts[donuts.length-1]["name"]
  let layout = {
      title: 'Buffalo Service Requests by Department<br>'+ s + " - " + f,
      showlegend: true,
      grid: {rows: 1, columns: donuts.length}
   };

  Plotly.newPlot('Div_Donut',donuts,layout);
  document.getElementById("starting_year_input").value = innerHTML = "";
  document.getElementById("ending_year_input").value = innerHTML = "";

} 

function plotDonut(){
  let startYear = document.getElementById("starting_year_input").value;
  let endYear = document.getElementById("ending_year_input").value;
  let donut = {"year_start":startYear ,"year_end":endYear};
  
  donut = JSON.stringify(donut);
  ajaxPostRequest("/donut", donut, callback_donut)
}


function callback_scatter(response){
  let scatter = JSON.parse(response);
  let year = scatter['year']
  let layout = {
      xaxis: { autorange: true },
      yaxis: { type: 'log', autorange: true },
      title: 'Service Request Duration by Department in '+ year
   };
  
  Plotly.newPlot('Div_Scatter', scatter['data'], layout)
  document.getElementById("year_input").value = innerHTML = "";
}


function plotScatter(){
  let year = document.getElementById("year_input").value;
  let scatter = {"year":year};
  
  scatter = JSON.stringify(scatter);
  ajaxPostRequest("/scatter", scatter, callback_scatter)
}