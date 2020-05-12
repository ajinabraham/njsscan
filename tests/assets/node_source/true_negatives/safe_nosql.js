
var MongoClient = require('mongodb').MongoClient;
timelineRouter.route("/api/timeline")
    .get(async function (req, res) {
        try {
            var foo = req.foo.bar;
            const startDate = "01/01/2000";
            const endDate = "01/01/2000";
            const query = { $where: "this.hidden == false" };

            if (startDate && endDate) {
                query["$where"] = "this.start >= new Date('" + startDate + "') && " +
                    "this.end <= new Date('" + endDate + "') &&" +
                    "this.hidden == false;";
            }

            const TimelineItem = await getTimelineItemModel();
            const timelineItems = await TimelineItem.find(query);
            console.log(colors.yellow(`# of Timeline Items retrieved: ${timelineItems.length}`));
            return res.json({ timelineItems: timelineItems });

        } catch (error) {
            res.status(500).send("There was an error retrieving timeline items.  Please try again later");
        }
    });

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