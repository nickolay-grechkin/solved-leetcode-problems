var debounce = function(fn, t) {
    let ref;
    return function(...args) {
        clearTimeout(ref);
        ref = setTimeout(() => fn(...args), t);
    }
};