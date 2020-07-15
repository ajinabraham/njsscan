const express = require('express')
const app = express()
const port = 3000
const wkhtmltoimage = require('wkhtmltoimage')

app.post('/test-ok', async (req, res) => {
    // ok
    const data = '<html></html>'
    const img = wkhtmltoimage.generate(data, { output: 'vuln.pdf' })
    res.send(img)
})

app.listen(port, () => console.log(`Example app listening at http://localhost:${port}`))