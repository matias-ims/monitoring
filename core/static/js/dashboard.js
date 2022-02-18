(function (global, factory) {
    if (typeof define === "function" && define.amd) {
      define("/dashboard", ["jquery", "Site"], factory);
    } else if (typeof exports !== "undefined") {
      factory(require("jquery"), require("Site"));
    } else {
      var mod = {
        exports: {}
      };
      factory(global.jQuery, global.Site);
      global.dashboard = mod.exports;
    }
  })(typeof globalThis !== "undefined" ? globalThis : typeof self !== "undefined" ? self : this, function (_jquery, _Site) {
    "use strict";
  
    _jquery = babelHelpers.interopRequireDefault(_jquery);
    (0, _jquery.default)(document).ready(function ($$$1) {
        (0, _Site.run)();
    });
    
    (0, _jquery.default)(document).ready(function ($$$1) {
            // var dynamicGauge = $$$1("#exampleDynamicGauge").data('gauge');
            // setInterval(function () {
            //   var random = Math.round(Math.random() * 1000);
            //   var options = {
            //     strokeColor: Config.colors("primary", 500)
            //   };
        
            //   if (random > 700) {
            //     options.strokeColor = Config.colors("pink", 500);
            //   } else if (random < 300) {
            //     options.strokeColor = Config.colors("green", 500);
            //   }
        
            //   dynamicGauge.setOptions(options).set(random);
            // }, 1500);
        
          setInterval(() => {
            $.ajax({
              type: 'GET',
              url: "data/",
              dataType: 'json',
              data:  { "objId": $$$1("#objId").val() },
              success: function(response) {
                $("#objId").val(response.p_id);
                console.log("Id =>" + response.p_id);
                var dynamicGauge = $$$1("#rpmGauge").data('gauge');
                dynamicGauge.set(80);
                console.log(response.rpm);
              },
              error: function(response) {
                  // alert the error if any occured
                  alert("ERROR...");
              },
            });
          }, 5000);
    });

    (function () {
      var seriesData = [[],];
      var random = new Rickshaw.Fixtures.RandomData(150);
  
      for (var i = 0; i < 150; i++) {
        random.addData(seriesData);
      }
  
      var $element = (0, _jquery.default)('#rpmChart');
      var graph = new Rickshaw.Graph({
        element: $element.get(0),
        width: $element.width(),
        height: 300,
        renderer: 'line',
        series: [{
          color: Config.colors("primary", 500),
          data: seriesData[0],
          name: 'RPM'
        }]
      });
      graph.render();
      
      setInterval(function () {
        random.removeData(seriesData);
        random.addData(seriesData);
        graph.update();
      }, 2000);

      var hoverDetail = new Rickshaw.Graph.HoverDetail({
        graph: graph
      });
      var legend = new Rickshaw.Graph.Legend({
        graph: graph,
        element: document.getElementById('rpmChartLegend')
      });
      var shelving = new Rickshaw.Graph.Behavior.Series.Toggle({
        graph: graph,
        legend: legend
      });
      var axes = new Rickshaw.Graph.Axis.Time({
        graph: graph
      });
      axes.render();
      (0, _jquery.default)(window).on('resize', function () {
        graph.configure({
          width: $element.width()
        });
        graph.render();
      });
    })();


  });
