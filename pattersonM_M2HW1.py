# CTS 285
# M2HW1
# Marceia Patterson
# 10/17/2022

# TO DO LIST:
# Display first menu: Choosing a math operation
# Display sceond menu: Choosing a difficulty
# Display math problem according to chosen operation and difficulty.


#Variables for first Menu
ADD_NUM = 1
SUB_NUM = 2
DIV_NUM = 3
MULT_NUM = 4
EXIT = 5


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
  pass;
   
def calcSub():
   pass;
   
def calcDiv():
   pass;
   
def calcMulti():
   pass;



def displayMenu():
    print("Please choose from the following: ")
    print("1) ADD")
    print("2) SUBTRACT")
    print("3) DIVIDE")
    print("4) MULTIPLY")
    print("5) EXIT")
    
if __name__ == "__main__":
    main()
