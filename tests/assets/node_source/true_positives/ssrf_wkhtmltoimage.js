var wkhtmltoimage = require('wkhtmltoimage')

// ruleid: wkhtmltopdf_ssrf_warning
wkhtmltoimage.generate(input(), { output: 'vuln.jpg' })

function test(userInput) {
    // ruleid: wkhtmltopdf_ssrf_warning
    wkhtmltoimage.generate(userInput, { output: 'vuln.jpg' })
}


app.get('/', function (req, res) {
    
    // ruleid:wkhtmltopdf_ssrf
    wkhtmltoimage.generate(req.foo, { output: 'vuln.jpg' })


});
