var obj = {
    func: function() {
        return this;
    },
    a: 1
}

function func() {
    return this;
}

console.log(func());                