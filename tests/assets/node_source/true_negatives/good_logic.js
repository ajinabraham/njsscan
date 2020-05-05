var express = require('express');
var app = express();
app.get('/view/:id', function (req, res) {

    if (inDb(req.cookies["user"])) {
        showProfile();
    }

});
