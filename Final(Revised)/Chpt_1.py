#Noah Martinez
#11/12/21
#the first chapter
import time
import Chpt_2
from Global_Variables import clues

def Intro_Chpt1():
    print("You come back home after a long day at the office,")
    print("only to find out that your home is ruined, and your daughter is missing.")
    time.sleep(2.5)
    print("Investigate your home, and search for clues as to who did this.")
    print()

def choose_Chpt1():
    print("What do you want to do?")
    print()
    print("A. Search The House For Clues")
    print("B. Go To The Police Station")
    print("C. Go To The Gunrunner")
    print("D. Call The Police")
    print()
    choice = input("Choose(A,B,C, or D): ")
    if choice == "A":
        A()
    elif choice == "B":
        B()
    elif choice == "C":
        C()

    elif choice == "D":
        D()
    else:
        print("perhaps retype your choice?")
        choose_Chpt1()

def A():
    print("You chose to look for clues.")
    time.sleep(0.5)
    print('in which you found')
    clues.append('clues')

def B():
    print("You chose to go to the Police Station,")
    print("to talk to your Police Friend")

def C():
    print("You chose to take matters into your own hands")
    time.sleep(2)
    print("Out of anger you go to a gun runner to get yourself a gun, and head out to find your daughter.")
    time.sleep(3)
    print("Then you realized you have no idea where even is your daughter. So you go back home.")
    print()
    Intro_Chpt1()
    choose_Chpt1()

def D():
    print("You chose to call the police.")
    time.sleep(2)
    print("Some time passes by...")
    time.sleep(2)
    print("The Police could not find your daughter, and decide to call off the search.")
    time.sleep(1)
    print("You will never get your daughter back.")
    print()
    playAgain = input('Want to play again?(Type "Yes" or "Y"): ')
    if playAgain == "Yes" or "Y":
        print()
        choose_Chpt1()
    else:
        quit()

#The following function is called in main function
def start():
    Intro_Chpt1()
    while True:
         choose_Chpt1()

         keep = input('Will you continue to choose? (N) ')
         keep  = keep.upper()
         if keep == 'N':
            break

    print('You are now exiting Chapter1')
    Chpt_2.start()