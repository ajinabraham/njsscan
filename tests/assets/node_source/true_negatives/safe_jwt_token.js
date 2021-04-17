//false
const token3 = jsonwt.sign(payload, config.secret)
//false
const token4 = jsonwt.sign(payload, secret2)

//false
const token11 = JWT.sign(payload, JWK.asKey(secret2))
//false
const token12 = JWT.sign(payload, secret2)



const jwt = require('jsonwebtoken')

const jwtSign = (payload = { id: 1 }) =>
    jwt.sign(payload, nop)

const jwtVerify = req => () => new Promise((resolve, reject) => {
    const token = req.headers['x-access-token']
    if (!token) {
        resolve(false)
    }
    jwt.verify(token, nop, (err, decoded) => {
        if (err) {
            resolve(false)
        }
        resolve(decoded)
    })
})

export default { jwtSign, jwtVerify }
    (() => {

        'use strict';

        let User = require('./user'),
            jwt = require('jsonwebtoken');

        const express = require('express');
        let router = express.Router();

        router.post('/signup', (req, res) => {
            let user = new User({
                name: name,
                password: password
            });
            var token = jwt.sign(user, safetoken, { expiresIn: 60 * 60 * 10 });
            res.send({ success: true, token: token });
        });

        module.exports = router;
    })();

'use strict';
const config = require('./app.config');
const privateMethods = {
    initialize(USER) {
        const router = require('express').Router(),
            jwt = require('jsonwebtoken');
        if (config) {
            router.route('/register').post((req, res) => {
                USER.findOne({}).exec((error, user) => {
                    if (error)
                        return res.status(400).send({ error: error });
                    user.save((error, user) => {
                        if (error) {
                            return res.status(400).send({ error: error });
                        } else {
                            const token = jwt.sign({ id: user._id }, safe);
                            return res.status(201).json({ token: token });
                        }
                    });
                });
            });
        }
    }
};
module.exports = privateMethods;