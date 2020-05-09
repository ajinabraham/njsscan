var handlebars = require('handlebars'),
    fs = require('fs'),
    Sqrl = require('squirrelly');
// do not match
var template = handlebars.compile(source);

app.get('/', function (req, res) {
    var storeName = "console.log(process.pid)" // this should be a user-controlled string
    function getStoreName() {
        return storeName;
    }
    var scope = {
        getStoreName: getStoreName
    }

    fs.readFile('example.html', 'utf-8', function (error, source) {
        var template = handlebars.compile(source + req.foo);
        handlebars.compile(source + req.foo.bar);


        var myTemplate = 'Hi, my name is {{name}}'
        var temp = myTemplate + req.foo['bar']
        var compiled = Sqrl.Compile(temp)


        var xx = source.replace('<!-->', req.foo)
        handlebars.compile(xx)


        var x = source + req.foo;
        var z = 2;
        handlebars.compile(x);

        var html = template(data);
        console.log(html)
    });

    //do not match
    var template = handlebars.compile(source);
});