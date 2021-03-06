from __future__ import print_function # must be first in file 
import random
def food_id(food):
    ''' Returns categorization of food
    
    food is a string
    returns a string of categories
    '''
    # The data
    fruits = ['apple', 'banana', 'orange']
    citrus = ['orange']
    starchy = ['banana', 'potato']
    
     # Check the category and report
    if food in fruits:
        if food in citrus:
            return 'Citrus, Fruit'        
        else:
            return 'NOT Citrus, Fruit'
    else:
        if food in starchy:
            return 'Starchy, NOT Fruit'
        else:
            return 'NOT Starchy, NOT Fruit'

def food_id_test():
    ''' Unit test for food_id
    returns True if good, returns False and prints error if not    
    good
    '''
    works = True
    if food_id('orange') != 'Citrus, Fruit':
        works = False
        print('orange bug in food id()')
    if food_id('banana') != 'NOT Citrus, Fruit':
        works = False
        print('banana bug in food_id()') 
    # Add tests so that all lines of code are visited during test 
    if works:
        print('food_id passed all tests')
    return works
def f(n):
    if int(n) == n:
        if n % 2 == 0:
            if n % 3 == 0:
                print(' n is a multiple of 6')
            else:
                print(' n is even')
        else:
            print(' n is odd')
    else:
        print('n it not an interger')
def guess_once():
    secret = random.randint(1, 4)
    print('I have a number between 1 and 4.')
    guess = int(raw_input('Guess: '))
    if guess != secret:
        print('Wrong, my number is ', secret, '.', sep='')
    else:
        print('Right, my number is', guess, end='!\n')

def quiz_decimal(low, high):
    print('Type a number between' , low, 'and' , high)
    number = float(raw_input(''))
    if number != low and number !=high:
        if low < number:
            if high > number:
                print(' Good!' , low,'<', number,'<', high,)
            else:
                print('no,' , number, 'is hreater than ', high,)
        else:
            print('No, ' , number, 'is less than ', low)
    else:
        print('No, ', number, 'is one of the endpoints of the interval')
    