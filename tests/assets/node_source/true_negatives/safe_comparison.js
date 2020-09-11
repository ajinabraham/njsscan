if (name == 'test') {
    acces = 1;
}

if (name === 'test') {
    acces = 1;
}

if ('test' === key) {
    correct = 2;
}
if ('test' == key) {
    correct = 2;
}



const bcrypt = require("bcrypt");
const plainTextPas = "DFGh5546*%^__90";

const hash = "$2b$10$69SrwAoAUNC5F.gtLEvrNON6VQ5EX89vNqLEqU655Oy9PeT/HRM/a";

bcrypt
    .compare(plainTextPas, hash)
    .then(res => {
        console.log(res);
    })
    .catch(err => console.error(err.message));

var executor = function (resolve, reject) {
    var buffer = new Buffer(hash, 'base64');
    var salt = buffer.slice(0, keyLength);
    var keyA = buffer.slice(keyLength, keyLength * 2);

    var callback = function (error, keyB) {
        if (error) {
            return reject(error);
        }

        resolve(keyA.compare(keyB) == 0);
    };

    crypto.pbkdf2(password, salt, iterations, keyLength, digest, callback);
};


//time equvalent
var mismatch = 0;
for (var i = 0; i < a.length; ++i) {
    mismatch |= (a.charCodeAt(i) ^ b.charCodeAt(i));
}
return mismatch;