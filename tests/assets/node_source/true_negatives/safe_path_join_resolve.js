const path = require('path')
const express = require('express')
const app = express()
const port = 3000
app.post('/test3', testCtrl3)

app.post('/okTest', function (req, res) {
    // ok
    createFile({
        filePath: pth.join(opts.path, 'val')
    })
    res.send('Hello World!');
})

app.listen(port, () => console.log(`Example app listening at http://localhost:${port}`))