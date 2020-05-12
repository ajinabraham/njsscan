var mysql = require('mysql');

connection.query("SELECT * FROM bank_accounts WHERE dob = ? AND bank_account = ?", [
    req.body.dob,
    req.body.account_number
], function (error, results) { });


connection.query("SELECT * FROM bank_accounts WHERE dob = :dob AND bank_account = :account_number", {
    dob: req.body.dob,
    account_number: req.body.account_number
}, function (error, results) { });


const mycon = mysql.createConnection({ host: host, user: user, password: pass, database: db });
mycon.connect(function (err) {
    mycon.query('SELECT name FROM users WHERE id = ?', [req.body.dob], (err, res) => { });
});

const pg = require('pg');
const pgcon = new pg.Client({ host: host, user: user, password: pass, database: db });
pgcon.connect();
var inp =  req.foo.bar;
pgcon.query('SELECT name FROM users WHERE id = $1', [inp], (err, res) => { });


const pg = require('pg');
const pool = new pg.Pool(config);

function handler(req, res) {
    var qry = "SELECT FOO,BAR FROM TABLE WHERE CAT=$1"
        + " ORDER BY FOO";
    pool.query(qry, [req.foo.nar], function (err, results) {
    });
}