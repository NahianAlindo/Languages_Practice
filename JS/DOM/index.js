// document.getElementById('example').innerHTML = 'Javascript rules!!'
// object literal syntax
const circle = {
    radius: 1,
    location: {
        x: 1,
        y: 1
    },
    draw: function(){
        console.log('draw');
    }
};


// factory function 
function createCircle(radius){
    return {
        radius,
        draw: function(){
            console.log('draw');
        }
    };
}

const circle2 = createCircle(1);

circle2.draw();

// js e class keyword chilo na es6 e. ekhon ase
function Circle(radius){
    this.radius = radius;
    this.draw = function(){
        console.log('draw');
    }
}

const another = new Circle(1); // prefered syntax

// Circle.call({//this - default constor u defined}, 1//arguments);
// the previous line works exactly like new
// Circle.apply({}, [1,2,3]//arguments passed in array) // same like Circle.call but not arguments passed in an array instead of , separated

// primitives like numbers are copied by value
// objects, arrays n functions are copied by reference
let x = 10;
let y = x;
x = 20;
console.log(x,y); // x: 20, y:10
x = {value: 10};
y = x;
// y.value :10

let num = { value: 10 };
function increase(num){
    num.value++;
}
increase(num);

// function numbero(){ // recommended for multi-line functions
//     return 20;
// }

const newCircle = new Circle(10);
newCircle.location = {x:1};
newCircle['location'] = {x:1};
const propertyName = 'location';
newCircle[propertyName] = {x:1};

const properyName  = 'center-location'
//circle.center-location will not work
// therefore, the following will work
newCircle[propertyName] = {x:1};

for (let key in newCircle){
    if (typeof newCircle[key] !== 'function')
        console.log(key, newCircle[key]);
}

const keys = Object.keys(newCircle);
console.log(keys);

if ('radius' in newCircle){
    console.log('Circle has a radius.');
}

// abstraction
function Circle1(radius){
    this.radius = radius;

    let defaultLocation = { x:0, y:0 };

    this.getDefaultLocation = function(){
        return defaultLocation;
    }
    let computeOptimumLocation = function(factor){
        console.log('draw');
    }
    //getter , setter
    Object.defineProperty(this, 'defaultLocation',{
        get: function(){
            return defaultLocation;
        },
        set: function(value){
            if (!value.x || !value.y){
                throw new Error('Invalid location.');
            }
            defaultLocation = value;
        }
    });
}

const circle1 = new Circle1(10);
circle1.defaultLocation = 1;
