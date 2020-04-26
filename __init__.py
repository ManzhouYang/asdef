"""you can learn math, info from wikipedia..., and more very good things...
the module is used and now are im trying to do this to a package, but how...
how should we do a url, webbsite...
when im know how to do a webbsite, so can you go to the webbsite named ..."""

from datetime import date
from time import time, sleep
import webbrowser as w
from random import choice
import turtle as t
import wikipedia

__version__ = '0.0.2'
next_verision = None
MAXPOOWER = 39.99999999999999
MINPOOWER = -39.99999999999999
periodic_table_many = 118

def wikipedia_info(search_for_or_find_for, search_or_find):
    if search_or_find == 'search':
        s = wikipedia.search(search_for_or_find_for)
        print(s)
    elif search_or_find == 'find':
        result = wikipedia.page(search_for_or_find_for)
        print(result.summary)
        
def turtle_circle(radius, color, x, y, shape=None):
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
    t.hideturtle()

def rektangel(width, height, color, x, y, shape=None):
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
    t.hideturtle()

def no_fill_circle(radius, color, x, y, shape=None):
    "WARNING: It can be a bug without i\'m know it, so be careful"
    t.penup()
    t.goto(x, y)
    t.shape(shape)
    t.pendown()
    t.pensize(1)
    t.color(color)
    t.circle(radius)
    t.penup()
    t.hideturtle()

def no_fill_rektangel(width, height, color, x, y, shape=None):
    "WARNING: It can be a bug without i\'m know it, so be careful"
    t.hideturtle()
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

def now():
    now = time()
    print(now)

def use_math(n, q):
    print(n * q)
    print('The sum of these is ' + str(n + q))
    if n > q:
        print('The differens of these is ' + str(n - q))
        print(n / q)
        print('The rest of these is ' + str(n % q))
    else:
        print('The differens of these is ' + str(q - n))
        print(q / n)
        print('The rest of these is ' + str(q % n))
        
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

def do_not_use_this(while_word):
    while True:
        print(while_word)
        svar = input('More? (yes, no): ')
        if svar == 'no':
            break

def open_webb(webb):
    w.open(webb)

class Do_not_know:
    pass

class randoms:
    "a bug is here"
    def random_number2(s, x, y):
        "if you see s, that you give s a number but not in the random"
        ord1 = [x, y]
        ord2 = choice(ord1)
        print(str(ord2))

    def random_not_number2(s, x, y):
        "if you see s, that you give s a number but not in the random"
        wert = [x, y]
        wert2 = choice(wert)
        print(wert2)

    def random_number3(s, x, y, z):
        "if you see s, that you give s a number but not in the random"
        ord3 = [x, y, z]
        ord4 = choice(ord3)
        print(str(ord4))

    def random_number4(s, x, y, z, n):
        "if you see s, that you give s a number but not in the random"
        ord5 = [x, y, z, n]
        ord6 = choice(ord5)
        print(str(ord6))

    def random_number5(s, x, y, z, n, m):
        "if you see s, that you give s a number but not in the random"
        ord7 = [x, y, z, n, m]
        ord8 = choice(ord7)
        print(str(ord8))

    def random_not_number3(s, x, y, z):
        "if you see s, that you give s a number but not in the random"
        wert3 = [x, y, z]
        wert4 = choice(wert3)
        print(wert4)

    def random_not_number4(s, x, y, z, n):
        "if you see s, that you give s a number but not in the random"
        wert5 = [x, y, z, n]
        wert6 = choice(wert5)
        print(wert6)

    def random_not_number5(s, x, y, z, n, m):
        "if you see s, that you give s a number but not in the random"
        wert7 = [x, y, z, n, m]
        wert8 = choice(wert7)
        print(wert8)

    def random_all(no_range, range_no):
        "WARNING: Don\'t use this in range, and use random_not_number"
        "if you see s, that you give s a number but not in the random"
        print('WARNING: Don\'t use this in range, and use random_not_number')
        print(range(0, 11))     # Not work... 
