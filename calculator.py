def add(x,y):
    return x+y
def subtract(x,y):
    return x-y
def multiply(x,y):
    return x*y
def divide(x,y):
    if y==0:
        return f'error!!!!{x}/{y} not defined'
    else:
        return x/y
def power(x,y):
    return x**y
def floordivision(x,y):
    if y==0:
        return f'error!!!!{x}//{y} not defined'
    else:
        return x//y
def square(x):
    return x*x
def cube(x):
    return x*x*x

def sqroot(x):
    for num in range(1,x):
        if x/num==num:
            return num
    else:
        return x
def avg(lst=[]):
    'enter a list to get average'
    #print(__doc__)
    sum=0
    count=0
    for num in lst:
        sum+=num
        count+=1
    return sum/count

def evaluate(expression):
    'enter an expression such as 1+2 or 3-2 etc'
    return eval('expression')



    
