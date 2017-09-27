'use strict'
let fs = require('fs')
let mymod = require('./mymodule.js')
fs.readdir(process.argv[2], 'utf-8', mymod)
