var untrusted_code = '"toString": !<tag:yaml.org,2002:js/function> "function (){very_evil_thing();}"';
var notneeded=1;
// I'm just converting that string, what could possibly go wrong?
require('js-yaml').load(untrusted_code) + ''

var yaml = require('js-yaml')

const yaml2 = require('js-yaml')

yaml.load(untrusted_code)
yaml2.load(untrusted_code)