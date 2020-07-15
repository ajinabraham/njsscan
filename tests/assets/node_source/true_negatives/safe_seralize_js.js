
function testOk() {
    // ok
    const result = serialize({ foo: '<img src=x />' }, { space: 2 })
    return result
}

function testOk2() {
    // ok
    const result = escape(serialize({ foo: '<img src=x />' }, { space: 2 }))
    return result
}

function testOk3() {
    // ok
    const result = encodeURI(escape(serialize({ foo: '<img src=x />' }, { space: 2 })))
    return result
}