const express = require('express');
const lusca = require('lusca');

const app = express();

app.use(lusca({
    csrf: true,
    csp: { policy: "referrer no-referrer" },
    xframe: 'SAMEORIGIN',
    p3p: 'ABCDEF',
    hsts: { maxAge: 31536000, includeSubDomains: true, preload: true },
    xssProtection: true,
    nosniff: true,
    referrerPolicy: 'same-origin'
}));

app.use(lusca.csrf());
app.use(lusca.csp({ policy: [{ "img-src": "'self' http:" }, "block-all-mixed-content"], reportOnly: false }));
app.use(lusca.xframe('SAMEORIGIN'));
app.use(lusca.p3p('ABCDEF'));
app.use(lusca.hsts({ maxAge: 31536000 }));
app.use(lusca.xssProtection(true));
app.use(lusca.nosniff());
app.use(lusca.referrerPolicy('same-origin'));

app.get('/', function (req, res) {
    var x = 1;
    res.writeHead(200, { 'x-xss-protection': 1 });

    res.set('x-xss-protection', '1; mode=block');
    //do not match
    res.set('x-xss-protection', 1);
    res.set('X-XSS-Protection', 1);
    //sgrep bug - https://github.com/returntocorp/sgrep/issues/512
    res.set({
        'Content-Length': '122',
        'x-xss-protection': 1,
        'ETag': '12345'
    })
    //sgrep bug - https://github.com/returntocorp/sgrep/issues/512
    res.writeHead(200, { 'x-xss-protection': 1 })
    res.set('X-XSS-Protection', x);

    // do not detect
    res.set(ffff)
});
