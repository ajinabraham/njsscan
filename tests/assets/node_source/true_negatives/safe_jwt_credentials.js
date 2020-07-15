
function exampleOk1() {
    // ok
    const jose = require('jose')
    const { JWK, JWT } = jose
    const token1 = JWT.sign(Object.assign({ bar: 123 }, { one: 1, two: 2 }), secrt, { some: 'params' })
}

function exampleOk2() {
    // ok
    const jsonwt = require('jsonwebtoken')
    let payload;
    payload = { one: 1, two: 2, foo: 'bar' }
    const token1 = jsonwt.sign(payload, secrt, { some: 'params' })
}

