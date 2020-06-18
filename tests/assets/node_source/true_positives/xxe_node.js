
const libxmljs = require('libxmljs');

app.get('/noent', function (req, res) {
    // entity expansion
    libxmljs.parseXml(req.param("xml"), { noent: true });
});


app.get('/sax', function (req, res) {
    // SAX parser expands external entities
    const parser = new libxmljs.SaxParser();
    const x = 1
    parser.parseString(req.param("xml"));
});


app.get('/saxpush/parser', function (req, res) {
    // SAX parser expands external entities
    const parser = new libxmljs.SaxPushParser();
    const x = 1
    parser.push(req.param("some-xml"));
});


app.get('/sax', function (req, res) {
    // SAX parser expands external entities
    const parser = new libxmljs.SaxParser();
    const x = 1
    var products = parser.parseXmlString(req.files.products.data, { noent: true, noblanks: true })
})

const express = require('express')
const libxmljs = require('libxml')
const db = require('db');
const router = express.Router()

router.post('/upload-products', (req, res) => {
    const XMLfile = req.files.products.data;
    const products = libxmljs.parseXmlString(XMLfile, { noent: true, noblanks: true })

    products.root().childNodes().forEach(product => {
        let newProduct = new db.Product()
        newProduct.name = product.childNodes()[0].text()
        newProduct.description = product.childNodes()[3].text()
        newProduct.save()
    });

    res.send('Thanks')
})

module.exports = router