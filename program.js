'use strict'
let count = 0
for (let i = 2 ; i < process.argv.length ; i += 1) {
  count += parseInt(process.argv[i]) 
}
console.log(count)

