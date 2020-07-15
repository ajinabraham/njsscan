function okTest() {
    const express = require('express')
    const xml2json = require('xml2json')
    const app = express()
    const port = 3000

    app.get('/', (req, res) => {
        // ok
        const content = expat.toJson(someVerifiedData(), { coerce: true, object: true });
        res.send(content)
    })

    app.listen(port, () => console.log(`Example app listening at http://localhost:${port}`))
}