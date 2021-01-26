
var express = require('express');
var router = express.Router();

router.get('/', function(req, res, next) {
     res.render('index')
});


router.post('/good', function(req, res, next) {
     res.render('index', { profile })
});

// Sure shot with hbs
var x = require('hbs')
var express = require('express');
var router = express.Router();

router.get('/', function(req, res, next) {
     res.render('index')
});

router.post('/good', function(req, res, next) {
     res.render('index', { profile })
});
module.exports = router;