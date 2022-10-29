# Python Notes

These notes are taken from the official Python documentation, found here: https://docs.python.org/3/tutorial/interpreter.html <br>
<br>

## Chapter 1 
A <b>High-level language</b> contains high-level data types such as arrays and dictionaries <br>
<br>
Modules: <br>
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
A module is any file while a package are many modules <br>
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
1. # -> Comments
2. + -> addition
3. - -> subtraction
4. / -> division
5. // -> floor division
6. * -> multiplication

An example of using the round function: <br>
round(variable, 2), where 2 - placeholder for decimal places <br>
<br>

Using Quotes <br>
' \' ' = single quote or " ' " <br>
\" \" = double quote <br>
<br>
Raw String: r'' <br>
<br>

Lists : [] <br>
<br>

Indexing: variable_name[position] or variable_name[starting:ending], ex: ending = 7, goes to 6th value. Always goes to position before end <br>
<br>

Concatenate: list1 + list2 <br>
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
if ,elif and else statement structure: <br>
<br>

```
if x < 0:
   print("")
elif x == 0:
   print()
else:
   print()
```
   
How to write for statements: <br>
for *variable* in words: <br>
* where words is an already predefined variable that has a lot of elements <br>
<br>

Range function: <br>
range(start, end, increment) <br>
<br>

Break and Continue: <br>
Used only in for or while loops <br>
<br>

A resource to read more about Breaks: https://www.pythonpool.com/python-break/ <br>
<br>
Using the keyword "pass" is a placeholder that will execute in a Python file, but won't make changes to the code <br>
<br>

How to use Match: <br>
match ....: <br>
    case number or variable: <br>
        return "" <br>
        
Functions <br>
Define the function: <br>
def name(*variable1, variable2): <br>
  code... <br>
<br>

Running the Function <br>
name() <br>


## Chapter 5
Make a list variable -> variable_name = [] <br>
<br>

Commands:
print - variable_name.sort() or variable_name.append() <br>
or variable_name.reverse() or variable_name.pop() <br>
<br>
Have a list, use the del[] command, specify index in [] <br>
Can use slicing <br>
<br>

Curly brackets: {}, no duplicate elements, no other data types such as [] <br>
Add elements in sets - variable_name.add() <br>
Update/replace elements - variable_name.update(element, new element) <br>
Delete elements: var_name.discard() or use remove() <br>
pop in sets delete random element <br>
<br>
len, max, min, sum() of sets that use numeric elements <br>
<br>

Dictionaries and Looping Techniques: <br>
knights = {'gallahad': 'the pure', 'robin': 'the brave'} <br>
for k, v in knights.items(): <br>
   print(k, v) <br>
<br>
.keys(), .values(), .items() <br>

6. Modules
Scripts, make the file/script then import it in another python file <br>

7. Input and Output <br>
f strings, format, {variable:.3f} <br>
where :.3f is 3 decimal places, .4f - 4 decimal places <br>
<br>

7.2 Read and Write Files <br>
f = open('nameoffile', 'w', encoding="utf-8") <br>
<br>
Commands to Read and Write Files: <br>
1. 'r' - read
2. 'w' - write
3. 'a' - append
4. 'r+' - read and write

Json files can be read and written by importing the package by specifying "import json" in the script

8. Errors and Exceptions

9. Classes
