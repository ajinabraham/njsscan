var express = require('express');
var app = express();
app.get('/', function (req, res) {
    var resp = req.query.name;
    res.send('Response</br>');
});
app.get('/3', function (req, res) {
    var resp = req.query.name;
    res.write('Response</br>');
});

app.get('/3', function (req, res) {
    var resp = req.foo;
    var x = 1;
    var foo = '1111'
    res.write('Response</br>' + foo);
});

app.get('/noxss', function (req, res) {
    var resp = req.query.name;
    res.write('Response</br>');
});

app.get('/noxs2s', function (req, res) {
    var resp = req.query.name;
    res.write('Response</br>');
});
//Sgrep limitation
app.get('/xss', function (req, res) {
    var resp = req.query.name;
    var html = "ASadad" + "bar" + "Asdadads"
    res.write('Response</br>' + html);
});
app.listen(8000);