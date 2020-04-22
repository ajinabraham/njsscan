var server = http.createServer(function (req, res) {
    var bla = 'dsdsd';
    switch (testIndex++) {
        case 0:
            res.writeHead(200, { test: 'foo \r\ninvalid: bar' });
            break;
        case 1:
            res.writeHead(200, { test: 'foo \ninvalid: bar' });
            break;
        case 2:
            res.writeHead(200, { test: 'foo \rinvalid: bar'+'asdadasd', foo: bar });
            break;
        case 3:
            // sgrep can't detect this!
            res.writeHead(200, { test: bla + 'foo \n\n\ninvalid: bar' });
            break;
        case 4:
            res.writeHead(200, { test: 'ffff' });
            server.close();
            break;
        default:
            assert(false);
    }
    res.end('Hi mars!');
});
server.listen(common.PORT);

var express = require('express');
var app = express();
app.get('/', function (req, res) {
    res.writeHead(200, { test: 'foo \r\ninvalid: bar'});

    res.set('Content-Type', 'req.query.foo');
    res.set('foo', 'asdad' + 'eq.query.foo');
    res.set('req.query.foo', 'asdadad');
    res.set('asda' + 'req.query.foo', 'asdadad');
    res.set({
        'Content-Type': 'text/plain',
        'Content-Length': 'req.query.foo',
        'ETag': '12345'
    })
    //do not detect
    res.writeHead(200, { tast: ddd })
    res.set(ffff)
});


