function okTest1() {
    // ok
    var saxStream = require("sax").createStream(strict, options)

    saxStream.on("ontext", function (node) {
        // same object as above
    })

    fs.createReadStream("file.xml").pipe(saxStream).pipe(fs.createWriteStream("file-copy.xml"))
}