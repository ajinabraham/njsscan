import { LoremIpsum } from "lorem-ipsum";
// const LoremIpsum = require("lorem-ipsum").LoremIpsum;

const lorem = new LoremIpsum({
    sentencesPerParagraph: {
        max: 8,
        min: 4
    },
    wordsPerSentence: {
        max: 16,
        min: 4
    }
});
let decipher = crypto.createDecipheriv('aes-128-ecb', Buffer.from(ENCRYPTION_KEY), iv);
lorem.generateWords(1);
lorem.generateSentences(5);
lorem.generateParagraphs(7);



var express = require('express');
var app = express();

app.get('/search', function (req, res) {
    var key = req.param("key");
    // Regex created from user input
    var re = new RegExp("\\b" + key);
});
//do not detect this
var re = new RegExp("\\b" + key + "=(.*)\n");


var express = require('express');
var app = express();
app.get('/', function (req, res) {
    var filePath = path.join(__dirname, '/' + req.query.load);
    fileSystem.readFile(filePath); // njsscan-ignore: generic_path_traversal
    readStream.pipe(res);
});

app.get('/', function (req, res) {
    var filePath = path.join(__dirname, '/' + req.query.load);
    fileSystem.readFile(filePath); // detect this
    readStream.pipe(res);
});


app.get('/some/path', function (req, res) {
    var target = req.param("target");
    // BAD: sanitization doesn't apply here
    res.redirect(target); //njsscan-ignore: express_open_redirect
});

app.listen(8888);

