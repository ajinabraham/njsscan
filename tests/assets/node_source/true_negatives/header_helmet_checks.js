const helmet = require('helmet')
const xssFilter = require('x-xss-protection')
const noSniff = require('dont-sniff-mimetype')
const hsts = require('hsts')
const frameguard = require('frameguard')
const permittedCrossDomainPolicies = require('helmet-crossdomain')

app.use(helmet.dnsPrefetchControl({ allow: true }))
app.use(dnsPrefetchControl({ allow: true }))