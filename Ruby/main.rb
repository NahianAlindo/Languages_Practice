$LOAD_PATH << '.' # just sys.path.append

require 'trig.rb'
require 'moral' # .rb ext not mandatory
require 'support'

$global_var = 10
MR_COUNT = 0
class Customer
  @@no_of_customers = 0 # class var accessible to only one class
  VAR1 = 100 # constant

  def initialize(id, name, addr) # constructor
    @cust_id = id # instance var accessible to one object
    @cust_name = name
    @cust_addr = addr
  end

  # put alias function here
  # This gives alias to methods or global variables. Aliases cannot be defined within the method body. The alias of the method keeps the current definition of the method, even when methods are overridden.    <alias method-name method-name> <alias global-variable-name global-variable-name> e.g. alias foo bar or alias $MATCH $&

  def print_info
    puts "Hello no. #{$global_var}"
    puts "Customer name: #{@cust_name}"
  end

  def test(a1 = 'Ruby', a2 = 'Perl')
    puts "prog lang is #{a1}"
    puts "prog lang is #{a2}"
  end

  def test_return
    i = 100
    j = 200
    k = 300
    [i, j, k]
  end

  def total_no_of_customers
    @@no_of_customers += 1
    puts "total customers #{@@no_of_customers}"
    puts "value of VAR #{VAR1}"
    puts "hi there, it\'s Alindo, #{20 * 60 * 60}"
  end

  def example_arr
    arr = ['fred', 10, 3.14, 'This is string']
    arr.each do |i|
      puts i
    end
  end

  def hash_map
    hsh = colors = { 'red' => 0xf00, 'green' => 0x0f0, 'blue' => 0x00f }
    hsh.each do |key, value|
      print key, ' is ', value, "\n"
    end
  end

  def range_with_last
    (1..5).each do |j|
      puts j
    end
  end

  def range_wo_last
    (1...5).each do |j|
      puts j
    end
  end

  ###############
  def operator_ex
    a = 10
    b = 20
    # a <=> b returns 0 if both are eq, -1 if a>b
    # -1 if a<b
    # 1 == 1.0 returns true
    # 1.eql?(1.0) is false coz 1 1.0 are not of the same data type and value

    # aObj.equal?(aObj) is true coz same obj id
    # aObj.equal?(bObj) is false coz diff obj id
  end
  ###############

  def if_else_method
    x = 0
    if x > 2
      puts 'x is greater than 2'
    elsif (x <= 2) && (x != 0)
      puts 'x is 1'
    else
      puts 'i cannot guess the number'
    end
  end

  def unless_block # executes unless if false
    # opposite of if else
    x = 1
    if x != 2
      puts 'x is not 2' # true so executes
    else
      puts 'x is 2'
    end
  end

  def case_method
    _age = 5
    case _age
    when 0..2
      puts 'baby'
    when 3..6
      puts 'little child'
    end
  end

  def while_method
    i = 0
    num = 5

    while i < num
      puts i.to_s
      i += 1
    end
  end

  def do_while_method
    _i = 0
    _num = 5
    loop do
      puts("inside the loop #{_i}")
      _i += 1
      break unless _i < _num
    end
  end

  def until_loop_method
    # executes if until cond is FALSE
    _i = 0
    _num = 5
    until _i > _num
      _i += 1
      puts("Inside the loop i = #{_i}")
    end
  end

  def for_loop
    (0..5).each do |i|
      print("#{i} ")
    end
  end

  def break_example
    (0..5).each do |i|
      break if i > 2

      puts "value of i is #{i}"
    end
  end

  def next_example
    (0..5).each do |i|
      next if (i >= 2) && (i <= 4)

      puts "value of i is #{i}"
    end
  end

  def redo_example # restarts curr iteration
    (0..5).each do |i|
      if (i >= 2) && (i <= 4)
        puts "redo value of i is #{i}"
        # redo
      end
      puts "value of i is #{i}"
    end
  end

  def retry_example # does not work wo begin-end
    puts 'Iteration'
    raise
  rescue StandardError
    retry
  end

  def private_method # such decl indicate private method
    #   When a method is defined outside of the class definition, the method is marked as private by default. On the other hand, the methods defined in the class definition are marked as public by default. The default visibility and the private mark of the methods can be changed by public or private of the Module.
  end

  def self.return_date; end

  def demo_cehck
    puts((1...10).include?(11).to_s)
  end

  def arr_passing(*test)
    puts "\nhe number of params is #{test.length}"
    (0...test.length).each do |i|
      puts "The params are #{test[i]}"
    end
  end
end

module Foo
  # MR_COUNT = 0
  ::MR_COUNT = 1    # set global count to 1
  MR_COUNT = 2      # set local count to 2
end

class Decade
  include Week # embed module in class
  no_of_yrs = 10
  def no_of_months
    puts Week::FIRST_DAY
    number = 10 * 12
    puts number
  end
end
# mixin for multiple inheritance
module A
  def method_a1; end

  def method_a2; end
end

module B
  def method_b1; end

  def method_b2; end
end

class Sample
  include A
  include B

  def method_s1; end
end

class Box
  @@count = 0 # class var declaration

  BOX_COMPANY = 'TATA Inc'.freeze
  BOXWEIGHT = 10

  # constructor method
  def initialize(w, h)
    @width = w
    @height = h # instance var
    @@count += 1
  end

  def to_s # define to_s method formatter
    "(w:#{@width}, h:#{@height})"
  end

  def setWidth=(value)
    @width = value
  end

  def setHeight=(value)
    @height = value
  end

  def printWidth
    @width
  end

  def printHeight
    @height
  end

  # define private accessor methods
  def getWidth # getter method
    @width
  end

  def getHeight
    @height
  end

  def getW
    @width
  end

  def getH
    @height
  end

  # make private getter private
  def getArea
    # @width * @height # or
    getWidth * getHeight
  end

  private :getWidth, :getHeight # make private accessors
  # instance method by default it is public

  def printArea
    @area = getWidth * getHeight
    puts "Area of the box is: #{@area}"
  end

  protected :printArea

  # operator overloading
  def +(other) # define + to do vector addition
    Box.new(@width + other.getW, @height + other.getH)
  end

  def -@ # Define unary minus for negation
    Box.new(-@width, -@height)
  end

  def *(scalar)
    Box.new(@width * scalar, @height * scalar)
  end

  def self.printCount # class/staticmethod
    puts "Box count is: #{@@count}"
  end
end

# define a child subclass
class BigBox < Box
  # add a new instance method
  def printArea
    @area = @width * @height
    puts "Big box area is: #{@area}"
  end
end

# class C
#   puts "Type fo self = #{self.type}"
#   puts "Name of self = #{self.name}"
# end

# default getter, setter methods
class Greeter
  attr_accessor :name # getter and setter both declared using this
  attr_reader :greeting
  attr_writer :age
end

class MyClass
  def m1; end

  protected

  def m2; end

  private

  def m3; end
end

puts MR_COUNT
puts Foo::MR_COUNT

customer1 = Customer.new('1', 'Nahian', '6/c,10/9mirpur')

customer2 = Customer.new('2', 'Alindo', '6/c,10/9mirpur')

# local var begin with _

# self receiver object of the current method
# nil means undefined
# __FILE__ name of curr src File
# __LINE__ curr line num in the src file
# fixnum vs bignum

# 0377                 # octal
# 0xff                 # hexadecimal
# 0b1011               # binary
# ?a                   # character code for 'a'
# ?\n

# a&b means and
# a|b means binary or
# a^b means binary xor
# ~a means complement

# (a and b), (a or b), not(a)
# (a&&b) true if both are non zero
# (a||b) true if one is non zero
# !a
# ?:
# defined? foo if init local-var else nil

# defined? puts        # => "method"
# defined? puts(bar)   # => nil (bar is not defined here)
# defined? unpack      # => nil (not defined here)
# defined? super     # => "super" (if it can be called)
# defined? super     # => nil (if it cannot be)
# defined? yield    # => "yield" (if there is a block passed)
# defined? yield    # => nil (if there is no block)

# this is a multiline comment

customer1.print_info
customer1.total_no_of_customers
customer2.total_no_of_customers
customer2.print_info

customer1.example_arr
customer1.hash_map
customer1.range_with_last
customer1.range_wo_last
customer1.if_else_method
customer1.unless_block
customer1.case_method
customer1.while_method
customer1.do_while_method
customer1.until_loop_method
customer1.demo_cehck
customer1.for_loop

customer1.break_example
customer1.next_example
customer1.redo_example

# customer1.retry_example

customer1.test # method
customer1.test('C')
customer1.test('C', 'C++')

# ruby returns last instrn value by default

var = customer1.test_return
print var

customer1.arr_passing('Zara', '6', 'F')
Customer.return_date # private class method
# Customer.pt_method #public method error bcoz of convention. private methods can be declared outside class definition

# undef bar cancels method defn.    By using undef and alias, the interface of the class can be modified independently from the superclass, but notice it may be broke programs by the internal method call to self.

def test
  puts "\nYou are in the method"
  yield # replaces statement with argument instruction
  puts 'You are again back to the method'
  yield
end

test { puts 'You are in the block' }

### yield use case : when we have no specific method to name it
def test_yield_2
  yield 5
  puts 'you are in the method test'
  yield 100
end

test_yield_2 { |i| puts "You are in the block #{i}" }

y = Trig.sin(Trig::PI / 4)
wrongdoing = Moral.sin(Moral::VERY_BAD)

# embedding module in class
d1 = Decade.new
puts Week::FIRST_DAY
Week.weeks_in_month
Week.weeks_in_year
d1.no_of_months

# multiple inhrtnce mixin

samp = Sample.new
samp.method_a1
samp.method_b1
samp.method_s1

names = Array.new(20)
puts "sizeof arr is #{names.size}"
puts "len arr is #{names.length}"

# assign the same thing to the whole array, init with a value

nums = Array.new(4, 'mac')

puts "arr is #{nums}"

# create arr even nums
nums = Array.new(10) { |e| e *= 2 }
puts nums.to_s

nums = Array.[](1, 2, 3, 4, 5)
nums = Array[1, 2, 3, 4, 5]
puts nums.to_s

digits = Array(0..9) # arr in range
puts digits.to_s
num = digits.at(6) # at index 6
puts num.to_s

# pack() is a Array class method which returns the contents of arr into a binary sequence according to the directives in aTemplateString

# Hashes
months = {} # empty hash map
months = Hash.new 'month' # hash map with defined default value

puts "hash map value for key is: #{months[0]}" # returns default hash map value for any key

H = Hash['a' => 100, 'b' => 200]

puts "#hash values: #{H['a']} #{H['b']}"

H = Hash['January' => [1, 'jan']]
puts (H['January']).to_s

puts "#{H.keys}: values: #{H.values}"
myStr = String.new('THIS IS TEST')
foo = myStr.downcase
print(foo.capitalize)
print(foo)
# use clone to copy arrays

range1 = (1..10).to_a # conv range to list
puts(range1)
range2 = ('bar'..'bat').to_a
puts(range2)

# range operations
digits = 0..9
puts digits.include?(5) # returns true
ret = digits.min
puts "min digit is #{ret}"
ret = digits.max
puts "max digit is #{ret}"

ret = digits.reject { |i| i < 5 }
puts "not rejected values are: #{ret}"

score = 70
result = case score
         when 0.40 then 'Fail'
         when 41..75 then 'Passed'
         end
puts result

puts '5 lies in (1..10)' if (1..10).include?(5) # triple equals

puts 'Enter a value'
val = gets
puts val

str = 'Hello Ruby'
putc str

aFile = File.new('yo.txt', 'w')
aFile.close

File.open('input.txt', 'w') do |aFile|
end

# write file
aFile = File.new('input.txt', 'r+')
if aFile
  aFile.syswrite('ABCDEF')
else
  puts 'Unable to open file!'
end

# read lines of a file
arr = IO.readlines('input.txt')
puts arr[0]

# read file failure
aFile = File.new('input.txt', 'r')

if aFile
  content = aFile.sysread(20)
  puts content
else
  puts 'unable to open file'
end

# rename file
File.rename('input.txt', 'input1.txt')

# Delete file test2.txt
File.delete('yo.txt')

# change permission
file = File.new('test.txt', 'w')
file.chmod(0o755)

# file inquiry
File.open('file.rb') if File.exist?('file.rb')
# if file is really a file
puts File.file?('input1.txt')

puts File.readable?('test.txt')   # => true
puts File.writable?('test.txt')   # => true
puts File.executable?('test.txt') # => false

# file has zero size or not
puts File.zero?('test.txt') # => true

# find type of file
puts File.ftype('test.txt') # => file

# file creation, modified and last access time

puts File.ctime('test.txt')
puts File.mtime('test.txt')
puts File.atime('test.txt')

puts Dir.chdir('/home/runner')
puts Dir.pwd
puts Dir.entries('/usr/bin').join(' ')
puts Dir.chdir('/home/runner/rubypractice')
puts Dir.pwd

Dir.mkdir('mynewdir', 755)
Dir.delete('mynewdir')

# use OOP Concepts

box = Box.new(10, 20)
puts box.printWidth
puts box.printHeight

x = box.getW
y = box.getH

puts x
puts y

puts box.getArea
Box.printCount

puts "String representation of box is: #{box}"

box2 = BigBox.new(10, 20)
box2.printArea

puts box + box2 # operator overloading

# # let us freez this object
# box.freeze
# if( box.frozen? )
#    puts "Box object is frozen object"
# else
#    puts "Box object is normal object"
# end

# # now try using setter methods
# box.setWidth = 30
# box.setHeight = 50

puts Box::BOX_COMPANY # Class constants are inherited and can be overridden like instance methods.

begin
  file = open('python.rb')
  puts 'File opened successfully' if file
rescue StandardError
  file = STDIN
end

print file, '==', STDIN, "\n"

begin
  file = open('python.rb')
  puts 'opened successfully' if file
rescue StandardError # except
  fname = 'input1.txt'
  # puts fname
  # retry
end

# exception handling
begin
  raise 'A test exception'
rescue Exception => e
  puts e.message
  puts e.backtrace.inspect
else
  puts 'Congratulations-- no errors!'

# you may have a file open on entry to the block and you need to make sure it gets closed as the block exits.

# The ensure clause does just this. ensure goes after the last rescue clause and contains a chunk of code that will always be executed as the block terminates.
ensure
  puts 'Ensuring execution'
end

# catch throw to get out of nested errors and execute as before
def promptAndGet(prompt)
  print prompt
  res = readline.chomp
  throw :quitRequested if res == '!'
  res
end

catch :quitRequested do
  name = promptAndGet('Name: ')
  age = promptAndGet('Age: ')
  sex = promptAndGet('Sex: ')
  # ..
  # process information
end
promptAndGet('Name:')

class FileSaveError < StandardError
  attr_reader :reason
  def initialize(reason)
    @reason = reason
  end
end

File.open('input1.txt', 'w') do |_file|
  begin
  # Write out the data ...
  rescue StandardError
    # Something went wrong!
    raise FileSaveError, $!
  end
end

# appnend to an aray
people = %w[alindo omio alvee mahdee]
ages = []
people.each do |_person|
  ages << 0 # appending using <<
end
puts "ages: #{ages}"

line = 'Perl'
# regex
puts 'There seems to be another lang here' if line =~ /P(erl|ython)/

if line =~ /ab+c/ # means a, more than 0 b's and c | also /ab*c/ means a, 0 or more b's and c
  puts 'There seems to be another lang here'
end
# \d -> digit
# \s -> whitespace
# \w -> alphanumeric character
# \A -> beginning of the String
# \z -> matches end of the string
# \., -> matches characters as is
# %r{}i i means ruby regex case insensitive

animals = %w[ant bee cat dog elk]
animals.each { |animal| puts animal }

3.times { print 'No! ' }

box3 = Box.allocate # create uninit not constructored obj
puts box3.getArea

# a || b means if not false or nil returns a otherwise returns b

# a ||= b means a = a || b
# a ||= b is a conditional assignment operator. It means:

# if a is undefined or falsey, then evaluate b and set a to the result.
# Otherwise (if a is defined and evaluates to truthy), then b is not evaluated, and no assignment takes place.

# obj = self.new # creates instance from a class method

# class Person < ApplicationRecord
#   def self.for_dave
#     Person.new(name: 'Dave')
#   end
# end
#
# class Employee < Person
# ..
# end
# dave = Employee.for_dave
#
# The for_dave() method was hardwired to return a Person object, so that’s
# what’s returned by Employee.for_dave .
# returns a Person
#
# require File.expand_path('../../config/environment', __FILE__)
#
#
# lambda
# The lambda operator converts a block into an object of type Proc . An alter-
# native syntax, introduced in Ruby 1.9, is ->
