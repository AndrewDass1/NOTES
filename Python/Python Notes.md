# Python Notes
These notes are taken from the official Python documentation, found here: https://docs.python.org/3/tutorial/interpreter.html <br>

## Chapter 1 
A <b>High-level language</b> contains high-level data types such as arrays and dictionaries <br>
<br>
Modules are files or scripts. These files or scripts can be ran by other files by importing the script's code as a package into another python file. Examples of Modules are: <br>
* I/O
* System Calls
* Sockets
* Interfaces to graphical user interface toolkits like TK

An interpreted language - Save you considerable time during program development because no complilation and linking is necessary <br>
<br>
Python is an interpreted language 


## Chapter 2
Interpreter - Program that converts the code a developer writes into an intermediate language, called byte code. It converts the code line by line, one at a time. It translates till the end and stops at that line where an error occurs, if any, which makes the debugging process easier. <br>
<br>
A reading about the Interpreter Source: https://pythongeeks.org/interpreter-in-python/ <br>
<br>


Note: To use argument passing, use the package "sys" by writing import sys to see what has been declared. Sys is a python package that uses commands that interacts with the interpreter. <br>
A package are many modules <br>
<br>

Steps: <br>
1. Source code -> Interpreter (Compiler + PVM - python virtual machine) converts intermediate code to bytecode
2. Compiler converts the source code for PVM
3. PVM reads and executes the commands


The ">>>" in command prompt means Interactive mode, where it is possible for the command prompt to take an input <br>
Source code encoding - UTF-8 <br>
<br>

## Chapter 3
Numeric Operation Signs or Symbols to use in Python:
1. Comments: Starts with a "#"
```
# Hello! This is a comment.
```
2. Addition: Use the "+" sign to add numbers
```
print(18 + 25)
```
3. Subtraction: Use the "-" sign to subtract numbers
```
print(18 - 25)
```
4. Division: Use the "/" to divide numbers
```
print(19 / 3)
```
5. Floor Division: Use the "//" to divide numbers and receive a whole number value as the ending result 
```
print(19 // 3) #The output will be 6.0
```
6. Multiplication: Use the "*" sign to multiply two numbers
```
print(2 * 6) 
```

An example of using the round function: <br>
round(variable, 2), where 2 - placeholder for decimal places <br>
<br>

Using Single Quotes:
```
' \' ' = single quote or " ' "
```
Using Double Quotes:
```
\" \" = double quote 
```
Using a Raw String: 
```
r"Text"
```

Lists : [] <br>
Indexing: variable_name[position] or variable_name[starting:ending], ex: ending = 7, goes to 6th value. Always goes to position before end <br>
Concatenate_example: list1 + list2 <br>
<br>

More methods: <br>
.append() <br>
len() <br>
<br>

Nested Lists: <br>
list3 = [list1, list2] <br>
list3[0][1] - Example of accessing position in nested list <br>

Make a new line: <br>
new line - \n <br>

## Chapter 4 - More Control Flow Tools
if, elif and else statement structure: <br>
<br>

```
if x < 0:
   print("")
elif x == 0:
   print("")
else:
   print("")
```
   
How to write for statements:
```
for *variable* in words: <br>
   write code here
```
Where words is an already predefined variable that has a lot of elements <br>
<br>

How to use the Range function:
```
range(start, end, increment)
```

Break and Continue keywords are used only in for or while loops. A resource to read more about Breaks: https://www.pythonpool.com/python-break/ <br>
Using the keyword "pass" is a placeholder that will execute in a Python file, but won't make changes to the code <br>
<br>

How to use Match:
```
match ....: <br>
    case number or variable: <br>
        return "" <br>
```
        
How to write and define Functions:
```
def name(*variable1, variable2):
  return("")
```
* name, variable1, and variable2 are placeholder values


## Chapter 5
Make a list variable -> variable_name = [] <br>
<br>

Commands:
1. variable_name.sort() 
2. variable_name.append()
3. variable_name.reverse() or variable_name.pop()
4. del[] - Specify index in list for that element to be deleted
5. Curly brackets: {}, no duplicate elements, no other data types such as []
6. Add elements in sets - variable_name.add() <br>
7. Update/replace elements - variable_name.update(element, new element)
8. Delete elements: var_name.discard() or use remove()
9. pop in sets delete random element
<br>
len, max, min, sum() of sets that use numeric elements <br>
<br>

Dictionaries and Looping Techniques:
```
knights = {'gallahad': 'the pure', 'robin': 'the brave'}
for k, v in knights.items():
   print(k, v)
```
.keys(), .values(), .items() <br>

## Chapter 7
How to Read and Write Files: <br>
f = open('nameoffile', 'w', encoding="utf-8") <br>
<br>
Commands to Read and Write Files: <br>
1. 'r' - read
2. 'w' - write
3. 'a' - append
4. 'r+' - read and write

Json files can be read and written by importing the package by specifying "import json" in the script

## Chapter 9
How to Write Classes: <br>
