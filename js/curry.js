var curry = function(fn) {
    return function curried(...args) {
        if (fn.length === argsLength) {
            return fn(...args);
        }
        return function (...newArgs) {
            return curried(...args, ...newArgs);
        };
    };
};

fn = function sum(a, b, c) { return a + b + c; }
const curriedSum = curry(fn);
console.log(curriedSum(1, 2)(3));