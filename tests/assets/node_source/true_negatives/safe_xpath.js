// Good
var xpath = require('xpath');
var express = require('express');
var app = express();
app.get('/xpath', function (req, res) {
    var user = req.param("name");
    var expr = xpath.parse("//persons/user[name/text()=$name]/details/text()");
    expr.select({
        node: root,
        variables: { name: user }
    });
    res.redirect('/home')
});