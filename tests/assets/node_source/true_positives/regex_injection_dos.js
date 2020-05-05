var express = require('express');
var app = express();

app.get('/search', function (req, res) {
    var key = req.param("key");
    // Regex created from user input
    var re = new RegExp("\\b" + key);
});
//do not detect this
var re = new RegExp("\\b" + key + "=(.*)\n");