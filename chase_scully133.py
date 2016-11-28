from __future__ import print_function # use Python 3.0 printing 

def age_limit_output(age):
    '''Step 6a if-else example'''
    AGE_LIMIT = 13          # convention: use CAPS for constants
    if age < AGE_LIMIT:
        print(str(age) + ' is below the age limit.')
    else:
        print(str(age) + ' is old enough.')
    print('Minimum age is ' + str(AGE_LIMIT))
def report_grade(percent): 
    '''Step 6b if-else'''
    GRADE = 80
    if percent < GRADE:
        print('A grade of ' + str (percent) + 'percent does not shows mastery. Seek extra help for more practise.')
    else:
        print('A grade of ' +str (percent) + 'percent shows mastery. Keep up the good work!')
        
def vowel(letter):
    vowels = 'aeiouAEIOU'
    if letter in vowels:
        return True
    else:
        return False
# should check len(letter)==1

def letter_in_word(guess, word):
    if guess in word:
        return True
    else:
        return False 
        
def hint(color, secret):
    if color in secret:
        print('The color ' + str (color) + 'IS in the secret sequence.')
    else:
        print('The color ' +str (color) + 'IS NOT in the secret sequence.')