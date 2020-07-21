const shell = require('shelljs');
const express = require('express')
const router = express.Router()

router.get('/greeting', (req, res) => {
    // ok
    const input = 'ls ./'
    return shell.exec(input, { silent: true })
})

router.get('/foo', (req, res) => {
    // ok
    return shell.exec('ls ./', { silent: true })
})