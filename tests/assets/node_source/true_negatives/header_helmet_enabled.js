const helmet = require('helmet')
app.use(helmet.dnsPrefetchControl({ allow: true }))