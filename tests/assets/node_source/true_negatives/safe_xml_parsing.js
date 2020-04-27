var child_process = require('child_process');
var x = 1;
app.get('/', function (req, res) {
    var libxml = require("libxmljs");
    var xml = '<?xml version="1.0" encoding="UTF-8"?>' +
        '<root>' +
        '<child foo="bar">' +
        '<grandchild baz="fizbuzz">grandchild content</grandchild>' +
        '</child>' +
        '<sibling>with content!</sibling>' +
        '</root>';

    var xmlDoc = libxml.parseXmlString(foo);

    // xpath queries
    var gchild = xmlDoc.get('//grandchild');

    console.log(gchild.text());  // prints "grandchild content"

    var children = xmlDoc.root().childNodes();
    var child = children[0];

    console.log(child.attr('foo').value()); // prints "bar"

    var doc = libxml.parseXmlString(foo);
    var doc = libxml.parseXmlString(foo, { noblanks: true });
    res.send('Hello World!')
})


app.get('/some/path', function (req, res) {
    libxmljs.parseXml(foo);
});