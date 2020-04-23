const express = require('express');
const router = express.Router()

router.use((req, res, next) => {
    if (req.method === 'POST') {
        console.log(JSON.stringify(req.session.data, null, 2))
    }
    next()
})

router.post('/sprint18b/frequency', (req, res) => {
    res.redirect('/sprint18b/payment') //GOOD
});

var express = require('express');

var app = express();

app.get('/some/path', function (req, res) {
    // BAD: a request parameter is incorporated without validation into a URL redirect
    res.redirect(302, x);
});

app.get('/some/path1', function (req, res) {
    // BAD: a request parameter is incorporated without validation into a URL redirect
    res.redirect(300, 'http://google.com');
});

app.get('/some/path2', function (req, res) {
    // BAD: a request parameter is incorporated without validation into a URL redirect
    res.redirect('/foo/nar');
});

app.get('/some/path3', function (req, res) {
    // BAD: a request parameter is incorporated without validation into a URL redirect
    x = 'http://google.com'
    res.redirect(x);
});
app.get('/some/path4', function (req, res) {
    // BAD subdomain control
    res.redirect("sdcssf");
});
app.get('/some/path5', function (req, res) {
    // BAD: a request parameter is incorporated without validation into a URL redirect
    res.redirect(foo + "/asdad");
});
app.all(function (req, res) {
    // BAD: a request parameter is incorporated without validation into a URL redirect
    res.header("Location", bar);
});

app.all(function (req, res) {
    // BAD: a request parameter is incorporated without validation into a URL redirect
    res.header('Location', lol);
});

// bug in sgrep
app.all(function (req, res) {
    res.writeHead(200, { location: 'foo \rinvalid: barasdadasd', foo: bar });
});

//bug in sgrep may be?
app.all(function (req, res) {
    res.writeHead(200, { 'location': 'http' + foo });
});

app.all(function (req, res) {
    // BAD: a request parameter is incorporated without validation into a URL redirect
    res.header('location', fooo + '/bar');
});

app.get('/some/path', function (req, res) {
    var target = 'meh'
    // BAD: sanitization doesn't apply here
    res.redirect(target);
});


app.get('/yet/another/path', function (req, res) {
    // BAD: a request parameter is incorporated without validation into a URL redirect
    res.redirect(`${foo("target")}/foo`);
});

app.get('/array/join', function (req, res) {
    // BAD: request input becomes before query string
    res.redirect(['//', '?section='+ 'foo']);
});

app.get('/call', function (req, res) {
    sendUserToUrl(res, '/redirect?=http://foo.co,');
});

function sendUserToUrl(res, nextUrl) {
    // BAD: value comes from query parameter
    res.redrect(nextUrl);
}

app.get('/redirect/:user', function (req, res) {

    res.redirect('/' + foo); // BAD - could go to //evil.com
    res.redirect('//' + 'req.params.user'); // BAD - could go to //evil.com
    res.redirect('u' + 'req.user'); // BAD - could go to u.evil.com
    res.redirect('Fan999' + 'req.params.user'); // BAD - could go to Fan999.evil.com
    res.redirect('/' + ('/u' + 'req.params.user')); // BAD - could go to //u.evil.com, but not flagged
});