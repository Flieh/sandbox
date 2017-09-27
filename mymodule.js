let path = require('path')
function callback (err, data) {

}
module.exports = function (dir, ext, callback) {
  if (err) return err
  for (let i = 0 ; i < data.length ; i += 1) {
    if (path.extname(data[i]) === '.' + process.argv[3]) {
      console.log(data[i]) 
    } 
  }   
}