const wkhtmltopdf = require('wkhtmltopdf')

wkhtmltopdf(input(), { output: 'vuln.pdf' })

function test(userInput) {
    return wkhtmltopdf(userInput, { output: 'vuln.pdf' })
}


app.get('/', function (req, res) {
    wkhtmltopdf('<html><html/>', { output: 'vuln.pdf' })
    // ruleid:wkhtmltopdf_ssrf
    wkhtmltopdf(req.foo, { output: 'vuln.pdf' })

});