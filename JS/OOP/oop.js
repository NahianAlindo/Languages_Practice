// encapsulation - class
let employee = {
    baseSalary: 30_000,
    overtime: 10,
    rate: 20,
    getWage: function(){
        return this.baseSalary + (this.overtime * this.rate);
    }
}

console.log(employee.getWage());

// abstraction 

class Book{
    name = 'Name';
    _waterAmount = 0; // protected and inheritable
    // new in js in jun '21
    #waterLimit = 200; // private and non-inheritable
    // closures can be used to make sth private
    // look it up


    constructor(title, author, year){
        this.title = title;
        this.author = author;
        this.year = year;
    }

    #fixWaterAmount(value) {
        if (value < 0) return 0;
        if (value > this.#waterLimit) return this.#waterLimit;
    }

    setWaterAmount(value) {
        this.#waterLimit = this.#fixWaterAmount(value);
    }

    getTitle(){
        this.getTitle();
    }

    setTitle(title){
        this.title = title;
    }

    

    getSummary(){
        return `${this.title} was written by ${this.author} in ${this.year}`;
    }


    setWaterAmount(value) {
        if (value < 0) value = 0;
        this._waterAmount = value;
    }

    getWaterAmount() {
        return this._waterAmount;
    }

    getAge(){
        const years  = new Date().getFullYear() - this.year;
        `return ${this.title} is ${years} years old`;
    }

    revise(newYear){ // revised edition year
        this.year = newYear;
        this.revised = true;
    }

    static topBookStore(){
        return 'Barnes & Noble';
    }
}

// Magazine Subclass
class Magazine extends Book{
    constructor(title, author, year, month){
        super(title, author, year);
        this.month = month;
    }
}

// abstract class er kachakachi
class Abstract {
    constructor() {
      if (new.target === Abstract) {
        throw new TypeError("Cannot construct Abstract instances directly");
      }
    }
  }
  
class Derived extends Abstract {
constructor() {
    super();
    // more Derived-specific stuff here, maybe
}
}

const a = new Abstract(); // new.target is Abstract, so it throws
const b = new Derived(); // new.target is Derived, so no error


// abstract class where method needs to be overridden
class Abstract {
    constructor() {
      if (this.method === undefined) {
        // or maybe test typeof this.method === "function"
        throw new TypeError("Must override method");
      }
    }
  }
  
class Derived1 extends Abstract {}

class Derived2 extends Abstract {
method() {}
}
  
  const a = new Abstract(); // this.method is undefined; error
  const b = new Derived1(); // this.method is undefined; error
  const c = new Derived2(); // this.method is Derived2.prototype.method; no error


const book1 = new Book('Book1', 'John Doe', '2013');
console.log(book1);
book1.revise('2018');
console.log(book1);
console.log(Book.topBookStore());

const mag1 = new Magazine('mag one', 'John Doe', '2018');
mag1.getSummary();
console.log(book1.name);

