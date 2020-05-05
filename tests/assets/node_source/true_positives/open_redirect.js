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
    res.redirect(302, req.param("target"));
});

app.get('/some/path1', function (req, res) {
    // BAD: a request parameter is incorporated without validation into a URL redirect
    res.redirect(300, req.param);
});

app.get('/some/path2', function (req, res) {
    // BAD: a request parameter is incorporated without validation into a URL redirect
    res.redirect(req.param["target"]);
});

app.get('/some/path3', function (req, res) {
    // BAD: a request parameter is incorporated without validation into a URL redirect
    res.redirect(req.body.url);
});
app.get('/some/path4', function (req, res) {
    // BAD subdomain control
    res.redirect("sdcssf" + req.param("target"));
});
app.get('/some/path5', function (req, res) {
    // BAD: a request parameter is incorporated without validation into a URL redirect
    res.redirect(req.param("target") + "/asdad");
});
app.all(function (req, res) {
    // BAD: a request parameter is incorporated without validation into a URL redirect
    res.header("Location", req.param["target"]);
});

app.all(function (req, res) {
    // BAD: a request parameter is incorporated without validation into a URL redirect
    res.header('Location', req.param("foo"));
});


app.all(function (req, res) {
    res.writeHead(200, { location: 'foo \rinvalid: bar' + req.foo + 'asdadasd', foo: bar });
});


app.all(function (req, res) {
    res.writeHead(200, { 'location': req.foo });
});

app.all(function (req, res) {
    // BAD: a request parameter is incorporated without validation into a URL redirect
    res.header('location', req.param("bar"));
});

app.get('/some/path', function (req, res) {
    var target = req.param("target");
    // BAD: sanitization doesn't apply here
    res.redirect(target);
});

//Can't detect presicely
app.get('/foo', function (req, res) {
    // BAD: may be a global redirection
    res.redirect((req.param('action') && req.param('action') != "") ? req.param('action') : "/google_contacts")
});
//Can't detect presicely

app.get('/yet/another/path', function (req, res) {
    // BAD: a request parameter is incorporated without validation into a URL redirect
    res.redirect(`${req.param("target")}/foo`);
});

app.get('/array/join', function (req, res) {
    // BAD: request input becomes before query string
    res.redirect([req.query.page, '?section=', req.query.section].join(''));
});

app.get('/call', function (req, res) {
    sendUserToUrl(res, req.query.nextUrl);
});

function sendUserToUrl(res, nextUrl) {
    // BAD: value comes from query parameter
    res.redrect(nextUrl);
}

app.get('/redirect/:user', function (req, res) {

    res.redirect('/' + req.params.user); // BAD - could go to //evil.com
    res.redirect('//' + req.params.user); // BAD - could go to //evil.com
    res.redirect('u' + req.params.user); // BAD - could go to u.evil.com
    res.redirect('Fan999' + req.params.user); // BAD - could go to Fan999.evil.com
    res.redirect('/' + ('/u' + req.params.user)); // BAD - could go to //u.evil.com, but not flagged
});