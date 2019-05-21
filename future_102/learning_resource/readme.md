# Python Functions [draft: 5/20/19]

Functions are a way to organize code into reusable blocks of code. They are easy to implement, yet flexible and powerful.

## Today we are going to:

* Introduce functions
* Anatomy of a function
* Our first basic function
* Exorcises

---

### Introduction

We already have used some of python's **built-in** functions, such as:

* `print()` At it's most basic level allows us to print to scree
* `str()` Allows to set the Type of an object to a string

We know if we **"call"** the print function and **"pass"** a string, "Hello world", as an **"argument"**, when the program executes it will print what ever we wrote to the screen.

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
>>> print(type(int(1)))
<class 'int'>
```

So far using functions, has been like magic. We pass an **argument** and it `returns` the results.

The python core developers wrote the **built-in** functions, we can get a list of all the built-in functions from the Python [documentation](https://docs.python.org/3/library/functions.html) but we can write our own function too, making python even more flexible and powerful

> Python was written with the idea of being modular, as a matter of fact all scripts in Python are considered 'modules'. Allowing programming to write small peaces of codes, and call them when we need them, calling chunks of code we had previously written into new scripts, just like we can call the `print()` function

---

#### Anatomy of a function

So far we understand the idea of using the built-in functions, there are repetitive tasks we would like to call and reuse with out coping and pasting all over our scripts.

For example we may have a block of sequential code that we would like to reuse and call it when we need it. 

We may want to print to screen a string with a line above and bellow to bring attention to it

```text
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
welcome to my house, take your shoes off
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
```

Sequentially we might do something like this, but every time we want to use this block of code, we have to copy it and past it where we what to use it.

if we use it in different parts of our script it would become very difficult to maintain, as we have to update all the instances of our block of code.

```python
my_string = 'welcome to my house, take your shoes off'
print('~' * len(my_string))
print('my_string')
print('~' * len(my_string))
```
---

#### Our first basic function

What if we turn it into a function and we can call it from any where in our script.

There are some simple steps we have to take to turn our block of code into a function.

```python
my_string = 'Help me write a function'
def header():
    print('~' * len(my_string))
    print('my_string')
    print('~' * len(my_string))
```

---
[ ] Explain the function format

---

We can now call our function header from any place in the script, even from other script and it will execute the indented chunk of code.

We call it our function like any other function. In this particular case the print statements are with the function, so all we have to do is call it, and it will print to screen automatically.

```python
>>> header()
~~~~~~~~~~~~~~~~~~~~~~~~
Help me write a function
~~~~~~~~~~~~~~~~~~~~~~~~
```

In this particular case is taking the variable `my_string` to generate the formatting and print the message.

We can make it more flexible if we could use it like the `print()` function, where we give it the message and it does the rest.

We can, by modifying it and passing the string as an `argument`

```python
def header(message):
    print('~' * len(message))
    print(message)
    print('~' * len(message))
```

We are passing an argument as 'message', so what ever string we pass as an argument will be used to format the string

```python
header('Welcome to my card game')
```

Now the result would look like this:

```cmd
~~~~~~~~~~~~~~~~~~~~~~~
Welcome to my card game
~~~~~~~~~~~~~~~~~~~~~~~
```

Having turned your block of code into a function, give you a few advantages.

* Centralized code, easy to maintained
* Modify once
* call it from anywhere, even from other scripts

Functions are really powerful and offer enormous legibilities.

---

#### Exorcises

---
[ ]  List some exorcises

---