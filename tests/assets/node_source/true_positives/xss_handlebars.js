function name() {
    var x = '<h1>hell0</h1>'
    var y = new Handlebars.SafeString(x);
    return new Handlebars.SafeString('<img src="" onload=alert(0)>');
}

function test2() {
    var x = 'foooo'
    var z = new Handlebars;
    var xx = z.SafeString(x)
    return xx;
}


var template = Handlebars.compile(source, { noEscape: true });
var template = "This is {{target}}";
var target = "user's pictures";
var result = Handlerbars.compile(template, { noEscape: true })({ target: target });
