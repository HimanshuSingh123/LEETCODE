/**
 * Calculates the sum of absolute differences between consecutive characters in the string based on their ASCII values.
 * @param {string} s
 * @return {number}
 */
var scoreOfString = function(s) {
    let sum = 0;
    var array = [];
    var pointer = 1;

    for(let i = 0; i < s.length; i++){
        array.push(s[i].charCodeAt(0));
    }
    for(let i = 0; i < array.length-1; i++){
        sum += Math.abs(array[i] - array[pointer])
        pointer += 1;
    }
    return sum;
};

function testFunction() {

    console.log(scoreOfString("zzzz") === 0 ? 'Test 1 Passed' : 'Test 1 Failed'); 

    console.log(scoreOfString("hello") === 13 ? 'Test 2 Passed' : 'Test 2 Failed'); 

    console.log(scoreOfString("") === 0 ? 'Test 3 Passed' : 'Test 3 Failed'); 

    console.log(scoreOfString("a") === 0 ? 'Test 4 Passed' : 'Test 4 Failed');
}

testFunction();