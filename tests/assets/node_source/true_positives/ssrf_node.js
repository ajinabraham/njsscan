var express = require('express');
const request = require('request');
var needle = require('needle');
var app = express();
const bent = require('bent')
const getJSON = bent('json')
const getBuffer = bent('buffer')
var urllib = require('urllib');

app.get('/', function (req, res) {
    request(req.query.name, function (error, response, body) {
        console.error('error:', error); // Print the error if one occurred
        console.log('statusCode:', response && response.statusCode); // Print the response status code if a response was received
        console.log('body:', body); // Print the HTML for the Google homepage.
    });

    needle('get', req.vbody.foo).then(res => {
        console.log(res.body);
    })
        .catch(err => {
            console.error(err);
        });


    urllib.request(req.foo, function (err, data, res) {
        if (err) {
            throw err; // you need to handle error
        }
        console.log(res.statusCode);
        console.log(res.headers);
        // data is Buffer instance
        console.log(data.toString());
    });

});

app.get('/', function (req, res) {

    needle.get(req.foo, function (error, response) {
        if (!error && response.statusCode == 200)
            console.log(response.body);
    });


    needle.post(req.foo)
        .pipe(out)
        .on('finish', () => {
            console.log('pipe done');
        });

    //Do not match this
    needle.get('http://google.com')
        .pipe(out)
        .on('finish', () => {
            console.log('pipe done');
        });

    //Do not match this to reduce false positives
    needle.get(somvar)
        .pipe(out)
        .on('finish', () => {
            console.log('pipe done');
        });


    axios.get(request.foo.bar)
        .then(function (response) {
            // handle success
            console.log(response);
        })
        .catch(function (error) {
            // handle error
            console.log(error);
        })
        .finally(function () {
            // always executed
        });


    let obj = await getJSON(req.foo);
    let buffer = await getBuffer(req.foo);

    fetch(req.post.doo, { method: 'POST', body: 'a=1' })
        .then(res => res.json()) // expecting a json response
        .then(json => console.log(json));

});

app.listen(8000);

needle.get(req.foo, function (error, response) {
    if (!error && response.statusCode == 200)
        console.log(response.body);
});


var net = require('net');


app.get('/', function (req, res) {
    var client = new net.Socket();
    client.connect(1337, req.body.host, function () {
        console.log('Connected');
        client.write('Hello, server! Love, Client.');
    });

    client.on('data', function (data) {
        console.log('Received: ' + data);
        client.destroy(); // kill client after server's response
    });

    client.on('close', function () {
        console.log('Connection closed');
    });


    const http = require('http');

    const req = http.get({ host: req.foo });
    req.end();
    req.once('response', (res) => {
        const ip = req.socket.localAddress;
        const port = req.socket.localPort;
        console.log(`Your IP address is ${ip} and your source port is ${port}.`);
        // Consume response object
    });

});