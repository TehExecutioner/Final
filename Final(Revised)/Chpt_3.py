# Noah Martinez
# 11/12/21
# Chapter 3, Meeting the Gunrunner
import time
import Chpt_4
from Global_Variables import inventory

print()
def Intro_Chpt3():
    print("You go to an underground gunrunner to gather supplies.")
    time.sleep(2.5)
    print("Choose your weapons.")
    print()

def choose_Chpt3_Primaries():
    print("Pick your primary")
    print()
    print("A. M4A1 (Great Range, Medium power, High Capacity)")
    print("B. Remington 870 (Great Stopping Power, Medium Range, Low Capacity)")
    print("C. RPG (Max Power, Measly Capacity, Great Range/Explosive Radius)")
    print("D. DSR-1 (High Power, High Range, Low Capacity)")
    print("E. Riot Shield (Bullet Deflection)")
    print()
    choice1 = input("Choose(A,B,C,D, or E): ")
    if choice1 == "A":
        A()
    elif choice1 == "B":
        B()
    elif choice1 == "C":
        C()
    elif choice1 == "D":
        D()
    elif choice1 == "E":
        E()
    else:
        print("perhaps retype your choice?")
        choose_Chpt3_Primaries()

def A():
    print("Solid choice, can turn a guy into swiss cheese.")
    inventory.append('M4A1')

def B():
    print("Great choice, definitely gonna pop some heads")
    inventory.append('Remington 870')

def C():
    print("Jeez, planning to take out a tank with that thing?")
    inventory.append('RPG-7')
def D():
    print("Very good choice, top of the line precision rifle right there.")
    inventory.append('DSR-1')
def E():
    print("Um, okay?")
    inventory.append('Riot Shield')

def choose_Chpt3_Secondaries():
    print("Pick your Secondary")
    print()
    print("A. M1911 (A tried and true pistol, WW2 era and still viable today. Packs a punch.)")
    print("B. Glock 17 (A great military/police pistol, with medium power and high capacity)")
    print('C. Combat Knife (Most lethal weapon you can have and be "Sneaky Peeky" about it)')
    print("D. Sawn-off Shotgun (Lol, Lupara go 'BLAM'! Low capacity though.)")
    print('E. .44 Magnum (A cop called this "The most powerful handgun in the world".)')
    print()
    choice2 = input("Choose(A,B,C,D, or E): ")
    if choice2 == "A":
        A2()
    elif choice2 == "B":
        B2()
    elif choice2 == "C":
        C2()
    elif choice2 == "D":
        D2()
    elif choice2 == "E":
        E2()
    else:
        print("perhaps retype your choice?")
        choose_Chpt3_Secondaries()

def A2():
    print("Nice! Can never go wrong with a old school .45 ACP.")
    inventory.append('M1911')
def B2():
    print("Very good choice.")
    inventory.append('Glock 17')
def C2():
    print("Better have a good primary with that, but you can never go wrong with stealth.")
    inventory.append('Knife')
def D2():
    print("This... is your BOOMSTICK!")
    inventory.append('Sawn-off Shotgun')
def E2():
    print("Make your enemies feel not-so-lucky.")
    inventory.append('.44 Magnum')


def start():
    Intro_Chpt3()
    while True:
        choose_Chpt3_Primaries()
        ans = input('Will you continue to choose(N) ')
        ans = ans.upper()
        if ans =='N':
            break
    print('Choose secondaries')
    while True:
        choose_Chpt3_Secondaries()
        ans = input('Will you continue to choose(N) ')
        ans = ans.upper()
        if ans =='N':
            break

    print('You are exiting from chapter3')
    Chpt_4.start()