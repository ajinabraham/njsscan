var child_process = require('child_process');
var x = 1;
app.get('/', function (req, res) {
    child_process.exec(
        'foo',
        function (err, data) {
            console.log('err: ', err)
            console.log('data: ', data);
        });

    child_process.exec('gzip',
        function (err, data) {
            console.log('err: ', err)
            console.log('data: ', data);
        });

    child_process.exec('foobar',
        function (err, data) {
            console.log('err: ', err)
            console.log('data: ', data);
        });

    child_process.exec(
        "sdsd",
        function (err, data) {
            console.log('err: ', err)
            console.log('data: ', data);
        });

    //Do not detect this //technically this should be detected but sgrep limitation
    child_process.exec(
        foo + "asdD",
        function (err, data) {
            console.log('err: ', err)
            console.log('data: ', data);
        });

    child_process.execSync(
        'rsync -avAXz --info=progress2 "/src" "/dest"',
        { stdio: 'inherit' });

    res.send('Hello World!')
})

var foo = '1';
require('child_process').exec('info=progress2 "/src" "/dest"');


const router = require('express').Router();
const exe = require('child_process');

router.post('/', function (req, res) {
    exe.exec('ls ', function (err, data) {
        if (!err) {
            res.json({ message: data });
        } else {
            res.status(500).json({ message: err });
        }
    });
});

module.exports = router;


var http = require("http");
var url = require("url");
var exe = require('child_process');
http.createServer(function (request, response) {
    var parsedUrl = url.parse(request.url, true);
    exe.exec('ping -c 2  google.com', function (err, data) {
        response.end();
    });

}).listen(8888);

exe.exec('ping -c 2  google.com', function (err, data) {
    response.end();
});