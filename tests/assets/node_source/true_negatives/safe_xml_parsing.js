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

    var xmlDoc = libxml.parseXmlString(xml);

    // xpath queries
    var gchild = xmlDoc.get('//grandchild');

    console.log(gchild.text());  // prints "grandchild content"

    var children = xmlDoc.root().childNodes();
    var child = children[0];

    console.log(child.attr('foo').value()); // prints "bar"

    var doc = libxml.parseXmlString(xml);
    var doc = libxml.parseXmlString(xml, { noblanks: true });
    res.send('Hello World!')
})