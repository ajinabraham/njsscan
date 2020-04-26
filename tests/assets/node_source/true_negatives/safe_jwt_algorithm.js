// ok
const jwt = require("jsonwebtoken");
const secret = safe_locattion;
const payload = jwt.verify(token, secret, { algorithms: ['RS256', 'HS256'] });