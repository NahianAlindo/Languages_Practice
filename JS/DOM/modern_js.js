
// arrow function
let numbero = () => {
    return 10;
}

console.log(numbero());

// arrow function with single return statement return 
// let number_ = () => return 10; eta hobe na instead wtite the bleow line
let number_ = () => 10;
console.log(number_());

let number_2 = (n) => n; // 
console.log(number_2(5));

let number_3 = n => n; // same as the previous one but not recommended syntax
console.log(number_3(4));

let number_4 = (a,b) => a+b;
console.log(number_4(10,5));