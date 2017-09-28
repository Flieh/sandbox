'use strict'
let Promise = require('bluebird')
let fs = Promise.promisifyAll(require('fs'))
fs.readFileAsync('input.txt', 'utf8')
  .then((contents) => {
    let lines = contents.split('\n')
    const count = lines.shift()
    let output = ''
    const vowels = 'aeiouy'
    for (let i = 0; i < count; i++) {
      let line = lines.shift()
      let vowelCount = 0
      for (let j = 0; j < line.length; j++) {
        if (vowels.indexOf(line.charAt(j)) > -1) vowelCount++
      }
      output += vowelCount
      output += ' '
    }
    console.log(output)
  },
  (err) => {
    return err
  })
