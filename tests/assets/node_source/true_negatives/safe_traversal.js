var http = require('http'),
    fileSystem = require('fs'),
    path = require('path');


var express = require('express');
var app = express();
app.get('/', function (req, res) {
    var filePath = path.join(__dirname, '/' + 'sss');
    var readStream = fileSystem.createReadStream("hardcoded");
    fileSystem.readFile("ddd");
    console.log(fileSystem.readFileSync('asass', 'utf8'));
    var foo = req.query.y;
    fileSystem.readFile("Asdada");
    //do not match
    fileSystem.readFile("bar");
    readStream.pipe(res);
});
app.listen(8888);
// do not match
fileSystem.readFile(ddd);
