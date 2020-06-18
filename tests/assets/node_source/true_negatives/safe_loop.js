const express = require('express');
const router = express.Router()


router.post("/list-users", (req, res) => {
    var obj = req.params.foo
    var someArr = [];

    for (var i = 0; i < obj.length; i++) {
        someArr.push(obj[i]);
    }

    res.send("done");
});


module.exports = router


app.post("/foo", (req, res) => {
    var obj = req.foo;

    var ret = [];

    for (var i = 0; i < obj.length; i++) {
        ret.push(obj[i]);
    }
});