// alert, prompt, let isBoss = confirm("Are you the boss");
// data types: number, bigint, string, boolean, null, undefined, symbol, object, Infinity
// ** means power
// use typeof()
// Converts non-numbers
console.log( +true ); // 1
console.log( +"" );   // 0
// CONDITIONAL FLOW

console.log('2' > 1); // true coz '2' becomes a number
console.log('01' == 1); // true coz string '01' becomes a number
console.log( true == 1 ); // true
console.log( false == 0 ); // true

let a = 0;
console.log(Boolean(a)); // false

let b = "0";
console.log(Boolean(b)); // true bcoz it's not an empty string
console.log(a==b); // true
console.log('' == false); // true bcoz it's an empty string

console.log(0===false); // false, bcoz the types are different
// === means strict equality check

console.log(null === undefined); // false
// for comparisions null/undefined are converted to numbers: null becomes 0, while undefined becomes NaN.

console.log(null>0); // false
console.log(null==0); // false ; this second one should be true but it is not bcoz this is an equality check not comparison.
console.log(null>=0); // true


console.log(undefined>0);
console.log(undefined<0);
console.log(undefined==0);
// Comparisons (1) and (2) return false because undefined gets converted to NaN and NaN is a special numeric value which returns false for all comparisons.
// The equality check (3) returns false because undefined only equals null, undefined, and no other value.

// Treat any comparison with undefined/null except the strict equality === with exceptional care.
// Don’t use comparisons >= > < <= with a variable which may be null/undefined, unless you’re really sure 
// of what you’re doing. If a variable can have these values, check for them separately.

console.log(5 > 4)
console.log("apple" > "pineapple")
console.log("2" > "12")
console.log(undefined == null)
console.log(undefined === null)
console.log(null == "\n0\n")
console.log(null === +"\n0\n")

// let age = prompt("Enter age")
// let accessAllowed = (age > 18) ? true : false


// let message = (age < 3) ? 'Hi, baby!' :
//   (age < 18) ? 'Hello!' :
//   (age < 100) ? 'Greetings!' :
//   'What an unusual age!';

//   console.log(message) THESE ARE NESTED IF STATEMENT SHORTHAND

let company = 'Netscape';
(company ==='Netscape') ? console.log("Right!") : console.log('Wrong');
let result = (a + b < 4) ? 'Below' : 'Over';

// let message = (login == 'Employee') ? 'Hello' :
//   (login == 'Director') ? 'Greetings' :
//   (login == '') ? 'No login' :
//   '';


// nullish coalescing operator
let user = "John";
// console.log(user??"Anonymous"); // takes the first non-nullish or not undefined defined truthy value
// DO NOT use ?? with && || operators
// loops and switch

// functions
function showMessage(user, text='Marley'){
    console.log('Hello everyone, ' + user + ' '+ text)
}

let userName = 'Bob';

showMessage(userName, 'Dylan')

