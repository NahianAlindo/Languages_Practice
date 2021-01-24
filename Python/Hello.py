import turtle
import calendar
import math
import re
import datetime
import pytz
import numpy as np
import pandas as pd
from collections import namedtuple
from collections import deque
from collections import ChainMap
from collections import Counter
from collections import OrderedDict
import converters
# import array as arr

#  from collections import defaultdict does not throw error for accessing unknown key

#  import time
#  regular expressions
text = "jkadflsdkjfl nrifaat26@gmail.com lkfjadsfj nazibriasa41@gmail.com"
pattern = re.compile("[a-zA-Z0-9\.\_]+@[a-zA-Z0-9]+\.[a-zA-Z0-9]+")
result = pattern.search(text)
print(result)
result = pattern.findall(text)
print(result)
x = 2.9
print(math.fabs(x))
print(math.ceil(x))
print(math.floor(x))
print(math.gcd(3, 6))
print('Hell')
print('*' * 10)
is_published = False
print(is_published)
name = input('What is your full name?: ')  # scanf
print('Hello, ' + name)
birth_year = input('Enter ur birth year: ')
age = 2020 - int(birth_year)
print(age)
myTurtle = turtle.Turtle()


# printing square
def square():
    for side in range(8):
        myTurtle.forward(100)
        myTurtle.right(90)


square()
myTurtle.forward(300)
myTurtle.speed(500)
square()

print(calendar.weekheader(3))  # returns the weekdays in a 3 length word
print()
print(calendar.firstweekday())  # index of the first weekday as 0
print()
print(calendar.month(2020, 1))  # prints out month
print()
print(calendar.monthcalendar(2020, 3))  # prints month in matrix form
print()
print(calendar.calendar(2020))  # prints the whole year calendar
# returns integer of the weekdays index
dayOfTheWeek = calendar.weekday(2020, 1, 12)
print(dayOfTheWeek)
print()
print(calendar.isleap(2020))
print()

#  exclusive returning the count of leap days in the range of the year parameters
print(calendar.leapdays(2020, 2024))

Omio_weight = 68
alindo_weight = 69

if Omio_weight > alindo_weight:
    square()
else:
    myTurtle.forward(20)

while Omio_weight != 90:
    Omio_weight += 1
    myTurtle.forward(10)

digits = [0, 1, 2, 3, 1, 3]
print()
digits.append(5)
digits.reverse()
print(digits[0:4:2])  # strides of 2 skipping
print(digits[4:0:-2])

for i in range(len(digits)):
    print(digits[0:i:2])
print(digits)

problems = 'broke, pale, short, nerdy'
print(problems)
l = problems.split(", ")
print(l)
l2 = problems.split("pale, ")
print(l2)
joined = ' and '.join(l)  # joins add to the middle of each space
print(joined)

csv = ','.join(l)
print(csv)

#   tuples cannot be changed
#   this is called tuple unpacking
person = ("pants", 22, "Pizza")  # tuple
person2 = ("rishabh-pant", 22, "Pasta")  # tuple
people = [person, person2]
name, age, food = person  # assigning tuple to variables, also doable using parentheses
for name, age, food in people:
    print(name)
    print(age)
    print(food)

# sets are represented with braces {} they have no specific order, don't contain duplicates,ignores duplicates
Set = {'strawberry', 'raspberry'}
print(Set)
Set.add(4)
print(Set)

#   getting rid of duplicates in a list using a set

list2 = [1, 2, 3, 2, 4, 5, 5]
set2 = set(list2)
print(list2)
print(set2)
print(list(set2))

library_1 = {'hey', 'kgf', 'war'}
library_2 = {'hey', '2.0', '102'}

common = library_1.intersection(library_2)

diff = library_1.difference(library_2)

print(common)
print(diff)

dictionary = {'name': 'omio', 'blood': 'A+'}
print(dictionary.get('blood'))

dictionary2 = {'omio': 44,
               'Alindo': 45}
print(dictionary2['omio'])

dictionary3 = {
    'omio': {'blood': 'A+',
             'food': 'chicken'
             },
    'joe': [123, 456]
}
print(dictionary3['omio'])
print(dictionary.items())  # key value pairs
print(dictionary.keys())  # just keys
print(dictionary.values())  # just values

print(dictionary2)
dictionary2.popitem()  # pops the last pair
print(dictionary2)

print(dictionary3)
print(dictionary3.pop('joe'))  # pops specific key
print(dictionary3)
dictionary3['load'] = 3
print(dictionary3)
dictionary3.clear()
print(dictionary3)  # sorted(list(dictionary3.values())) sorts values
names = ['tanu', 'dhruba', 'dibbo']

# list comprehension is equivalent to looping through and doing some operation on items
print([person for person in names])
print([person + ' shot me' for person in names])
movies_rating = {'war': 8, 'kgf': 6, 'hotel transylvania': 8}
list_movie = []
for movie in movies_rating:
    if movies_rating[movie] > 6:
        list_movie.append(movie)

print(list_movie)

# equivalent list comprehension
print([movie for movie in movies_rating if movies_rating[movie] > 6])

today = datetime.date.today()
print(today)

birthday = datetime.date(1998, 4, 26)
print(birthday)

since = (today - birthday).days
print(since)

timeDelta = datetime.timedelta(days=10)
print(today + timeDelta)
print(today.month)
print(today.today())
print(today.weekday())
print(datetime.time(10, 29, 50, 23))  # datetime.datetime(Y, M, D, h, m, s, ms)
print(datetime.datetime.now() + datetime.timedelta(hours=10))

for tz in pytz.all_timezones:
    print(tz)

datetime_today = datetime.datetime.now(tz=pytz.UTC)
datetime_dhaka = datetime_today.astimezone(pytz.timezone('Asia/Dhaka'))
print(datetime_dhaka)

#  string formatting using dates
# f= string formatting p =parsing in the functions
print(datetime_dhaka.strftime('%B %d, %Y'))
#  datetime_thing = datetime.datetime.strptime('March 09, 2019', '&B %d, %Y')
#  print(datetime_thing)
#  maya library github

listed1 = [1, 2, 3, 4, 5]
# truncates last if zipping lists are not equal length
listed2 = ['one', 'two', 'three', 'four']
zipped = list(zip(listed1, listed2))
print(zipped)
listed2 = ['one', 'two', 'three', 'four', 'five']
zipped = list(zip(listed1, listed2))
print(zipped)
unzipped = list(zip(*zipped))
print(unzipped)

items = ['Apple', 'Banana', 'Orange']
counts = [3, 6, 4]
prices = [0.99, 1.2, 3.5]
sentences = []
for (item, count, price) in list(zip(items, counts, prices)):
    item, count, price = str(item), str(count), str(price)
    sentence = 'I bought ' + count + ' ' + item + 's at ' + price + ' dollars each.'
    #  sentences.append(sentence)
    print(sentence)

tupleA = namedtuple('courses', 'name, technology')
# tupleS = tupleA('data science', 'python')
tupleS = tupleA._make(['ai', "python"])
print(tupleS)
deckList = ['l', 'i', 's', 't']
deck = deque(deckList)
print(deck)
deck.append('python')
print(deck)
deck.appendleft('python3')
print(deck)
deck.pop()
print(deck)
deck.popleft()
print(deck)

dict1 = {1: 'learn', 2: 'python'}
dict2 = {3: 'implement', 4: 'R'}
chMap = ChainMap(dict1, dict2)
print(chMap)

listForCounter = [1, 2, 3, 4, 2, 1, 1, 3, 4]
counter = Counter(listForCounter)  # counter counts the hashable objects
print(counter)
print(list(counter.elements()))  # returns all the elements
# returns reverse sorted list of occurrence of all elements in a value: occurrence format
print(counter.most_common())
subtraction = {1: 2, 3: 1}
print(counter.subtract(subtraction))
print(counter.most_common())
ordDict = OrderedDict()
ordDict[1] = 'e'
ordDict[2] = 'd'
ordDict[3] = 'u'
print(ordDict)  # ordered dictionary inserts in dict in a ordered manner
print(ordDict.keys())
print(ordDict.items())

#   formatted strings
firstName = 'nahian'
lastName = 'alindo'
message = f'{firstName} [{lastName}] is a student'  # the {} work like %d
print(message)
print(message.upper())
# finds first occurrence index of searched character or else -1
print(message.find('s'))
print(message.replace('nahian', 'Awesome Nahian'))
print('nahian' in message)
for x in range(4):
    for y in range(4):
        print(f'({x}, {y})')

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
for row in matrix:
    for item in row:
        print(item)


def greet_user(userName, lastName):
    print(userName + ' ' + lastName)


greet_user(userName="Alindo", lastName="Nahian")
# this does not cause problems but if keyword argument was used before a
greet_user("Alindo", lastName="Nahian")


# conditional argument that would cause errors

def squaring(number):
    return number * number


a = squaring(2)
print(a)  # return of a function is None by default

#  exception handling
try:
    age = int(input('Please enter age: '))
    income = 20000
    risk = income / age
    print(age)
except ZeroDivisionError:
    print('You cannot divide by zero')
except ValueError:
    print('Invalid Value')


class Computer:
    def __init__(self, cpu, ram):
        self.cpu = cpu
        self.ram = ram
        print('in init')

    def config(self):
        print('Config is', self.cpu, self.ram)


comp1 = Computer('i5', 16)
comp2 = Computer('Ryzen', 8)
comp1.config()
Computer.config(comp1)  # same


class Car:
    #   class variables are outside init
    wheels = 4

    def __init__(self):  # constructor
        self.mil = 10  # instance variables
        self.com = 'BMW'


car1 = Car()
car2 = Car()
car1.mil = 8

print(car1.com, car1.mil, car1.wheels)
print(car2.com, car2.mil, car2.wheels)


class Student:
    school = 'Telusko'

    def __init__(self, m1, m2, m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    #  instance methods

    def avg(self):
        return (self.m1 + self.m2 + self.m3) / 3

    def get_m1(self):
        return self.m1

    def set_m1(self, val):
        self.m1 = val

    #  for variables outside init named class variables to access use cls instead of class
    @classmethod  # decorator for class method, same goes for decorator below for static method
    def getSchool(cls):
        return cls.school

    @staticmethod
    def info():  # static method . these have nothing to do with above instance or class methods
        print('This is a Student Class tutorial')


s1 = Student(30, 50, 66)
s2 = Student(46, 49, 56)
print(s1.avg())
print(s2.avg())
print(s1.getSchool())
print(s2.info())


class Person:

    def __init__(self, Sname, rollNo):
        self.name = Sname
        self.rollno = rollNo
        self.lap = self.Laptop()

    def show(self):
        print(self.name, self.rollno)
        self.lap.show()

    class Laptop:

        def __init__(self):
            self.brand = 'HP'
            self.cpu = 'i5'
            self.ram = 8

        def show(self):
            print(self.brand, self.cpu, self.ram)


stu1 = Person('nahian', 45)
stu1.show()
print(stu1.lap.brand)
lap1 = Person.Laptop()  # you have to access inner class after outer class
print(lap1.brand)  # prints same thing cause laptop is a subclass of person class
lap1.show()


# inheritance
class A:

    def __init__(self):
        print('in A init constructor')

    def feature1(self):
        print('feature 1 is working')

    def feature2(self):
        print('feature 2 is working')


class B(A):
    def feature3(self):
        print('feature 3 is working')

    def feature4(self):
        print('feature 4 is working')


class C(B):

    def __init__(self):
        # SUPER keyword is being used to access constor parent class even if C has its own constor
        super().__init__()
        print('in C init constructor')

    def feature5(self):
        print('feature 5 is working')


class D:

    def __init__(self):
        print('in D init')

    def feature6(self):
        print('feature 6 is working')


class E(B, D):
    def __init__(self):
        super().__init__()  # super has to decide between contor of B and D so
        # follows method resolution order from left to right so prints contor of a as b is on left inheriting from A

    def feature7(self):
        print('feature 7 is working')

    def feature8(self):
        super().feature4()


#  B<A: inheritance, C<B<A: multilevel inheritance, E<B&D: multiple inheritance as D does not inherit from C
#  demonstration

b = B()
b.feature1()
c = C()
c.feature2()
e = E()
e.feature1()  # does not have access to C so method does not show in intellisense
e.feature8()


# polymorphism method overloading overriding operator overloading
class PyCharm:

    def execute(self):
        print('Compiling')
        print('Running')


class MyIde:
    def execute(self):
        print('Compiling')
        print('Running')
        print('spell check')
        print('convention check')


class Laptop:
    def code(self, ide):
        ide.execute()


ide = PyCharm()  # lap2 object in form pycharm
lap2 = Laptop()
lap2.code(ide)
ide = MyIde()
lap2.code(ide)  # in form myide


# operator overloading
class Stud:
    def __init__(self, m1, m2):
        self.m1 = m1
        self.m2 = m2

    def __add__(self, other):
        m1 = self.m1 + other.m1
        m2 = self.m2 + other.m2
        stud3 = Stud(m1, m2)

        return stud3

    def __gt__(self, other):
        r1 = self.m1 + self.m2
        r2 = other.m1 + other.m2
        if r1 > r2:
            return True
        else:
            return False

    def __str__(self):
        return ' {} {} '.format(self.m1, self.m2)

    # method overloading
    # since python doesn't support overloading , we do it this way
    def sum(self, a=None, b=None, c=None):
        added = 0
        if a != None and b != None and c != None:
            added = a + b + c
        elif a != None and b != None:
            added = a + b
        else:
            added = a
        return added


stud1 = Stud(15, 30)
stud2 = Stud(56, 10)
Stud3 = stud1 + stud2
print(Stud3.m1)

if stud1 > stud2:
    print('stud1 wins')
else:
    print('stud2 wins')

print(stud1.sum(5, 3))


class AA:

    def show(self):
        print('in AA')


class BB(AA):
    def show(self):
        print('in BB')


a = BB()
a.show()

print(converters.kg_to_lbs(68))
# from converters import kg_to_lbs
# done to directly access the function without any . operator needed


seq = [1, 2, 3, 4, 5]
# maps function to the list with the lambda expression
print(list(map(lambda var: var*2, seq)))
# which is analogous to anonymous functions

print(list(filter(lambda num: num % 2 == 0, seq)))

tweet = 'Go Sports! #Sports'
# splits the tweet and gets anything after the pound sign
print(tweet.split('#')[1])
print('x' in [1, 2, 3])
x = [(1, 2), (3, 4), (5, 6)]
for a, b in x:  # tuple unpacking
    print(b)

my_list = [1, 2, 3]

arra = np.array(my_list)
print(arra)

my_mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(np.array(my_mat))


# numpy has built in methods used in the following
are = np.arange(0, 10)  # also takes steps and dtype as following parameters
print(are)
print(np.arange(0, 11, 2))
print(np.zeros(3))  # three zeros
print(np.zeros((5, 5)))  # passing a tuple of the zeros i want
print(np.ones(4))  # 4 ones
print(np.ones((5, 5)))  # matrix of ones
# prints 1d array of 10 equally spaced from 0 to 5
print(np.linspace(0, 5, 10))
print(np.eye(4))  # prints a 4x4 identity matrix
print(np.random.rand(5))  # uniform distributed 1d array in range of 0 to 1
print(np.random.rand(5, 5))  # uniform distributed 5x5 2d array in range 0 to 1
print(np.random.randn(4))  # from a standard normal distribution
print(np.random.randn(5, 5))
print(np.random.randint(1, 100, 10))  # ten random ints from 1 to 100
arr = np.arange(25)  # from 0 ot 25
print(are.min())  # argmax and argmin returns index
print(are.argmax())
print(are.argmin())
print(are.max())
print(arr)
print(arr.shape)  # returns shape of the arr
print(arr.dtype)  # returns data type in the array
arr = arr.reshape(5, 5)  # reshapes it into a 5x5 matrix
# from numpy.random import randint then use randit(2, 10) automatically
print(are[8])
print(are[5:])
are[0:5] = 100
print(are)
# numpy array slices do not generate a copy slices make change to the original array
# so be careful while making another array variable with a slice
# and use arr.copy() for making a copy
are_copy = are.copy()
are_copy[:9] = 15
print(are_copy)
print(arr[1][2])
print(arr[1, 2])  # same as the previous line
# grab chunks of the 2d array
array = [[5, 10, 15], [20, 25, 30], [35, 40, 45]]
array = np.array(array)
print(array)
print(array[:2, 1:])  # grab everything until row 2 and from column 1 onwards
are = np.arange(0, 11)
bool_are = are > 5  # this is called conditional selection
print(bool_are)
# now we can use the bool_are to select elements of the are
print(are[bool_are])  # 6 7 8 9 10
print(are[are > 5])  # same thing
arr_2d = np.arange(50).reshape(5, 10)
print(arr_2d)
print(arr_2d[1:3, 3:5])
# array with scalar operations like add, subtract, multiply
print(are + are)
print(are - are)
print(are * are)
print(are)
print(are + 100)
#  numpy doesnt terminate program for 0 divide error, just shows a warning
#  and fills the value with either nan or inf
print(are ** 2)
print(np.sqrt(are))
print(np.max(are))
print(np.sin(are))
print(np.log(are))
print(np.std(are))  # standard deviation
print(np.sum(arr_2d))  # sum of an array
print(arr_2d.sum(axis=0))  # sum of all columns
