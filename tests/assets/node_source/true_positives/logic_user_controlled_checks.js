var express = require('express');
var app = express();
app.get('/view/:id', function (req, res) {

    if (req.cookies["user"] === req.params["id"]) {
        showProfile();
    }

});
