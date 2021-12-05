from Global_Variables import inventory
import time
import Chpt_5

def Intro_Chpt4():
    print("You find the gang location, now you must fight off the gang members")
    print("in order to reach your daughter.")
    print()
    time.sleep(1)
    print("you have equipped", inventory)
    time.sleep(3)
    fate()

def fate():
    live()
    live2()
    live3()
    live4()
    die()
    die2()
    die3()
    die4()

def live():
    if 'M4A1' and 'M1911' in inventory:
        print('You made it out, no fuss!')
    elif 'M4A1' and 'Glock 17' in inventory:
        print('You made it out, no fuss!')
    elif 'M4A1' and '.44 Magnum' in inventory:
        print('You made it out, no fuss!')
    elif 'M4A1' and 'Sawn-off Shotgun' in inventory:
        print('You made it out, no fuss!')
    elif 'M4A1' and 'Knife' in inventory:
        print('You made it out, no fuss!')
    else:
        live2()

def live2():
    if 'Riot Shield' in inventory and 'M1911' in inventory:
        print('You practically barged your way to the boss!')
    elif 'Riot Shield' in inventory and '.44 Magnum' in inventory:
        print('You practically barged your way to the boss!')
    elif 'Riot Shield' in inventory and 'Glock 17' in inventory:
        print('You practically barged your way to the boss!')
    else:
        live3()

def live3():
    if 'Remington 870' in inventory and 'M1911' in inventory:
        print('You left no one alive, only left a mess!')
    elif 'Remington 870' in inventory and '.44 Magnum' in inventory:
        print('You left no one alive, only left a mess!')
    elif 'Remington 870' in inventory and 'Glock 17' in inventory:
        print('You left no one alive, only left a mess!')
    elif 'Remington 870' in inventory and 'Knife' in inventory:
        print('You left no one alive, only left a mess!')
    else:
        live4()

def live4():
    if 'DSR-1' in inventory and 'Sawn-off Shotgun' in inventory:
        print('You picked off a ton of people, positioned at another building. No one could locate you!')
    elif 'DSR-1' in inventory and 'Glock 17' in inventory:
        print('You picked off a ton of people, positioned at another building. No one could locate you!')
    else:
        die()

def die():
    if 'RPG-7' and 'M1911' in inventory:
        print('Everyone died because you blew up the building!')
        quit()
    elif 'RPG-7' and 'Glock 17' in inventory:
        print('Everyone died because you blew up the building!')
        quit()
    elif 'RPG-7' and '.44 Magnum' in inventory:
        print('Everyone died because you blew up the building!')
        quit()
    elif 'RPG-7' and 'Sawn-off Shotgun' in inventory:
        print('Everyone died because you blew up the building!')
        quit()
    elif 'RPG-7' and 'Knife' in inventory:
        print('Everyone died because you blew up the building!')
        quit()
    else:
        die2()

def die2():
    if 'Riot Shield' and 'Sawn-off Shotgun' in inventory:
        print('You died by getting shot up, while attempting to switch to your secondary!')
        quit()
    elif 'Riot Shield' and 'Knife' in inventory:
        print('You died by getting shot up, while attempting to switch to your secondary!')
        quit()
    else:
        die3()

def die3():
    if 'DSR-1' and 'M1911' in inventory:
        print('You died by getting shot up because you ran out of ammo!')
        quit()
    elif 'DSR-1' and '.44 Magnum' in inventory:
        print('You died by getting shot up because you ran out of ammo!')
        quit()
    elif 'DSR-1' and 'Knife' in inventory:
        print('You died by getting shot up because you ran out of ammo!')
        quit()
    else:
        die4()

def die4():
    if 'Remington 870' and 'Sawn-off Shotgun' in inventory:
        print('You died by getting shot up, because')
        print('you did not have a weapon that had enough range to hit further targets!')
        quit()


def start():
    Intro_Chpt4()
    #You may add the options for Chapter4
    print('Now you are exiting from chapter4')
    print('Chapter5 will start')
    Chpt_5.start()

