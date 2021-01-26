var session = require('express-session')
var express = require('express')
var app = express()

function samestite() {
    var expiryDate = new Date(Date.now() + 60 * 60 * 1000) // 1 hour
    var opts = {
        keys: ['key1', 'key2'],
        name: 'foo',
        cookie: {
            secure: true,
            sameSite: 'strict',
            domain: 'example.com',
            path: 'foo/bar',
            maxAge: expiryDate
        }
    }

    app.use(session(opts))
}

