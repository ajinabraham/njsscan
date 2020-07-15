const vm = require('vm')



// ok
function testOk1(userInput) {
    var sandbox = {
        foo: 1
    }
    vm.createContext(sandbox)
    vm.runInContext('safeEval(orderLinesData)', sandbox, { timeout: 2000 })
}


// ok
app.get('/', function testOk1(userInput) {
    var sandbox = {
        foo: 1
    }
    vm.runInNewContext('safeEval(orderLinesData)', sandbox, { timeout: 2000 })
    res.send('hello world')
})


// ok
app.get('/', function okTest3(req, res) {
    const code = `
        var x = 1;
    `
    vm.runInThisContext(code)
    res.send('hello world')
})


// ok
app.get('/', function okTest4(req, res) {
    const parsingContext = vm.createContext({ name: 'world' })
    const code = `return 'hello ' + name`
    const fn = vm.compileFunction(code, [], { parsingContext })
})


// ok
app.get('/', function okTest5(req, res) {
    const parsingContext = vm.createContext({ name: 'world' })
    const code = `return 'hello ' + name`
    const fn = vm.compileFunction(code, [], { parsingContext })
    res.send('hello world')
})

//ok
app.get('/', function okTest6(req, res) {
    const script = new vm.Script(`
        function add(a, b) {
          return a + b;
        }

        const x = add(1, 2);
    `);

    script.runInThisContext();
    res.send('hello world')
})
