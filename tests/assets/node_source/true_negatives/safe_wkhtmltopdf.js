const express = require('express')
const app = express()
const port = 3000
const wkhtmltopdf = require('wkhtmltopdf')



app.post('/ok', async (req, res) => {
    // ok
    const pdf = wkhtmltopdf('<html></html>', { output: 'vuln.pdf' })
    res.send(pdf)
})

app.listen(port, () => console.log(`Example app listening at http://localhost:${port}`))