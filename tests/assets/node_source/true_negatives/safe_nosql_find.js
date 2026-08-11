let username = env['user_admin'];
var query = { $where: `this.username == '${username}'` }
User.find(query, function (err, users) {
    if (err) {
        // Handle errors
    } else {
        res.render('userlookup', { title: 'User Lookup', users: users });
    }
});



app.post('/login', function (req, res) {
    User.findOne({ 'email': 'foo@bar.com', 'password': config['password'] }, function (err, data) {
        if (err) {
            res.send(err);
        } else if (data) {
            res.send('User Login Successful');
        } else {
            res.send('Wrong Username Password Combination');
        }
    })
});


var sani = require('mongo-sanitize')
async function removeContent(params) {
    logger.log('info', `Removing content for id: ${params.correlationId}`);
    const clean = sani(params.correlationId);

    const result = await db.collection('queue-items').findOne({ correlationId: clean });
    if (result) {
        const { _id: fileId } = await getFileMetadata({ gridFSBucket, filename: clean });
        await gridFSBucket.delete(fileId);
        return true;
    }
}

// mongo-sanitize on request input should not flag (issue #83)
app.post('/login-safe', function (req, res) {
    const emailClean = sani(req.body.email)
    User.findOne({ email: emailClean }, function (err, data) { })
    User.findOne({ email: sani(req.body.email) }, function (err, data) { })
})

const api = {
    currencyRate: {
        getByDateAndBase: async (date, base) => {
            return db.collection('currencyRate').findOne({
                date: sani(date),
                base: sani(base.toUpperCase()),
            })
        },
    },
}