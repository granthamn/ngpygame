# Functions
def fib(n):
    """Function to print Fibonnacci sequence up to n"""
    a,b=0,1
    while a < n:
        print(a,end=",")
        a,b=b,a+b

def fib2(n):
    """Return a list containing Fib sequence up to n"""
    result=[]
    a,b = 0,1
    while a < n:
        result.append(a)
        a,b=b,a+b
    return result

def ask(prompt, retries=4, reminder='Try again, please!:'):
    """Function to demonstrate default parameters"""
    while True:
        ok = input(prompt)
        if ok in ('y','ye','yes'):
            return True
        if ok in ('n','no','nope'):
            return False
        retries=retries - 1
        if retries < 0:
            raise ValueError('Invalid response')
        print(reminder)
        
