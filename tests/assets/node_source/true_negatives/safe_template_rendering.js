var handlebars = require('handlebars'),
    fs = require('fs');
// do not match
var template = handlebars.compile(source);

app.get('/', function (req, res) {
    //do not match
    var template = handlebars.compile(source);

});