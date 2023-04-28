#!/usr/bin/env python
# coding: utf-8

# ### Very basic Python Concepts
# #### To run the cells, click on the code that you want to run and press (Shift + Enter)
# #### If there are some other basic concepts that you think I should add, please feel free to comment on Github and I will add an example to the document.

# #### Variables

# In[ ]:


# Variables
x,y,z = (1,2,3) # The variables are x,y,z, while 1,2,3 are the values.
print(x)
print(y)
print(z)


# #### For Loop Example

# In[ ]:


#for loop Example 1
exampleList = [1,2,3,4,5,6,7,8,9]; # Lists are denoted by square brackets [] and are mutable/changable.

for each_number in exampleList: # each_number becomes a new variable
    print(eachNumber)


# ##### Example #2

# In[ ]:


#for loop Example 2, Python will stop before reaching 11 so it will only print out to 10
for x in range(1,11):
    print(x)


# #### While Loop

# In[ ]:


# while loop example
condition = 1;
while condition < 10:
    print(condition)
    condition += 1 # +- is useful because it will be iterative and add 1 until the condition is met


# #### If Statements

# In[ ]:


# if statement example
x = 5
y = 8
z = 5

if z < y > x:
    print('y is greater than z and greater than x')
if z <= x:
    print('z is less than or equal to x')
if z != y:
    print('z is not equal to y')


# #### If, elif, and else example

# In[ ]:


# if, elif, and else example
x = 5
y = 10
z = 22

if x > y:
    print('x is greater than y')
elif x < z:
    print('x is less than z')
else:
    print('The if and elif(s) statements did not run')


# #### Simple Functions

# In[ ]:


# Simple Functions example
def py_example ():
    z = 3 + 9
    print (z)

py_example()


# In[ ]:


# Simple function with parameters
def simple_addition(num1,num2):
    answer = num1 + num2
    print('The answer is', answer)

simple_addition(2,5)


# #### Function paramters ()

# In[ ]:


# Default function parameters
def simple(num1,num2):
    pass # pass just allows the function to pass

def simple5(num1,num2 = 5):
    print(num1,num2)

simple(4,5) #Nothing will happen
simple5(1) # shows num1 and num2 which is set to 5 so it will print 1 5
simple5(1, 20) #But the default paramter can be overwritten if given an input


# #### Global and local variables

# In[ ]:


# Global and local variables
# X is a local variable and will cause an error if you try to add to it within the definition
x = 6

def example():
    print(x)
    print(x+5)
    x += 1 # This will cause an error because it is calling on the non-existant local variable
example() # Running this command will receive an error "UnboundLocalError: local variable 'x' referenced before assignment"


# In[ ]:


# To make it a global varaible you have to include it in the definition, but not the best practice to do so

x = 2

def example():
    global x
    print(x)
    x+=5
    print(x)
example()


# In[ ]:


# This is a way to bypass using a global variable

x = 6

def example():
    globx = x
    print(globx)
    globx += 5
    print(globx)
    return globx

x = example()


# #### Writing to a file

# In[ ]:


# Write to a file, it will overwrite previous file
text = 'Sample text'
saveFile = open('exampleFile.txt','w') # r = read, w = write, a = append
saveFile.write(text)
saveFile.close() # It is extremely important to close the scipt


# #### Appending a file

# In[ ]:


# Appending a file
appendMe = '\nNew bit of information' #"\n" adds a new line
appendFile = open('exampleFile.txt','a')
appendFile.write(appendMe)
appendFile.close()


# #### Reading a file

# In[ ]:


# Read a file
# You can also make a list
readMe = open('exampleFile.txt','r').read()
print(readMe)

# you can also read a list
readMe = open('exampleFile.txt','r').readlines()
print(readMe)


# #### Classes

# In[ ]:


# Basic  Classes Example, Grouping definitions together
class calculator:
    def addition(x,y):
        added = x + y
        print(added)
    def subtraction(x,y):
        subtracted = x - y
        print(subtracted)
    def multiplication(x,y):
        mult = x * y
        print(mult)
    def division(x,y):
        div = x / y
        print(div)

calculator.multiplication(3,5)


# #### Inputs

# In[ ]:


# Simple input
x = input('What is your name? ')
print('Hello', x)


# #### Importing Modules

# In[ ]:


# Module example
import statistics
example_list = [2,3,4,7,16,6,3,3,6,6,3,6,1,2,7,1];
x = statistics.mean(example_list)
print(x)
y = statistics.median(example_list)
print(y)
z = statistics.stdev(example_list)
print(z)
v = statistics.variance(example_list)
print(v)


# In[ ]:


# Syntax examples
import statistics as stat
example_list = [2,3,4,7,16,6,3,3,6,6,3,6,1,2,7,1];
x = stat.variance(example_list)
print(x)


# In[ ]:


# You can import modules directly for even shorter line
from statistics import variance, mean
example_list = [2,3,4,7,16,6,3,3,6,6,3,6,1,2,7,1];
x = variance(example_list)
y = mean(example_list)
print(x,y)


# In[2]:


# It is a good idea to close/exit out of a program when done so uncomment the exit() when done by deleting the #
# exit()

