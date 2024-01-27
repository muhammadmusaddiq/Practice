def fun():
         print("Muhammad Musaddiq")
         print("CIT KORANGI CAMPUS")
         print("TIMING 7-9")
#driver's code
#calling function

EXAMPLE OF EVEN/ODD

def evenOdd(x):
    if(x % 2 == 0):
        print("even")
    else :
         print("odd")
#Driver code
evenOdd(2)
evenOdd(3)

EXAMPLE OF NUMBERING

#python program to demonstrate
#default arguments
def myFun(x, y = 50):
  print("x: ", x)
  print("y: ", y)
 #Driver code
myFun(10)

EXAMPLE OF PYTHON KEYWORD ARGUMENTS

def student(firstname, lastname):
    print(firstname, lastname)
    
#keyword arguments
student(firstname ='Geeks',lastname ='Practice')
student(lastname = 'Practice',firstname ='Geeks')
