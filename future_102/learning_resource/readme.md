# Introduction to Python Functions

- [Introduction to Python Functions](#introduction-to-python-functions)
  - [Introduction](#introduction)
  - [Anatomy of a function](#anatomy-of-a-function)
    - [Function structure](#function-structure)
      - [Defining our function](#defining-our-function)
      - [Function indentation formatting](#function-indentation-formatting)
      - [Function docstring](#function-docstring)
      - [Function code block](#function-code-block)
      - [Return the function value/s](#return-the-function-values)
    - [Our first basic function](#our-first-basic-function)
      - [Parameters and arguments in functions](#parameters-and-arguments-in-functions)
        - [Positional function parameters](#positional-function-parameters)
    - [Exorcises](#exorcises)

Functions are a way to organize code into reusable blocks of code. They are easy to implement, yet flexible and powerful.

---

## Introduction

We already have used some of python's **built-in** functions, such as:

- `print()` At it's most basic level allows us to print to scree
- `str()` Allows to set the Type of an object to a string

We know if we **"call"** the print function and **"pass"** a string, "Hello world", as an **"parameter"**, when the program executes it will print what ever we wrote to the screen.

```python
>>> print('Hello world')
Hello world
```

For example we can change the **type** of an **integer** with the built in function `str()` function.

```python
>>> str(1)
```

we can combine functions to make them more powerful

```python
>>> print(type(1))
<class 'int'>
>>> print(type(str(1)))
<class 'str'>
>>>
```

Using functions, has been like magic. We pass an **parameter** and it `returns` the results.

The python core development team wrote all the **built-in** functions, we can get a list of all the built-in functions from the Python [documentation](https://docs.python.org/3/library/functions.html). We can also **write our own function,** making python even more flexible and powerful

> Python was written with the idea of being modular, as a matter of fact all scripts in Python are considered 'modules'. Allowing programmers to write small pieces of code, and call them when we need them. Calling chunks of code we had previously written into new scripts, just like we can call the `print()` function

---

## Anatomy of a function

So far we understand the idea of using the built-in functions, there are repetitive tasks we would like to call and reuse with out copying and pasting all over our scripts.

For example we may have a block of sequential code that we would like to reuse and call it when we need it.

We may want to print to screen a string with a line above and below to bring attention to it

```text
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
welcome to my house, take your shoes off
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
```

Sequentially we might do something like this, but every time we want to use this block of code, we have to copy it and past it where we want to use it.

```python
my_string = 'welcome to my house, take your shoes off'

print('~' * len(my_string))
print('my_string')
print('~' * len(my_string))
```

if we use it in different parts of our script it would become very difficult to maintain, as we have to update all the instances of our code block.

By turning our code block into a function, we add flexibility to the use and maintenance of our code

---

### Function structure

Lets brake down the structure of a function and learn how to write one.

#### Defining our function

We first have to define a function, with a keyword and name

```python
def function_name():
```

1. First we need to define a function by using the keyword
   1. `def`
2. Add space and enter a function name
   1. `def function_name`
3. We need to follow the function name with parenthesis
   1. `def function_name()`
4. We must end the definition line with **colon**
   1. `def function_name():`

---

#### Function indentation formatting

we let python know which code belongs to a particular function, by indenting it below the function definition.

```txt
# code does not belong to function

def function_name([parameter], [parameter]):
    statements
    statements
    [return result]

# code does not belong to function above
```

Now, we know the proper function indentation format, lets continue with our function.

---

#### Function docstring

Right below the function definition we begin with our docstring

A docstring is a string literal that occurs as the first statement in a module, function, class, or method definition. Such a docstring becomes the `__doc__` special attribute of that object.

- It is intended as formated documentation for that module, function, class or method.
- Useful as we read a program and try to understand it or remember what we wrote.
- Useful if we import a script into another script to make use of a particular function, as code editors can display the docstring of the function you are about to import

```python
def function_name():
    """ DocString, write a brief description of your function"""
```

1. Right below the definition, indent your code
2. With-in triple quotes enter your docstring

> "A universal convention supplies all of maintainability, clarity, consistency, and a foundation for good programming habits too. What it doesn't do is insist that you follow it against your will. That's Python!"
> 
> —Tim Peters on comp.lang.python, 2001-06-16

---

#### Function code block

We have defined and docstring our function, now we have to write the logic that our function will execute.

```python
def function_name():
    """ DocString, write a brief description of your function"""
    a = n1
    b = n2
    c = a + b
```

- Write each line of your function code, starting with indentation

> If we *call the function* in the example above and assign it to a variable we **would not** get anything in **return.**

---

#### Return the function value/s

In order to get the result from our function, we must tell the function what to return by using the keyword `return`

```python
def function_name():
    """ DocString, write a brief description of your function"""
    a = n1
    b = n2
    c = a + b
    return c
```

- In the last line of our function, type the keyword `return` followed by the value to return. Now if you assign your function to a variable it will return a value that can be used for other operations

>Note that a function can execute other functions, and code which will cause your application to do something with out having to use the keyword `return`. We will see an example below.

---

### Our first basic function

What if we turn our sequential code into a function, then we can call it from anywhere in our script.

There are some simple steps we have to take to turn our block of code into a function.

```python
my_string = 'Help me write a function'

def header():
    """ DocString: write a brief description """
    print('~' * len(my_string))
    print('my_string')
    print('~' * len(my_string))
```

Now that we know how a function is made. We can call our function, `header()`, from any place in the script, even from other scripts and it will execute the indented code block.

We call our function like any other function. In this particular case the print statements are within the function, so all we have to do is call it, and it will print to screen automatically.

```python
>>> header()
~~~~~~~~~~~~~~~~~~~~~~~~
Help me write a function
~~~~~~~~~~~~~~~~~~~~~~~~
```

In this particular case is taking the variable `my_string` to generate the formatting and print the message.

---

#### Parameters and arguments in functions

We can make our function more flexible if we could use it like the `print()` function, where we pass the message and it does the rest.

In python you can pass parameters and arguments to a function. You can pass any number of parameters to a function, they are just variables. You can also pass three types of arguments, the **default** argument, **key** argument and **arbitrary** argument.

In this lesson we will introduce the **positional parameter**

---

##### Positional function parameters

Positional parameters are the most commonly use in functions, so this is where we are going to start, in later lesson we will cover the other types of parameters and arguments.

A function can take any number of **parameters,** you just have to separate them with comas. `def function(parm, param2):`

> It is important to note, you must pass the values of the parameters in the correct order, hence the name positional. You can even pass other functions as parameters.

But lets start by passing a **single positional parameter.**

1. Add an parameter name, `message`, inside the parenthesis of our function definition.

2. Assign that parameter name to all the operations that need to make use of it.

```python
def header(message):
    print('~' * len(message))
    print(message)
    print('~' * len(message))
```

We are passing a parameter as 'message', so what ever string we pass as parameter will be used to format the string. 

- Lets call our function with the positional parameter in it
- Note, we could assign the string to a variable and pass that variable as the parameter

```python
>>> header('Welcome to my card game')
```

Now the `header()` function will return the following:

```cmd
~~~~~~~~~~~~~~~~~~~~~~~
Welcome to my card game
~~~~~~~~~~~~~~~~~~~~~~~
```

Having turned your code block into a function, give you a few advantages.

- Centralized code
- Modify once, easy to maintained
- Call it from anywhere, even from other scripts

Functions are really powerful and offer enormous flexibility.

---

### Exorcises

Write a function to do the following. You may want to write the sequential code, then you can turn your code block into a function.

- [ ] Find the Max of three numbers.
- [ ] Sum all the numbers in a list.
- [ ] Multiply all the numbers in a list.
- [ ] Reverse a string.
- [ ] Accepts a string and calculate the number of upper case letters and lower case letters.
