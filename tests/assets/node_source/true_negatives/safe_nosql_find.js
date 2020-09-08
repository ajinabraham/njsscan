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


async function removeContent(params) {
    logger.log('info', `Removing content for id: ${params.correlationId}`);
    const clean = sanitize(params.correlationId);

    const result = await db.collection('queue-items').findOne({ correlationId: clean }); //ignore: node_nosqli_injection
    if (result) {
        const { _id: fileId } = await getFileMetadata({ gridFSBucket, filename: clean });
        await gridFSBucket.delete(fileId);
        return true;
    }
}