# TODO Support suppression by rule id
# TODO support suppression of rule id + file
# TODO add more placeholder rules for xpath like sqli
# TODO support good findungs like CSRF check is present
# add documentation to change all serverside js like electron pantomjs nodejs
# more granular test, look for detection nos
# make a github action
# more templating framework https://expressjs.com/en/resources/template-engines.html
# Support minified versions - try lusca xss header minfied

#express coverage for param types

// GET /search?q=tobi+ferret
console.dir(req.query.q)
// => 'tobi ferret'

// GET /shoes?order=desc&shoe[color]=blue&shoe[type]=converse
console.dir(req.query.order)
// => 'desc'

console.dir(req.query.shoe.color)
// => 'blue'

console.dir(req.query.shoe.type)
// => 'converse'

// GET /shoes?color[]=blue&color[]=black&color[]=red
console.dir(req.query.color)
// => ['blue', 'black', 'red']

support for https://github.com/appsecco/dvna/blob/master/core/appHandler.js#L235