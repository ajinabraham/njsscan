var jwt = require('express-jwt');
var blacklist = require('express-jwt-blacklist');

// ok
app.get('/ok-protected', jwt({ secret: process.env.SECRET, isRevoked: blacklist.isRevoked }), function (req, res) {
    if (!req.user.admin) return res.sendStatus(401);
    res.sendStatus(200);
});


// ok
let configSecret = config.get('secret')
const opts = Object.assign({ issuer: 'http://issuer' }, { secret: configSecret, isRevoked: blacklist.isRevoked })

app.get('/ok-protected', jwt(opts), function (req, res) {
    if (!req.user.admin) return res.sendStatus(401);
    res.sendStatus(200);
});