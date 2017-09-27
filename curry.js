const curry = function (fn) {
  let args = Array.prototype.slice.call(arguments, 1)
  return function () {
    return fn.apply(this, args.concat(
      Array.prototype.slice.call(arguments, 0)
    ))
  }
}

let sequence = function (start, end) {
  let result = []
  for (let i = start; i <= end; i++) {
    result.push(i)
  }
  return result
}

let seq = curry(sequence, 1)
let seq5= curry(seq, 5)
let seq10 =  curry(seq, 10)
console.log(seq5())
console.log(seq10())