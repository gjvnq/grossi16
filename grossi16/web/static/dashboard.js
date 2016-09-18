var ResultsChart;
var ResultData={"LastUpdate": 0};

$( document ).ready(function() {
  ResultsChart = nv.addGraph(function() {
    ResultsChart = nv.models.pieChart().x(function(d) {
      return d.text
    }).y(function(d) {
      return d.votes
    }).showLabels(false);
    ResultsChart.noData("Nenhum voto por enquanto...");
    ResultsChart.labelType("percent").showLabels(true);
    ResultsChart.labelsOutside(false);
    ResultsChart.tooltip.contentGenerator(function(key) {
        resp = key.data.text + '<br/>' +  key.data.votes + ' voto(s)'
        return resp
       });
    ResultsChart.tooltip.enabled(true);

    d3.select("#results svg").datum({}).transition().duration(350)
    return ResultsChart;
  });

  update_chart_data();
})

function update_chart_data() {
  $.ajax({
    type: 'POST',
    url: '/teacher/get_data',
    data: JSON.stringify({ cache_prevention_workarround: 'bla' }),
    contentType: 'application/json',
    dataType: 'json',
    timeout: 300,
    context: $('#results'),
    success: function(new_data){
      update_results_time();
      if (new_data.LastUpdate > ResultData.LastUpdate) {
        console.log("Updating data")
        ResultData = new_data;
        update_chart_image(ResultData.votes);
      }
      setTimeout(update_chart_data, 300);
    },
    error: function(xhr, type){
      console.log(xhr);
      $("#err-results").text("Falha ao carregar os resultados: "+xhr.status+" "+xhr.statusText);
      setTimeout(update_chart_data, 300);
    }
  });
}

function update_results_time() {
  $("#err-info").text("Última atualização: "+new Date(Date.now()).toLocaleString());
}

function update_chart_image(data) {
  d3.select("#results svg").datum(data).transition().duration(350).call(ResultsChart);
}


function switchToPercentageMode() {
  ResultsChart.labelType("percent").showLabels(true);
  d3.select("#results svg").selectAll("*").remove();
  ResultsChart.update();
}