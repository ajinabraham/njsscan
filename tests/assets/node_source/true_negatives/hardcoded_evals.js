var express = require('express');
var app = express();
app.get('/', function (req, res) {
    var resp = eval("(hello())");
    var z = new Function('arg1', 'arg2')
    z(1, 2);
    setTimeout('alert(', 0);
    setInterval('1223', 0);
    res.send('Response</br>');
});
app.listen(8000);
eval("outside_express")
setTimeout('alert(', 0);
setInterval('nnnnn', 0);
new Function('arg1', 'arg2', 'ssss')