/**
 * @param {Array} arr
 * @param {number} size
 * @return {Array}
 */
var chunk = function(arr, size) {
    const resultingArr = [];

    for (i = 0; i < arr.length; i+=size) {
        const tmpArr = [];
        for (j = i; j < i + size; j++) {
            if (arr[j] !== undefined) {
                tmpArr.push(arr[j])
            }
        }
        resultingArr.push(tmpArr);
    }
    return resultingArr;    
};

console.log(chunk([], 1))


arr = [1,9,6,3,2], 
size = 3