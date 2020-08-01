

app.post('/smth', function (req, res) {
    // ruleid:node_nosqli_injection
    var query = {};
    query['email'] = req.body.email;
    User.findOne(query, function (err, data) {
        if (err) {
            res.send(err);
        } else if (data) {
            res.send('User Login Successful');
        } else {
            res.send('Wrong Username Password Combination');
        }
    })
});

app.post('/login', function (req, res) {
    // ruleid:node_nosqli_injection
    User.findOne({ 'email': req.body.email, 'password': req.body.password }, function (err, data) {
        if (err) {
            res.send(err);
        } else if (data) {
            res.send('User Login Successful');
        } else {
            res.send('Wrong Username Password Combination');
        }
    })
});