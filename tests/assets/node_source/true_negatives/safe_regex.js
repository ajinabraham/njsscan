var express = require('express');
var app = express();

app.get('/search', function (req, res) {
    var key = req.param("key");
    var re = new RegExp("\\bfoo");
});