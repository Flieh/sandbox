'use strict'
let fs = require('fs')
let page = fs.readFileSync(process.argv[2]).toString()
let lines = page.split('\n')
console.log(lines.length - 1)