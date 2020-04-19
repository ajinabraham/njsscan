const express = require('express');
const app = express();


app.get('/', function (req, res) {
    var y = 1;
    var x = 'null';
    res.set('access-control-allow-origin', x);
    //do not match - sgrep bug -rewrite-rule
    // do not detect - sgrep bug
    res.set('access-control-allow-origin', 'xyz.com');
    //do not detect - sgrep bug
    res.set('access-control-allow-origin', null);

});