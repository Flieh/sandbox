'use strict'
let Promise = require('bluebird')
let fs = Promise.promisifyAll(require('fs'))

fs.readFileAsync('input.txt', 'utf8')
  .then((contents) => {
    medOfThree(contents)
  },
  (err) => {
    return err
  })

let countVowels = (contents) => {
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
}

let sumOfDigits = (input) => {
  let lines = input.split('\n')
  const count = lines.shift()
  let output = ''
  let numbers = []
  let total
  let digits
  for (let i = 0; i < count; i++) {
    numbers = lines.shift().split(' ')
    numbers = numbers.map((number) => {
      return Number(number)
    })
    total = ((numbers[0] * numbers[1]) + numbers[2])
    // console.log(total)
    digits = countDigits(total)
    let sumOfDigits = 0
    for (let j = 0; j < digits; digits--) {
      let digit = Math.floor(total / (10 ** (digits - 1)))
      // console.log(digit)
      total -= digit * (10 ** (digits - 1))
      sumOfDigits += digit
    }
    // console.log(sumOfDigits)
    output += sumOfDigits
    output += ' '
  }
  console.log(output)
}

let countDigits = (number) => {
  if (number < 1) return 0
  let count = 1
  let magnitude = 9
  while (number > magnitude) {
    count++
    magnitude = magnitude + (magnitude * 10)
  }
  return count
}

let medOfThree = (input) => {
  let lines = input.split('\n')
  const count = lines.shift()
  const numElems = 3
  let numbers = []
  let temp
  let output = ''
  for (let i = 0; i < count; i++) {
    numbers = lines.shift().split(' ')
    let movement = false
    for (let j = 0; j < numElems - 1; j++) {
      if (numbers[j] > numbers[j + 1]) {
        temp = numbers[j]
        numbers[j] = numbers[j + 1]
        numbers[j + 1] = temp
        movement = true
      }
    }
    output += numbers[1]
    output += ' '
  }
  console.log(output)
}
