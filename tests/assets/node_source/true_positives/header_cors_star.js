const express = require('express');

const app = express();

app.options('*', cors())
app.get('/', function (req, res) {

    res.set(ffff)
});

app.get('/', function (req, res) {
    var y = 1;
    var x = '*';
    //sgrep bug - https://github.com/returntocorp/sgrep/issues/512
    res.writeHead(200, { 'Access-Control-Allow-Origin': '*' });
    res.set('access-control-allow-origin', '*');
    //do not match - sgrep bug -rewrite-rule
    res.set('Access-Control-Allow-Origin', 'google.com');
    res.set('Access-Control-Allow-Origin', '*');
    res.set({
        'Content-Length': req.query.foo,
        'access-control-allow-origin': '*',
        'ETag': '12345'
    })
    res.writeHead(200, { 'Access-Control-Allow-Origin': '*' })

    res.set('access-control-allow-origin', x);

    // do not detect - sgrep bug
    res.set('access-control-allow-origin', 'xyz.com');
    //do not detect - sgrep bug
    res.set('access-control-allow-origin', null);

});