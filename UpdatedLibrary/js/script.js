'use strict';

/**
* Dashboard Menu View
**/
var DashboareMenuView = Stapes.subclass({

  _dashboardMenuList : null,

  _menuList: [
    {menuText: "Summary Report", menuIcon: "fa-pie-chart"},
    {menuText: "Detailed Report", menuIcon: "fa-list"}
  ],

  constructor: function(){
    this._bindEventHandlers();
    this._loadTemplate();
    this.emit('changeMenu', 0);
  },

  _loadTemplate: function(){
    var template = Mustache.render(document.getElementById('dashboard-menu-tmpl').innerHTML, this._menuList);
    this._dashboardMenuList = document.createElement('ul');
    this._dashboardMenuList.setAttribute('id', 'dashboard-menu-list');
    this._dashboardMenuList.innerHTML = template;
    [].slice.call(this._dashboardMenuList.children).forEach(function(li, index){
      li.addEventListener('click', function(e){
        this.emit('changeMenu', index);
      }.bind(this));
    }, this);
  },

  _bindEventHandlers: function(){
    this.on({
      'changeMenu' : function(index){
        this._updateActiveMenu(index);
      }
    })
  },

  _updateActiveMenu: function(idx){
    [].slice.call(this._dashboardMenuList.children).forEach(function(li, index){
      var arrow = li.querySelector('.arrow-left');
      if(li.classList.contains('active')) {
        li.classList.remove('active');
        arrow.classList.remove('active');
      }
      if(idx === index) {
        li.classList.add('active');
        arrow.classList.add('active');
      }
    }, this);
  },

  render: function(){
    document.getElementById('dashboard-menu').appendChild(this._dashboardMenuList);
    return this;
  }

});

var SummaryReportView = Stapes.subclass({

  constructor: function(){
    this._loadTemplates();
  },

  _loadTemplates: function(){
    this._summaryTemplate = document.getElementById('summary-tmpl').innerHTML;
    this._summaryChartTemplate = document.getElementById('summary-chart-tmpl').innerHTML;
    this._summaryScenariosTemplate = document.getElementById('summary-scenarios-tmpl').innerHTML;
  },

  render: function(resultData, channelMetrics, scenarioMetrics){
    document.getElementById('content').innerHTML = Mustache.render(this._summaryTemplate, resultData, {
      summaryChart: this._summaryChartTemplate,
      summaryScenarios: this._summaryScenariosTemplate
    });
    this._showOverallChart(resultData);
    this._showChannelChart(channelMetrics);
    this._showScenarioChart(scenarioMetrics);
    this._bindScenarioEventHandler();
  },

  updateOverallChart: function(resultData){
    document.getElementById('summary-chart').innerHTML = Mustache.render(this._summaryChartTemplate, resultData);
    this._showOverallChart(resultData);
  },

  updateChannelChart: function(channelMetrics){
    this._showChannelChart(channelMetrics);
  },

  updateScenarioChart: function(scenarioMetrics) {
	  this._showScenarioChart(scenarioMetrics);
  },

  _bindScenarioEventHandler: function(){
    var scenariosTableBody = document.getElementById('scenarios-table-body');
    var _thisView = this;
    [].slice.call(scenariosTableBody.children)
    .forEach(function(tableRow, index){
        tableRow.setAttribute("data-idx", index);
        tableRow.addEventListener('click', function(e){
            _thisView.emit('scenarioClick', index);
            e.stopImmediatePropagation();
            _thisView._onDocumentClickHandler = _thisView._onDocumentClick.bind(_thisView);
            document.removeEventListener('click', _thisView._onDocumentClickHandler);
            document.addEventListener('click', _thisView._onDocumentClickHandler);
            _thisView._updateSummaryActiveRow(index);
        });
    });
  },

  _onDocumentClick: function(e){
    this.emit('scenarioClick', -1);
    this._updateSummaryActiveRow(-1);
    document.removeEventListener('click', this._onDocumentClickHandler);
  },

  _updateSummaryActiveRow: function(idx) {
      var scenariosTableBody = document.getElementById('scenarios-table-body');
      [].slice.call(scenariosTableBody.children)
      .forEach(function(tableRow, index){
          if(tableRow.classList.contains('active')){
              tableRow.classList.remove('active');
          }
          if(idx === index){
              tableRow.classList.add('active');
          }
      });
  },

  _showOverallChart: function(resultData){
    var data = {
        series: []
    };

    if(resultData.metrics.passed) {
        data.series.push({value: resultData.metrics.passed, className: 'ct-series-a'});
    }
    if(resultData.metrics.failed) {
        data.series.push({value: resultData.metrics.failed, className: 'ct-series-b'});
    }
    if(resultData.metrics.skipped) {
        data.series.push({value: resultData.metrics.skipped, className: 'ct-series-c'});
    }

    var chartist = new Chartist.Pie('#overall-chart-container', {
        series: data.series
        }, {
           labelInterpolationFnc: function(series, value) {
               return Math.round(value / series.reduce(function(a, b) {
               	return {value: a.value + b.value};
               }).value * 100) + '%';
           }.bind(this, data.series)
        });
  },

  _showScenarioChart: function(scenarioMetrics){
	  document.getElementById('scenario-metrics-container').innerHTML =
		  Mustache.
		  render(document.getElementById('scenario-metrics-tmpl').innerHTML, scenarioMetrics);
	  var data = {
	        series: []
	    };

	    if(scenarioMetrics.metrics.passed) {
	        data.series.push({value: scenarioMetrics.metrics.passed, className: 'ct-series-a'});
	    }
	    if(scenarioMetrics.metrics.failed) {
	        data.series.push({value: scenarioMetrics.metrics.failed, className: 'ct-series-b'});
	    }
	    if(scenarioMetrics.metrics.skipped) {
	        data.series.push({value: scenarioMetrics.metrics.skipped, className: 'ct-series-c'});
	    }

	    var chartist = new Chartist.Pie('#overall-scenario-metrics-chart-container', {
	        series: data.series
	        }, {
	           labelInterpolationFnc: function(series, value) {
	               return Math.round(value / series.reduce(function(a, b) {
	               	return {value: a.value + b.value};
	               }).value * 100) + '%';
	           }.bind(this, data.series)
	        });
  },

  _showChannelChart: function(channelMetrics){
    var series = [];
    Object.keys(channelMetrics.channelMetrics).forEach(function(key, index){
      var passed = series[0] ? series[0] : [];
      var failed = series[1] ? series[1] : [];
      var skipped = series[2] ? series[2] : [];

      passed.push({value: channelMetrics.channelMetrics[key].passed, className: 'ct-series-a'});
      failed.push({value: channelMetrics.channelMetrics[key].failed, className: 'ct-series-b'});
      skipped.push({value: channelMetrics.channelMetrics[key].skipped, className: 'ct-series-c'});

      series = [passed, failed, skipped];
    });
    new Chartist.Bar('#channel-chart-container',{
        labels: Object.keys(channelMetrics.channelMetrics),
        series: series
      }, {
      stackBars: true,
      axisX: {
        onlyInteger: true
      },
      axisY: {
        onlyInteger: true
      },
      plugins: [this._ctStackBarLabels(series).bind(this)]
    }).on('draw', function(data) {
        if(data.type === 'bar') {
          data.element.attr({
            style: 'stroke-width: 60px'
          });
        }
      });
  },

  _ctStackBarLabels: function(series, options) {
      return function ctStackBarLabels(chart) {
        var defaultOptions = {
          labelClass: 'ct-label',
          labelOffset: {
            x: 0,
            y: 0
          },
          textAnchor: 'middle'
        };

        options = Chartist.extend({}, defaultOptions, options);

        if(chart instanceof Chartist.Bar) {
          chart.on('draw', function(data) {
            if(data.type === 'bar') {
              if(data.series[data.index].value){
                  data.group.elem('text', {
                    x: data.x1 + options.labelOffset.x,
                    y: ((data.y1 + data.y2) / 2) + 4,
                    style: 'text-anchor: ' + options.textAnchor
                  }, options.labelClass).text(this._calculatePercentage(
                      [series[0][data.index],
                       series[1][data.index],
                       series[2][data.index]],
                       data.series[data.index].value));
              }
            }
          }.bind(this));
        }
      }
    },

    _calculatePercentage: function(series, value) {
        return Math.round(value / series.reduce(function(a, b) {
        	return {value: a.value + b.value};
        }).value * 100) + '%';
    }

});

/**
* Summary Controller
**/

var SummaryController = Stapes.subclass({

  constructor: function(){
    this._resultModel = new ResultModel();
    this._channelMetrics = this._calculateChannelMetrics(this._resultModel.getAll());
    this._scenarioMetrics = this._calculateScenarioMetrics(this._resultModel.getAll());
    this._summaryReportView = new SummaryReportView();
    this._bindEventHandlers();
  },

  _bindEventHandlers: function() {
    this.on({
      'show': function(){
        this._summaryReportView.
          render(this._resultModel.getAll(), this._channelMetrics, this._scenarioMetrics);
      }
    });

    this._summaryReportView.on({
      'scenarioClick': function(index){
        if (index !== -1) {
          this._summaryReportView.
            updateOverallChart(
              this._resultModel.getAll().scenarios[index]);
          this._summaryReportView.
            updateChannelChart(
              this._channelMetrics.scenariosChannelsMetrics[index]);
          this._summaryReportView.
          	updateScenarioChart(this._scenarioMetrics.scenarios[index]);
        } else {
          this._summaryReportView.
            render(this._resultModel.getAll(), this._channelMetrics, this._scenarioMetrics);
        }
      }
    }, this)

  },

  _calculateScenarioMetrics: function(resultData){
	var scenarioMetrics = {
			scenarios: [],
			metrics:{
				passed: 0,
				failed: 0,
				skipped: 0
			}
	};
	var scenarios = resultData.scenarios.map(function(scenario, index){
		var metrics = {
				passed: 0,
				failed: 0,
				skipped: 0
		}
		if (scenario.metrics.passed > 0 && scenario.metrics.failed === 0 ) {
			metrics.passed++;
			scenarioMetrics.metrics.passed++;
		} else if(scenario.metrics.failed !== 0) {
			metrics.failed++;
			scenarioMetrics.metrics.failed++;
		} else {
			metrics.skipped++;
			scenarioMetrics.metrics.skipped++;
		}
		return {metrics: metrics};
	});
	scenarioMetrics.scenarios = scenarios;
	return scenarioMetrics;
  },

  _calculateChannelMetrics: function(resultData) {
      var overAllChannelMetrics = {}
      var scenarioChannelsMetrics = resultData.scenarios.
        map(function(scenario, index){
        var channelMetrics = {};
        scenario.testCases.forEach(function(testCase, index){
          var channelName =
            testCase.testCaseName.substring(testCase.testCaseName.indexOf('-') + 1).trim();
          var metricsCount = {
            total : channelMetrics[channelName] ?
              channelMetrics[channelName].total : 0,
            passed : channelMetrics[channelName] ?
              channelMetrics[channelName].passed : 0,
            failed : channelMetrics[channelName] ?
              channelMetrics[channelName].failed : 0,
            skipped : channelMetrics[channelName] ?
              channelMetrics[channelName].skipped : 0
          };
          testCase.steps.forEach(function(step, index){
            metricsCount.total++;
            metricsCount.passed += step.status == 1 ? 1 : 0;
            metricsCount.failed += step.status == 2 ? 1 : 0;
            metricsCount.skipped += step.status == 3 ? 1 : 0;
          });
          channelMetrics[channelName] = metricsCount;
        });
        Object.keys(channelMetrics).forEach(function(key, index){
          overAllChannelMetrics[key] = {
            total: overAllChannelMetrics[key] ?
              overAllChannelMetrics[key].total + channelMetrics[key].total :
              channelMetrics[key].total,
            passed: overAllChannelMetrics[key] ?
              overAllChannelMetrics[key].passed + channelMetrics[key].passed :
              channelMetrics[key].passed,
            failed: overAllChannelMetrics[key] ?
              overAllChannelMetrics[key].failed + channelMetrics[key].failed :
              channelMetrics[key].failed,
            skipped: overAllChannelMetrics[key] ?
              overAllChannelMetrics[key].skipped + channelMetrics[key].skipped :
              channelMetrics[key].skipped
          }
        });
        return {
          scenarioName: scenario.scenarioName,
          channelMetrics: channelMetrics
        };
      });
      return {
        scenariosChannelsMetrics: scenarioChannelsMetrics,
        channelMetrics: overAllChannelMetrics
      };
  }

});

var DetailedReportView = Stapes.subclass({

  constructor: function(){
    this._loadTemplates();
  },

  _loadTemplates: function(){
    this._detailedReportTemplate = document.getElementById('detailed-report-tmpl').innerHTML;
    this._scenarioDetailsTemplate = document.getElementById('scenario-details-tmpl').innerHTML;
    this._stackTraceTemplate = document.getElementById('stack-trace-tmpl').innerHTML;
  },

  _hideStackTraceContainer: function() {
		document.getElementById('content').removeChild(this._stackTraceContainerDiv);
		document.removeEventListener('click', this._hideStackTraceContainerHandler);
		document.removeEventListener('keyup', this._onDocumentKeyUpHandler);
		this._stackTraceContainerDiv.removeEventListener('click', this._stackTraceContainerClickHandler);
  },
  
  _stackTraceContainerClickHandler: function(e) {
		e.stopPropagation();
},

  _onDocumentKeyUp: function(e) {
  	if (e.keyCode === 27) {
  		this._hideStackTraceContainer();
  	}
  },

  _screenShotsDocumentClick: function(){
    this._screenShotsView.emit('hide');
    document.removeEventListener('click', this._screenShotsDocumentClickHandler);
  },

  _screenShotsDocumentKeyUp: function(e) {
    if (e.keyCode === 27) {
      this._screenShotsDocumentClickHandler();
      document.removeEventListener('keyup', this._screenShotsDocumentKeyUpHandler);
    }
  },

  render: function(resultScenarios){
    document.getElementById('content').innerHTML = Mustache.render(this._detailedReportTemplate, resultScenarios, {
      scenarioDetails: this._scenarioDetailsTemplate
    });
    this._screenShotsView = new ScreeShotsView();

    resultScenarios.forEach(function(scenario, scenarioIndex){
      var stepsStartIndex = 1;
      scenario.testCases.forEach(function(testCase, testCaseIndex){
        testCase.steps.forEach(function(step, stepIndex){
          if (step.stackTrace !== null) {
            document.getElementById('content').
              querySelectorAll('.steps')[scenarioIndex].
              querySelector('.results').children[stepsStartIndex + stepIndex].
              querySelector('.status-column').addEventListener('click', function(e){
                this._stackTraceContainerDiv = document.createElement('div');
                this._stackTraceContainerDiv.setAttribute('class', 'stack-trace-container');
                this._stackTraceContainerDiv.innerHTML =
                  Mustache.render(this._stackTraceTemplate, {
                    testCaseName: testCase.testCaseName,
                    name: step.name,
                    exceptionMessage: step.exceptionMessage,
                    stackTrace: step.stackTrace
                  });
                var contentDiv = document.getElementById('content')
                contentDiv.appendChild(
                  this._stackTraceContainerDiv);
                this._hideStackTraceContainerHandler = this._hideStackTraceContainer.bind(this);
                this._onDocumentKeyUpHandler = this._onDocumentKeyUp.bind(this);
                this._stackTraceContainerDiv.addEventListener('click', this._stackTraceContainerClickHandler);
              	document.addEventListener('click', this._hideStackTraceContainerHandler);
              	document.addEventListener('keyup', this._onDocumentKeyUpHandler);
                var windowDimension = {
              		width : contentDiv.offsetWidth,
              		height : window.innerHeight
              	}
              	var boundingRect = this._stackTraceContainerDiv.getBoundingClientRect();
              	var containerDimension = {
              		width : boundingRect.width,
              		height : boundingRect.height
              	}
                var dashboardMenuWidth = document.getElementById('dashboard-menu').offsetWidth;
              	this._stackTraceContainerDiv.style.top = ((windowDimension.height / 2) - (containerDimension.height / 2))
              			+ 'px';
              	this._stackTraceContainerDiv.style.left = (dashboardMenuWidth + ((windowDimension.width / 2) - (containerDimension.width / 2)))
              			+ 'px';
              	e.stopPropagation();
              }.bind(this));
          }
          if (step.screenShots.length > 0) {
            var viewAnchor = document.createElement('a');
            viewAnchor.setAttribute('href', 'javascript:;');
            viewAnchor.textContent = 'View';
            viewAnchor.addEventListener('click', function(e) {
              e.stopPropagation()
              this._screenShotsView.emit('show', step.screenShots);
              this._screenShotsDocumentClickHandler = this._screenShotsDocumentClick.bind(this);
              this._screenShotsDocumentKeyUpHandler = this._screenShotsDocumentKeyUp.bind(this);
              document.addEventListener('click', this._screenShotsDocumentClickHandler);
              document.addEventListener('keyup', this._screenShotsDocumentKeyUpHandler);
              return false;
            }.bind(this));
            document.getElementById('content').
              querySelectorAll('.steps')[scenarioIndex].
              querySelector('.results').children[stepsStartIndex + stepIndex].
              querySelector('.media-column').appendChild(viewAnchor);
          }
        }, this);
        stepsStartIndex += testCase.steps.length + 1;
      }, this);
    }, this);
  }

});

var ScreeShotsView = Stapes.subclass({
  constructor: function() {
    this._screenShotsTemplate = document.getElementById('screenshots-tmpl').innerHTML;
    this._screenShotsDiv = document.createElement('div');
    this._screenShotsDiv.setAttribute('class', 'screenshot-container');
    document.getElementById('content').appendChild(this._screenShotsDiv);
    this._bindEventHandlers();
  },
  _bindEventHandlers: function() {
    this.on('show', function(screenShots){
      this._currentIndex = 0;
      this._screenShotsLength = screenShots.length;
      this._screenShotsDiv.classList.add('visible');
      this.render(screenShots);
      this._updateDirection();
      this._updateImage();
      document.getElementById('screenshot-image-container')
        .addEventListener('click', this._screenShotImageContainerClick);
      this._moveLeftHandler = this._moveLeft.bind(this);
      this._moveRightHandler = this._moveRight.bind(this);
      document.getElementById('direction-left')
        .addEventListener('click', this._moveLeftHandler);
      document.getElementById('direction-right')
        .addEventListener('click', this._moveRightHandler);
    }.bind(this));
    this.on('hide', function(){
      this._screenShotsDiv.classList.remove('visible');
      document.getElementById('screenshot-image-container')
        .removeEventListener('click', this._screenShotImageContainerClick);
      document.getElementById('direction-left')
        .removeEventListener('click', this._moveLeftHandler);
      document.getElementById('direction-right')
        .removeEventListener('click', this._moveRightHandler);
    }.bind(this));
  },
  _screenShotImageContainerClick: function(e){
    e.stopImmediatePropagation();
  },
  _moveLeft: function(e){
    if (this._currentIndex > 0) {
      this._currentIndex --;
    }
    this._updateDirection()
    this._updateImage();
  },
  _moveRight: function(e) {
    if (this._currentIndex < this._screenShotsLength - 1) {
      this._currentIndex ++;
    }
    this._updateDirection();
    this._updateImage();
  },
  _updateDirection: function() {
    if(this._currentIndex === 0) {
      document.getElementById('direction-left').classList.remove('visible');
    } else {
      document.getElementById('direction-left').classList.add('visible')
    }

    if(this._currentIndex === this._screenShotsLength - 1) {
      document.getElementById('direction-right').classList.remove('visible');
    } else {
      document.getElementById('direction-right').classList.add('visible');
    }
  },
  _updateImage: function() {
    [].slice.call(document.getElementById('screenshot-image-container').querySelectorAll('img'))
      .forEach(function(image, index){
        image.classList.remove('visible');
        if(this._currentIndex === index) {
          image.classList.add('visible');
        }
      }.bind(this));
  },
  _hideScreenShotView: function(e) {
    this._screenShotsDiv.classList.remove('visible');
  },
  render: function(screenShots) {
    this._screenShotsDiv.innerHTML = Mustache
            .render(this._screenShotsTemplate, screenShots);
  }
});

var DetailedController = Stapes.subclass({

  constructor: function(){
    this._resultModel = new ResultModel();
    this._detailedReportView = new DetailedReportView();
    this._bindEventHandlers();
  },

  _bindEventHandlers: function(){
    this.on('show', function(){
      this._detailedReportView.render(this._resultModel.getAll().scenarios);
    })
  }

});

/**
* Results Model
**/
var ResultModel = Stapes.subclass({
  constructor: function(){
    this.set(result);
  }
})

/**
* Main Controller
**/
var MainController = Stapes.subclass({

  constructor: function(){
    this._dashboardMenu = new DashboareMenuView().render();
    this._bindEventHandlers();
    this._summaryController = new SummaryController();
    this._detailedController = new DetailedController();
    this._summaryController.emit('show');
  },

  _bindEventHandlers: function(){
    this._dashboardMenu.on({
      'changeMenu': function(index){
        if (index === 0) {
          this._summaryController.emit('show');
        } else if (index === 1) {
          this._detailedController.emit('show');
        }
      }
    }, this);
  }

});

new MainController();
