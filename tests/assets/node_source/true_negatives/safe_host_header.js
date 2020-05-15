app.get('/', function (req, res) {
    //do not match
    var x = 'https://' + foo
    // do not match
    var x = "https://" + req.foo + "/reset" + foo;
    // do not match
    var x = "https://" + z + "/reset";

    var reset = 'https://site.com/' + req.somethingelse + '/password_reset';

    var site = "sitehead.com"
    var foo = {
        text: 'reset password: https://' + site + '/resettoken/' + foo,
        token: 'f2131ASDSADASoo',
    };

});
