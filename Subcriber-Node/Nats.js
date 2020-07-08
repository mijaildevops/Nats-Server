"use-strict";

//Connect to vsblty-cluster with a random clientId
var cluster = 'vsblty-cluster';
var clientId = 'vsblty-nodejs-sub-' +  Math.floor((Math.random() * 10000) + 1);
var stan = require('node-nats-streaming').connect(cluster, clientId);


stan.on('connect', function () {	
  console.log('Connected to ' + cluster + ' as client ' + clientId + '\n\n');
  
  
  var endpointId = '8907c1fd-c16e-4604-8d69-ef9aa8ceedd1';
  
  // facial + Identificacion
  //var channel = 'vsblty-channel-metrics-' + endpointId; // nothing
  //var channel = 'vsblty-channel-realtime-' + endpointId; // nothing
  var channel = 'vsblty-channel-frameprocessed-' + endpointId; // ok
  
  // Objectdetection
  //var channel = 'vsblty-channel-objectdetection-' + endpointId;
  // Metricas
  //var channel = 'vsblty-channel-metrics-' + endpointId;
  
  // Subscribe and get all available messages
  var opts = stan.subscriptionOptions().setDeliverAllAvailable();
  var subscription = stan.subscribe(channel, opts);
  subscription.on('message', function (msg) {
    console.log('Received a message with sequence [' + msg.getSequence() + ']');
	
	//Generate json filename based on sequence and date
	var dateFormat = require('dateformat');
	var actualDate = dateFormat(new Date(), "yyyymmddhMMss");
	var filename = msg.getSequence() + '_' + actualDate + '.json';
	
	//Write json file with received data
	var fs = require('fs');
	fs.writeFile ('./files/' + filename, msg.getData(), function(err) {
		if (err) throw err;
		console.log('Writing file ' + filename + ' to disk completed!\n');
	});
  });
});

stan.on('close', function() {
  process.exit();
});
