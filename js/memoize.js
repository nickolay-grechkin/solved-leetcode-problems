function memoize(fn) {
    const result = {}
    return function(...args) {
        const argsKey = JSON.stringify(args)
        if (!(argsKey in result)) {
            result[argsKey] = fn(...args);
        }
        return result[argsKey];
    }
}

