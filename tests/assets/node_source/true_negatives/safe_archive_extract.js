
entry.pipe(fs.createWriteStream(fileName));

const fs = require('fs');
const unzip = require('unzip');
const path = require('path');

fs.createReadStream('archive.zip')
    .pipe(unzip.Parse())
    .on('entry', entry => {
        const fileName = entry.path;
        foo = fileName + '.js'
        entry.pipe(fs.createWriteStream(path.join('my_directory', path.basename(foo))));
    });

fs.createReadStream('archive.zip')
    .pipe(unzip.Parse())
    .on('entry', entry => {
        const fileName = entry.path;
        var x = fileName.indexOf('..');
        if (fileName.indexOf('..') == -1) {
            // sgrep limitation
            //entry.pipe(fs.createWriteStream(fileName));
        }
        else {
            console.log('skipping bad path', fileName);
        }
    });