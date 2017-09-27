'use strict'
let fs = require('fs')
let path = require('path')
fs.readdir(process.argv[2], 'utf-8', callback)

function callback (err, data) {
  if (err) return err
  for (let i = 0 ; i < data.length ; i += 1) {
    if (path.extname(data[i]) === '.' + process.argv[3]) {
      console.log(data[i]) 
    } 
  }   
}