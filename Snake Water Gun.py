import random
any = ("swg")
print("Welcome to snake,water and gun game")
print('you can try 4 times')
com_wins = 0
human_wins = 0
number_of_try = 1
while number_of_try<=4:
    user_select = input(' write \n s for snake,\n w for water ,\n g for gun ,\n 0 for exit the game:')
    c_choice = random.choice(any)
    if user_select=='s'and user_select.isalpha():
        if  c_choice=='w':
            print("human wins")
            human_wins=human_wins+1
        elif  c_choice=='g':
            print('computer wins')
            com_wins=com_wins+1
        elif c_choice=='s':
            print('match die')
        else:
            print("please try new ")
    elif user_select=='w' and user_select.isalpha():
        if  c_choice=='g':
            print("human wins")
            human_wins=human_wins+1
        elif  c_choice=='s':
            print('computer wins')
            com_wins=com_wins+1
        elif  c_choice=='w':
            print('match die')
        else:
            print("please try new ")
    elif user_select=='g' and user_select.isalpha():
        if  c_choice=='s':
            print("human wins")
            human_wins=human_wins+1
        elif  c_choice=='w':
            print('computer wins')
            com_wins=com_wins+1
        elif c_choice=='g' :
            print('match die')
        else:
            print("please try new ")
    elif user_select==0:
        break
    else:
        print('invalid input')
    print('the score is : computer wins =',com_wins , 'and' , 'human wins =' ,human_wins)
    print('now you have',4-number_of_try,'choice')
    number_of_try=number_of_try+1

print('the total score of computer and human is :' )
print('computer score is',com_wins,' , and human score is',human_wins , '.')

if com_wins<human_wins:
    print("so, finally 'human is winner's")
if human_wins<com_wins:
    print("so,finally 'computer is winner'")
if human_wins==com_wins:
    print('the score is same')

