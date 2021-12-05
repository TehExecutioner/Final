import time
from Global_Variables import inventory
def Intro_Chpt5():
    print("You find the gang leader in his personal office, only to notice he")
    print("has your daughter at gunpoint. He demands you drop your weapons.")
    time.sleep(1)
    print("You have done so to increase odds of your daughter living, what are you going to do?")
    print("A. Throw Knife (If Equipped)")
    print("B. Negotiate")
    choice = input(":")
    if choice == "A":
        A()
    else:
        B()

def A():
    if 'Knife' in inventory:
        print("You remember you have a knife, and without hesitation, you throw it at the boss's")
        print("foot, and winces in pain, as he lets you daughter go. You pick up your gun, and blow")
        print("him to smithereens. You take your daughter by the hand, and walk home in the sunrise.")
    else:
        print("You thought you had a knife, but you didn't, so you resorted to your next option.")
        B()
def B():
    print("You decided to take the safest approach, and see if you can negotiate a deal, the boss agrees.")
    print("He demanded that you give him 300,000 dollars for your daughter, which is half of your life savings,")
    print("but at least you'll be saving your daughter's life. You transfer him the funds, and he lets you both")
    print("go. You feel defeated, but at least you have saved your daughter's life.")

def start():
    while True:
        Intro_Chpt5()
        ans  = input('Will you continue to choose the options (N)')
        ans = ans.upper()
        if ans == 'N':
            break

    print('You are reaching at the end of chapter5')
    print('Game is over')
    quit()