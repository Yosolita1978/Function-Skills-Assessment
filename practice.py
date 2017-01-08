"""
Skills function practice.

Please read the the instructions first (separate file). Your solutions should
go below this docstring.

PART ONE:

    >>> hello_world()
    Hello World

    >>> say_hi("Balloonicorn")
    Hi Balloonicorn

    >>> print_product(3, 5)
    15

    >>> repeat_string("Balloonicorn", 3)
    BalloonicornBalloonicornBalloonicorn

    >>> print_sign(3)
    Higher than 0

    >>> print_sign(0)
    Zero

    >>> print_sign(-3)
    Lower than 0

    >>> is_divisible_by_three(12)
    True

    >>> is_divisible_by_three(10)
    False

    >>> num_spaces("Balloonicorn is awesome!")
    2

    >>> num_spaces("Balloonicorn is       awesome!")
    8

    >>> total_meal_price(30)
    34.5

    >>> total_meal_price(30, .3)
    39.0

    >>> sign_and_parity(3)
    ['Odd', 'Positive']

    >>> sign_and_parity(-2)
    ['Even', 'Negative']

PART TWO:

    >>> full_title("Balloonicorn")
    'Engineer Balloonicorn'

    >>> full_title("Jane Hacks", "Hacker")
    'Hacker Jane Hacks'

    >>> write_letter("Jane Hacks", "Hacker", "Balloonicorn")
    Dear Hacker Jane Hacks, I think you are amazing! Sincerely, Balloonicorn

"""

###############################################################################

# PART ONE

def hello_world():
    ''' This function says "Hello World" with no arguments'''
    
    print "Hello World"

def say_hi(name):
    ''' This function says "Hi" to the string (name) that takes as an argument '''
    
    print "Hi {}".format(name)

def print_product(num1, num2):
    '''Print the product of the two integers that takes as argument '''

    print num1 * num2

# 4. Write a function called 'repeat_string' that takes a string and an integer
#    and prints the string that many times

def repeat_string(string, n):
    ''' Print the string repeated the n times '''
    print string * n 


# 5. Write a function called 'print_sign' that takes an integer and prints
#    "Higher than 0" if higher than zero and "Lower than 0" if lower than zero.
#    If the integer is zero, print "Zero".

def print_sign(number):
    ''' This function evaluates if the integer is higher, lower or equal to zero '''
    
    if number > 0:
        print "Higher than 0"
    elif number < 0:
        print "Lower than 0"
    elif number == 0:
        print "Zero"


# 6. Write a function called 'is_divisible_by_three' that takes an integer and
#    returns a boolean (True or False), depending on whether the number is
#    evenly divisible by 3.

def is_divisible_by_three(number):
    ''' This function returns True or False if a number is divisible by 3 '''
    if number % 3 == 0:
        return True
    else:
        return False


# 7. Write a function called 'num_spaces' that takes a sentence as one string
#    and returns the number of spaces.

def num_spaces(sentence):
    ''' This function counts how many spaces are in a sentence that takes as argument '''

    list_sentence = list(sentence)
    count = 0
    for element in list_sentence:
        if element == " ":
            count = count + 1

    return count


# 8. Write a function called 'total_meal_price' that can be passed a meal price
#    and a tip percentage. It should return the total amount paid
#    (price + price * tip). **However:** passing in the tip percentage should
#    be optional; if not given, it should default to 15%.

def total_meal_price(price, tip=.15):
    ''' This function returns the total amount to pay with the formula (price + price * tip) '''

    tip_amount = price * tip
    total_meal_price = price + tip_amount

    return total_meal_price 



# 9. Write a function called 'sign_and_parity' that takes an integer as an
#    argument and returns two pieces of information as strings --- "Positive"
#    or "Negative" and "Even" or "Odd". The two strings should be returned in
#    a list.
#
#    Then, write code that shows the calling of this function on a number and
#    unpack what is returned into two variables --- sign and parity (whether
#    it's even or odd). Print sign and parity.

def sign_and_parity(number):
    ''' This function return in a list (a print statement) if a number is Positive, Negative, Even or Odd '''

    print_statement = []
    
    if number % 2 == 0:
        print_statement.append("Even")
    
    if number % 2 != 0:
        print_statement.append("Odd")

    if number > 0:
        print_statement.append("Positive")

    if number < 0:
        print_statement.append("Negative")

    return print_statement


sign, parity = sign_and_parity(30)
print sign, parity

# This function will break baddly if the number = 0. The first validation needs to be if the numbers is Zero. 



###############################################################################

# PART TWO

# 1. Write a function that takes a name and a job title as parameters, making
#    it so the job title defaults to "Engineer" if a job title is not passed
#    in. Return the person's title and name in one string.

def full_title(name, title="Engineer"):
    ''' This functions return in one string the job title and the name that takes as arguments '''

    return "{} {}".format(title, name)

# 2. Given a recipient name & job title and a sender name, print the following
#    letter:
#
#       Dear JOB_TITLE RECIPIENT_NAME, I think you are amazing!
#       Sincerely, SENDER_NAME.
#
#    Use the function from #1 to construct the full title for the letter's
#    greeting.

def write_letter(recipient_name, job_title, sender_name):
    ''' This function wrote a letter to the recipient name, using her/his job title, from the sender name that takes as argument. It returns a string with format '''
    
    print "Dear {}, I think you are amazing! Sincerely, {}".format(full_title(recipient_name, job_title), sender_name)



###############################################################################

# END OF PRACTICE: You can ignore everything below.

if __name__ == "__main__":
    import doctest

    print
    result = doctest.testmod()
    if not result.failed:
        print "ALL TESTS PASSED. GOOD WORK!"
    print
