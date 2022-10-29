# CTS 285
# M2HW1
# Marceia Patterson
# 10/17/2022

# TO DO LIST:
# Display first menu: Choosing a math operation
# Show a random ADDITION problem if 1 is chosen, vice versa for the others.


import random

#Variables for first Menu
ADD_NUM = 1
SUB_NUM = 2
DIV_NUM = 3
MULT_NUM = 4
EXIT = 5


DB1 = random.randrange(9,99)
DB2 = random.randrange(9,99)

def main():
    choice = 0
    while choice != EXIT:
   
        displayMenu()
        try:
            choice = int(input("Enter your choice: "))
            
        except ValueError:
            print('Please only type options 1-5 on the Menu.')
            print('\n')
        if choice == ADD_NUM:
            print("Addition selected.")
            calcAdd()
            
        elif choice == SUB_NUM:
            print("Subtraction selected.")
            calcSub()
        elif choice == DIV_NUM:
            print("Division selected.")
            calcDiv()
        elif choice == MULT_NUM:
            print("Multiplication selected.")
            calcMulti()
            
        elif choice == EXIT:
            print("Exiting program. Goodbye!")
        else:
            print("Invalid input")
        
    
    #Menu stuff - 1) Add; 2) Subtract; 3) Divide; 4) Multiply; 5) Exit.
    #Need a loop.
    
    

def calcAdd():
    add1 = random.randrange(0,99)
    add2 = random.randrange(0,99)
    
    answer =  int(input(f"What is {add1} + {add2}?\n"))
    if answer == (add1 + add2):
        print("That's right!")
    else:
        print("The answer was ",add1 + add2)
        print("Try again.")
        calcAdd()
   
def calcSub():
   sub1 = random.randrange(0,99)
   sub2 = random.randrange(0,99)
    
   answer =  int(input(f"What is {sub1} - {sub2}?\n"))
   if answer == (sub1 - sub2):
        print("That's right!")
   else:
        print("The answer was ",sub1 - sub2)
        print("Try again.")
        calcSub()
   
def calcDiv():
   g = random.randrange(1,10)
   y = random.randrange(1,10)
   
   x = g * y

   answer =  int(input(f"What is {x} / {g}?\n"))
   if answer == (x / g):
        print("That's right!")
   else:
        print("The answer was ",x / g)
        print("Try again.")
        calcDiv()
   
def calcMulti():
   multi1 = random.randrange(1,99)
   multi2 = random.randrange(1,99)
    
   answer =  int(input(f"What is {multi1} * {multi2}?\n"))
   if answer == (multi1 * multi2):
        print("That's right!")
   else:
        print("The answer was ",multi1 * multi2)
        print("Try again.")
        calcMulti()



def displayMenu():
    print("Please choose from the following: ")
    print("1) ADD")
    print("2) SUBTRACT")
    print("3) DIVIDE")
    print("4) MULTIPLY")
    print("5) EXIT")
    
if __name__ == "__main__":
    main()
