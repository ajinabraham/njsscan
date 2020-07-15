app.get('/ok-test', (req, res) => {
    // ok
    const func = require(hardcodedPath)
    return res.send(func())
})

let okController = function (req, res) {
    // ok
    const func = require('lib/func.js')
    return res.send(func())
}
app.get('/ok-test2', okController)

app.listen(port, () => console.log(`Example app listening at http://localhost:${port}`))