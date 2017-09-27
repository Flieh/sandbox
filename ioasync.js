'use strict'
let fs = require('fs')
fs.readFile(process.argv[2], function(err, data) {
  if (err) return err
  let lines = data.toString().split('\n')
  console.log(lines.length - 1)
})
  