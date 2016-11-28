# -*- coding: utf-8 -*-
def days():
    ''' Explain the function here
    '''
    for days in 'MTWRFSS':
        print(day + 'day')
    for day in range(5,8):
        print('It is the ' + 'th of September')
        
import matplotlib.pyplot as plt # standard short name
import random
plt.ion() # sets “interactive on”: figures redrawn when updated

def picks():
    a = [] # make an empty list
    
    # Why all the brackets below?     
    # a += [  brackets here to add an iterable onto a list      ]    
    #    random.choice(   [brackets here to choose from a list] )    
    # a += [random.choice([1, 3, 10])] 
    
    for choices in range(5):
         a += [random.choice([1, 3, 10])]
         
    plt.hist(a)
    plt.show()
    
def roll_hundred_pair():
    p = []
    diceone = [1,2,3,4,5,6]
    dicetwo = [1,2,3,4,5,6]
    for choices in range(100):
        p += [random.choice(diceone) + random.choice(dicetwo)]
       
    plt.hist(p)
    plt.show()    

def dice(n):    
    c = 0
    dice_one = [1,2,3,4,5,6]
    for choices in range(n):
        c += random.choice(dice_one)
    print "Roll was " + str(c)