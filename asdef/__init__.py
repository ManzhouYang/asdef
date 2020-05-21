"""this is a example package that im ..."""

from datetime import date
from math import pi
import webbrowser as w
from random import choice
import turtle as t
import wikipedia      # You must install wikipedia before you're useing wikipedia_info

__version__ = '0.0.5'
MAXPOOWER = 39.99999999999999
MINPOOWER = -39.99999999999999
periodic_table_many = 118

def CircleArea(radius):
    print('Area:', str(pi*radius**2))

def GlobeVolume(radius):
    print('Volume:', str(4/3*pi*radius**3))

def CircleCircumference(radius):
    print('Circumference:', str(pi*2*radius))

def GlobeArea(radius):
    print('Area:', str(4*pi*radius**2))

def Not_use_this(url):
    "this is done with: while True: w(webbrowser).open(url)"
    while True: w.open(url)

def wikipedia_info(search_or_find_for, search_or_find):
    if search_or_find == 'search':
        s = wikipedia.search(search_or_find_for)
        print(s)
    elif search_or_find == 'find':
        result = wikipedia.page(search_or_find_for)
        print(result.summary)
        
def turtle_circle(radius, color, x, y, shape=None, hideturtle=True):
    "WARNING: It can be a bug without i\'m know it, so be careful"
    t.penup()
    t.goto(x, y)
    t.shape(shape)
    t.pendown()
    t.pensize(1)
    t.color(color)
    t.begin_fill()
    t.circle(radius)
    t.end_fill()
    t.penup()
    if hideturtle is True:
        t.hideturtle()

def rektangel(width, height, color, x, y, shape=None, hideturtle=True):
    "WARNING: It can be a bug without i\'m know it, so be careful"
    t.penup()
    t.goto(x, y)
    t.shape(shape)
    t.pendown()
    t.pensize(1)
    t.color(color)
    t.begin_fill()
    for raknare in range(1, 3):
        t.forward(width)
        t.right(90)
        t.forward(height)
        t.right(90)
    t.end_fill()
    t.penup()
    if hideturtle is True:
        t.hideturtle()

class prime:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def primes_number(start, end):
        for n in range(start, end):
            for x in range(2, n):
                if n % x == 0:
                    print(n, 'equals', x, '*', n//x)
                    break
            else:
                # loop fell through without finding a factor
                if (int(number) != 0) and (int(number) != 1):
                    print(number, 'is a prime number')
                else:
                    print(number, 'is not a prime number or a composite number')
    def primes_number2(number):
        for x in range(2, number):
            if (int(number) == 0) or (int(number) == 1):
                break
            if number % x == 0:
                print(number, 'equals', x, '*', number//x)
                break
        else:
            # loop fell through without finding a factor
            if (int(number) != 0) and (int(number) != 1):
                print(number, 'is a prime number')
            else:
                print(number, 'is not a prime number or a composite number')

def no_fill_circle(radius, color, x, y, shape=None, hideturtle=True):
    "WARNING: It can be a bug without i\'m know it, so be careful"
    t.penup()
    t.goto(x, y)
    t.shape(shape)
    t.pendown()
    t.pensize(1)
    t.color(color)
    t.circle(radius)
    t.penup()
    if hideturtle is True:
        t.hideturtle()

def no_fill_rektangel(width, height, color, x, y, shape=None, hideturtle=True):
    "WARNING: It can be a bug without i\'m know it, so be careful"
    t.penup()
    t.goto(x, y)
    t.shape(shape)
    t.pendown()
    t.pensize(1)
    t.color(color)
    t.begin_fill()
    for raknare in range(1, 3):
        t.forward(width)
        t.right(90)
        t.forward(height)
        t.right(90)
    t.end_fill()
    t.penup()
    if hideturtle is True:
        t.hideturtle()

def use_math(n, q):
    print('The product of these is: ' + str(n * q))
    print('The sum of these is ' + str(n + q))
    if n > q:
        print('The differens of these is ' + str(n - q))
        print(n / q)
        print('The rest of these is ' + str(n % q))
    else:
        print('The differens of these is ' + str(q - n))
        print(q / n)
        print('The rest of these is ' + str(q % n))
        
def fib(end_n):    # write Fibonacci series up to end_n
    a, b = 0, 1
    while a < end_n:
        print(a, end=' ')
        a, b = b, a+b
    print()
def fib2(end_n):  # return Fibonacci series up to end_n
    result = []
    a, b = 0, 1
    while a < end_n:
        result.append(a)    # see below
        a, b = b, a+b
    return result
def fab(end_n):
    a, b = 0, 1
    while a < end_n:
        print(a)
        a, b = b, a+b
    print()
def feb(numbers):
    "it starts with 0, 1"
    a, b = 0, 1
    for i in range(0, numbers):
        print(a)
        a, b = b, a+b

def cheeseshop(kind, *arguments, **keywords):
    print("-- Do you have any", kind, "?")
    kind1 = "-- I'm sorry, we're all out of " + kind
    kind2 = "-- Here you are your " + kind
    both = [kind1, kind2]
    ct =  choice(both)
    print(ct)
    for arg in arguments:
        print(arg)
    print("-" * 40)
    for kw in keywords:
        print(kw, ":", keywords[kw])

def poower(d, a):
    if (d < 40 and a < 40) and (d > -40 and a > -40):
        print(d ** a)
        print(a ** d)
    elif d <= MINPOOWER or a <= MINPOOWER:
        print('It\'s to small.')
    else:
        print('It\'s to big.')

def big(x, y, z, n, m, e):
    print('The biggest number is ' + str(max(x, y, z, n, m, e)))


def small(x, y, z, n, m, e):
    print('The smallest number is ' + str(min(x, y, z, n, m, e)))

def secretry(password):
    print('your new password is: ' + ''.join(reversed(password)))
    answer = input('(yes or no)Even better? Write it here: ')
    if answer == 'yes':
        pass

def sec_on_days(days):
    hours = days * 24
    minuts = hours * 60
    seconds = minuts * 60
    if days != 1:
        print('They are ' + str(seconds) + ' seconds on ' + str(days) + ' days.')
    else:
        print('They are 86400 seconds on one day.')

def min_on_days(days):
    hours = days * 24
    minuts = hours * 60
    if days != 1:
        print('They are ' + str(minuts) + ' minuts on ' + str(days) + ' days.')
    else:
        print('They are 1440 minuts on one day.') 

def sec_on_weeks(weeks):
    days = weeks * 7
    hours = days * 24
    minuts = hours * 60
    seconds = minuts * 60
    
    print('They are ' + str(seconds) + ' seconds on ' + str(weeks) + ' weeks.')

def min_on_weeks(weeks):
    days = weeks * 7
    hours = days * 24
    minuts = hours * 60
    print('They are ' + str(minuts) + ' minuts on ' + str(weeks) + ' weeks.')

def wekday(year, month, day):
    if date(year, month, day).weekday() == 0:
        print('Monday')
    elif date(year, month, day).weekday() == 1:
        print('Tuesday')
    elif date(year, month, day).weekday() == 2:
        print('Wednesday')
    elif date(year, month, day).weekday() == 3:
        print('Thurday')
    elif date(year, month, day).weekday() == 4:
        print('Friday')
    elif date(year, month, day).weekday() == 5:
        print('Saturday')
    else:
        print('Sunday')

def whileee(while_word):
    while True:
        print(while_word)
        svar = input('More? (yes, no): ')
        if svar == 'no':
            break


def open_webb(webb):
    w.open(webb)

def random_number3(x, y, z):
    ord3 = [x, y, z]
    ord4 = choice(ord3)
    print(str(ord4))

def random_number4(x, y, z, n):
    ord5 = [x, y, z, n]
    ord6 = choice(ord5)
    print(str(ord6))

def random_not_number3(x, y, z):
    wert3 = [x, y, z]
    wert4 = choice(wert3)
    print(wert4)

def random_not_number4(s, x, y, z, n):
    "if you see s, that you give s a number but not in the random"
    wert5 = [x, y, z, n]
    wert6 = choice(wert5)
    print(wert6)

def random_all():
    "WARNING: Don\'t use this in range, and use random_not_number"
    "if you see s, that you give s a number but not in the random"
    print('WARNING: Don\'t use this in range, and use random_not_number')
