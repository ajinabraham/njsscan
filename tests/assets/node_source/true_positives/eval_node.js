var express = require('express');
var app = express();
app.get('/', function (req, res) {
    var resp = eval("(" + req.query.name + ")");
    var z = new Function('arg1', 'arg2', req.query.name)
    z(1, 2);
    setTimeout('alert(' + req.body.name, 0);
    setInterval(req.body.name, 0);
    res.send('Response</br>' + resp);
});
app.listen(8000);
eval("outside_express")
setTimeout('alert(' + req.body.name, 0);
setInterval(req.body.name, 0);
new Function('arg1', 'arg2', req.query.name)