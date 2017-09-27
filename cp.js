'use strict';
var maxSearch = 200000;
var startSearch = 50005;
var isPrime = function (num) {
    if (num === 1 || num == 2 || num === 3 || num === 5)
        return true;
    if (num % 2 === 0 || num % 3 === 0 || num % 5 === 0)
        return false;
    for (var i = 7; i <= Math.sqrt(num); i += 2) {
        if (num % i === 0)
            return false;
    }
    return true;
};
var target = startSearch;
var timer = 0;
for (var i = 0; i < maxSearch; i++) {
    timer = Date.now();
    if (isPrime(target)) {
        process.stdout.write('  ' + target + '  found in ' + (Date.now() - timer) + ' ms');
        break;
    }
    process.stdout.write('.');
    target++;
}
