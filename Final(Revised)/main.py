import Chpt_1
import Chpt_2
import Chpt_3
import Chpt_4
import Chpt_5
import Global_Variables

#In main function, you need to provide game introduction
def game_intro():
    print('*' *70)
    print('\nThis game is about you, the player, attempting to save your daughter.')
    print('Your choices affect your outcome, so choose wisely!')
    print()
    print('*' * 70)



game_intro()
name = input('What is your name ')
ans = input('Hi {}, Will you start a game? y/n'.format(name))
ans = ans.upper()

if ans == 'Y':
    Chpt_1.start()
else:
    print('You are exiting this game')
    quit()
