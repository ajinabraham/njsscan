var http = require('http'),
    fileSystem = require('fs'),
    path = require('path');


var express = require('express');
var app = express();
app.get('/', function (req, res) {
    var filePath = path.join(__dirname, '/' + req.query.load);
    var readStream = fileSystem.createReadStream(filePath);
    fileSystem.readFile(req.query.foo);
    console.log(fileSystem.readFileSync(req.query.nar, 'utf8'));
    var foo = req.query.y;
    fileSystem.readFile(foo);
    fileSystem.readFile(foo + "bar");
    readStream.pipe(res);
});
app.listen(8888);
// do not match
fileSystem.readFile(ddd);
