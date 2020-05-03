function name() {
    var x = '<h1>hell0</h1>'
    var y = new Handlebars.escapeExpression(x);
    return new Handlebars.escapeExpression('<img src="" onload=alert(0)>');
}

function test2() {
    var x = 'foooo'
    var z = new Handlebars;
    var xx = z.escapeExpression(x)
    return xx;
}


var template = Handlebars.compile(source, { noEscape: false });
var template = "This is {{target}}";
var target = "user's pictures";
var result = Handlerbars.compile(template, { noEscape: false })({ target: target });

Sqrl.autoEscaping(true)