const fs = require('fs');
const { VM, NodeVM } = require('vm2');
const express = require('express')
const app = express()
const port = 3000

app.get('/', (req, res) => res.send('Hello World!'))


app.get('/ok-test1', async function (req, res) {
    code = `
    console.log("Hello world")
  `;

    const sandbox = {
        setTimeout,
        fs: {
            watch: fs.watch
        }
    };

    const vmResult = new VM({
        timeout: 40 * 1000,
        sandbox
    }).run(code);

    res.send('hello world');
})

app.get('/ok-test2', function (req, res) {
    const sandbox = {
        setTimeout,
        fs: {
            watch: fs.watch
        }
    };

    const nodeVM = new NodeVM({ timeout: 40 * 1000, sandbox });
    nodeVM.run('console.log("Hello world")')

    res.send('hello world');
})

app.get('/ok-test3', function (req, res) {
    const sandbox = {
        setTimeout,
        fs: {
            watch: fs.watch
        }
    };

    const nodeVM = new NodeVM({ timeout: 40 * 1000, sandbox });
    const script = new VMScript('console.log("Hello world")')
    nodeVM.run(script)

    res.send('hello world');
})



// ok
app.get('/ok-test4', async function okTest1() {
    code = `
    console.log("Hello world")
  `;

    const sandbox = {
        setTimeout,
        fs
    };

    return new VM({ timeout: 40 * 1000, sandbox }).run(code);
})

// ok
app.get('/ok-test5', function okTest2() {
    const sandbox = {
        setTimeout,
        fs
    };

    const nodeVM = new NodeVM({ timeout: 40 * 1000, sandbox });
    return nodeVM.run('console.log("Hello world")')
})

app.listen(port, () => console.log(`Example app listening at http://localhost:${port}`))