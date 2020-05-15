// https://www.acunetix.com/blog/articles/automated-detection-of-host-header-attacks/
app.get('/', function (req, res) {

    //semgrep string lateral support is pending
    var foo = {
        text: `reset url: https://${req.host}/password_reset/${token}`
    };

    //do not match
    var x = 'https://' + foo
    // do not match
    var x = "https://" + req.foo + "/reset" + foo;
    // do not match
    var x = "https://" + z + "/reset";



    var url = 'http://' + req.host;
    var reset = 'https://' + req.host + '/password_reset';
    var pass = "https://" + req.host + "/reset";

    var z = req.host;
    var pass = "https://" + z + "/reset";

    var reset_url = "Reset password: <a href='http://" + req.host + "/reset_pass'>Reset</a>";
    var foo = {
        text: 'password: https://' + req.host + '/token/',
        token: 'f2131ASDSADASoo',
    };

    var foo = {
        text: 'reset password: https://' + req['host'] + '/token/',
        token: 'f2131ASDSADASoo',
    };

    let x = "https://" + req['host'] + "/reset" + foo;
    x = "https://" + req("host") + "/reset" + foo + 'barr' + foo2;

    var foo = {
        text: 'reset password: https://' + req.host + '/resettoken/' + foo,
        token: 'f2131ASDSADASoo',
    };

});
