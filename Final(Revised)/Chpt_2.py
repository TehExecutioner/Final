from Global_Variables import clues
import time
import Chpt_3

def Intro_Chpt2():
    print("You ask your friend in the police department to ask for any information")
    print("regarding any information about local gangs")
    print()
def choose_Chpt2():
    print("What do you want to do?")
    print()
    print("A. Show clues gathered.")
    print("B. Just ask for locations of any local gangs.")
    choice = input("Choose(A or B): ")
    if choice == "A":
        A()
    elif choice == "B":
        B()
    else:
        print("perhaps retype your choice?")
        choose_Chpt2()

def A():
    if 'clues' in clues:
        print("Your friend knew exactly what gang was involved in the crime")
        print("and gave you a location to a Warehouse that's not too far.")
    else:
        print('You did not gather any clues though!')
        B()
def B():
    print("Your police friend provided you with a list of known gangs in the area.")
    print()
    print("It's up to you to guess which location might your daughter be at.")
    print("Choose wisely.")
    print()
    print("A. Coin Laundry")
    print("B. Abandoned Warehouse")
    print("C. Old Train Yard")
    print("D. Restaurant")
    choice= input("")
    if choice == "B":
        print("You're Right!")
    else:
        print("You got your location wrong, game over.")
        quit()

#create a function to call the Intro_Chpt2 and choose_Chpt2()
def start():
    Intro_Chpt2()
    while True:
        choose_Chpt2()
        ans = input('Will you continue to choose(N) ')
        ans = ans.upper()
        if ans == 'N':
            break
    print('You are exiting from Chapter2')
    Chpt_3.start()