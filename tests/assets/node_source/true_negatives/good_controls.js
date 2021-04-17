const rateLimit = require("express-rate-limit");

// Enable if you're behind a reverse proxy (Heroku, Bluemix, AWS ELB, Nginx, etc)
// see https://expressjs.com/en/guide/behind-proxies.html
// app.set('trust proxy', 1);

const apiLimiter = rateLimit({
    windowMs: 15 * 60 * 1000, // 15 minutes
    max: 100
});

// only apply to requests that begin with /api/
app.use("/api/", apiLimiter);


var cookieParser = require('cookie-parser')
var csrf = require('csurf')
var bodyParser = require('body-parser')
var express = require('express')

// setup route middlewares
var csrfProtection = csrf({ cookie: true })
var parseForm = bodyParser.urlencoded({ extended: false })

// create express app
var app = express()

// parse cookies
// we need this because "cookie" is true in csrfProtection
app.use(cookieParser())

app.get('/form', csrfProtection, function (req, res) {
    // pass the csrfToken to the view
    var x = req.csrfToken()
    res.set(csrfToken, x )
})

app.post('/process', parseForm, csrfProtection, function (req, res) {
    res.send('data is being processed')
})



app.use(helmet({
    // Content-Security-Policy
    "contentSecurityPolicy": {
        "directives": {
            "defaultSrc": ["'self'"],
            "scriptSrc": ["'self'", "'unsafe-inline'"]
        }
    },
    // X-DNS-Prefetch-Control
    "dnsPrefetchControl": { "allow": false },
    // Expect-CT
    "expectCt": {
        "enforce": true,
        "maxAge": 86400
    },
    // X-Frame-Options
    "frameguard": { "action": "deny" },
    "hidePoweredBy": {},
    // Strict-Transport-Security
    "hsts": {
        "includeSubDomains": true,
        "maxAge": 2592000
    },
    // X-Download-Options: noopen
    "ieNoOpen": {},
    // X-Content-Type-Options: nosniff
    "noSniff": {},
    // 'Cache-Control', 'Surrogate-Control', 'Pragma' and 'Expires' HTTP headers
    "nocache": {},
    "referrerPolicy": { "policy": "same-origin" },
    // X-XSS-Protection: '1; mode=block'
    "xssFilter": { "setOnOldIE": true }
}));


// CSP
const helmet = require('helmet')
app.use(helmet.contentSecurityPolicy({
    directives: {
        defaultSrc: ["'self'"],
        styleSrc: ["'self'", 'maxcdn.bootstrapcdn.com']
    }
}))
const csp = require('helmet-csp')
app.use(csp({
    directives: {
        defaultSrc: ["'self'"],
        styleSrc: ["'self'", 'maxcdn.bootstrapcdn.com']
    }
}))
app.use(csp({
    directives: {
        defaultSrc: ["'self'", 'default.com'],
        scriptSrc: ["'self'", "'unsafe-inline'"],
        sandbox: ['allow-forms', 'allow-scripts'],
        reportUri: '/report-violation',
        objectSrc: ["'none'"],
        upgradeInsecureRequests: true,
        workerSrc: false  // This is not set.
    }
}))

//cross domain policy
//const helmet = require('helmet')
app.use(helmet.permittedCrossDomainPolicies())
const permittedCrossDomainPolicies = require('helmet-crossdomain')
app.use(permittedCrossDomainPolicies())
app.use(permittedCrossDomainPolicies({ permittedPolicies: 'master-only' }))
app.use(permittedCrossDomainPolicies({ permittedPolicies: 'by-content-type' }))
app.use(permittedCrossDomainPolicies({ permittedPolicies: 'all' }))



//DNS-Prefetch-Control
const helmet = require('helmet')
// prefetch control off
app.use(helmet.dnsPrefetchControl())
app.use(dnsPrefetchControl())
app.use(helmet.dnsPrefetchControl({ allow: false }))
app.use(dnsPrefetchControl({ allow: false }))
// Sets "X-DNS-Prefetch-Control: on".
app.use(helmet.dnsPrefetchControl({ allow: true }))
app.use(dnsPrefetchControl({ allow: true }))


//Expect CT
const expectCt = require('expect-ct')
// Sets Expect-CT: max-age=123
app.use(expectCt({ maxAge: 123 }))
// Sets Expect-CT: enforce; max-age=123
app.use(expectCt({
    maxAge: 123,
    enforce: true,
}))
app.use(expectCt({
    enforce: true,
    maxAge: 30,
    reportUri: 'http://example.com/report'
}))


//Feature Policy
const helmet = require('helmet')
app.use(helmet.featurePolicy({
    features: {
        fullscreen: ["'self'"],
        vibrate: ["'none'"],
        payment: ['example.com'],
        syncXhr: ["'none'"]
    }
}))
const featurePolicy = require('feature-policy')
app.use(featurePolicy({
    features: {
        vibrate: ["'self'"],
        syncXhr: ["'none'"]
    }
}))


//Frameguard
// Make sure you run "npm install helmet" to get the Helmet package.
const helmet = require('helmet')
app.use(helmet.frameguard({ action: 'sameorigin' }))
// Make sure you run "npm install frameguard" to get the Frameguard package.
const frameguard = require('frameguard')
app.use(frameguard({ action: 'deny' }))
// Don't allow me to be in ANY frames.
// Sets "X-Frame-Options: DENY".
app.use(frameguard({ action: 'deny' }))
// Only let me be framed by people of the same origin.
// Sets "X-Frame-Options: SAMEORIGIN".
app.use(frameguard({ action: 'sameorigin' }))
app.use(frameguard())  // defaults to sameorigin
// Allow from a specific host.
// Sets "X-Frame-Options: ALLOW-FROM http://example.com".
// Note that browser support for this option is low!
app.use(frameguard({
    action: 'allow-from',
    domain: 'http://example.com'
}))
//sail js
const helmet = require('helmet');
module.exports.http = {
    middleware: {
        order: [
            'helmetProtection',
        ],
        helmetProtection: function helmetProtection(req, res, next) {
            return helmet({
                frameguard: {
                    action: 'deny',
                },
            })(req, res, next)
        },
    }
}



//Xpowered by
const helmet = require('helmet')
app.disable('x-powered-by')
app.use(helmet.hidePoweredBy())
const hidePoweredBy = require('hide-powered-by')
app.use(hidePoweredBy())
app.use(helmet.hidePoweredBy({ setTo: 'PHP 4.2.0' }))



//HSTS


const helmet = require('helmet')
// Sets "Strict-Transport-Security: max-age=5184000; includeSubDomains".
const sixtyDaysInSeconds = 5184000
app.use(helmet.hsts({
    maxAge: sixtyDaysInSeconds
}))
const hsts = require('hsts')
// Sets "Strict-Transport-Security: max-age=5184000; includeSubDomains".
const sixtyDaysInSeconds = 5184000
app.use(hsts({
    maxAge: sixtyDaysInSeconds
}))
app.use(helmet.hsts({
    maxAge: sixtyDaysInSeconds,
    includeSubDomains: false
}))
app.use(helmet.hsts({
    // Must be at least 1 year to be approved
    maxAge: 31536000,

    // Must be enabled to be approved
    includeSubDomains: true,
    preload: true
}))
const hstsMiddleware = helmet.hsts({ /* ... */ })
app.use((req, res, next) => {
    if (req.secure) {
        hstsMiddleware(req, res, next)
    } else {
        next()
    }
})

//ienoopen

const helmet = require('helmet')
// Sets "X-Download-Options: noopen".
app.use(helmet.ieNoOpen())
const ieNoOpen = require('ienoopen')
// Sets "X-Download-Options: noopen".
app.use(ieNoOpen())


//nosniff
const helmet = require('helmet')
// Sets "X-Content-Type-Options: nosniff".
app.use(helmet.noSniff())
// Make sure you run "npm install dont-sniff-mimetype" to get this package.
const noSniff = require('dont-sniff-mimetype')
// Sets "X-Content-Type-Options: nosniff".
app.use(noSniff())



//referrer policy
const helmet = require('helmet')
// Sets "Referrer-Policy: same-origin".
app.use(helmet.referrerPolicy({ policy: 'same-origin' }))
const referrerPolicy = require('referrer-policy')
// Sets "Referrer-Policy: no-referrer".
app.use(referrerPolicy({ policy: 'no-referrer' }))
// Sets "Referrer-Policy: same-origin".
app.use(helmet.referrerPolicy({ policy: 'same-origin' }))
// Sets "Referrer-Policy: unsafe-url".
app.use(helmet.referrerPolicy({ policy: 'unsafe-url' }))
// Sets "Referrer-Policy: no-referrer,unsafe-url"
app.use(helmet.referrerPolicy({
    policy: ['no-referrer', 'unsafe-url']
}))
// Sets "Referrer-Policy: no-referrer".
app.use(helmet.referrerPolicy())


// XSS protection header
const helmet = require('helmet')
// Sets "X-XSS-Protection: 1; mode=block".
app.use(helmet.xssFilter())
const xssFilter = require('x-xss-protection')
// Sets "X-XSS-Protection: 1; mode=block".
app.use(xssFilter())
app.use(xssFilter({ setOnOldIE: true }))
// This has some security problems for old IE!
app.use(xssFilter({ reportUri: '/report-xss-violation' }))
app.use(xssFilter({ mode: null }))