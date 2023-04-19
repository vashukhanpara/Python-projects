from time import *
import random as r
from tkinter import EXCEPTION

count=0
def mistake(par_test, user_test):
    error = 0
    for i in range(len(par_test)):
        try:  # ahi try and except no use etla mate karyo 6 k jo apde userinput ma 5 j words lakhie to error ave kem k etle index na thai sake
            if (par_test[i] != user_test[i]):
                error = error+1
        except:
            error = error+1
    return error


def speed_time(s_time, e_time, user_paragraph):
    time_delay = round(e_time - s_time, 3)
    # round() na use thi number round figer thai jai
    time_r = round(time_delay, 2)
    speed = len(user_paragraph)/time_r

    return round(speed)


while count<=3:
    check = input('if you are ready to start , type "yes" for ready, else type "no" :')
    if check == 'yes' or  user_check==1:
        test = ('The mechanical engineering field requires an understanding of core areas including mechanics, dynamics, thermodynamics, materials science'), ('structural analysis, and electricity. In addition to these core principles, mechanical engineers use tools such as computer-aided design (CAD)'), ('computer-aided manufacturing (CAM), and product lifecycle management to design and analyze manufacturing plants'), (
'industrial equipment and machinery, heating and cooling systems, transport systems, aircraft, watercraft'), ('robotics, medical devices, weapons, and others. It is the branch of engineering that involves the design, production, and operation of machinery.[2][3]'), ('my name is gaurav prajapati welcome to wscube teck jodhpur so you can come at jodhpur to learn very good python or any other language or webdevlopment')
        test1 = r.choice(test)
        test1 = (test[1])
        print('********** Welcome to Typing Speed Test**********')
        print(test1)
        print()
        time1 = time()
        print('type this paragraph to check your speed')
        test_input = input()
        time2 = time()
        
        print('speed : ', speed_time(time1, time2, test_input), 'words per second')#aama words per second ahiya na lakhine def function ma return ni hare lakhie to pan chale
        print('error : ', mistake(test1, test_input))

        count=count+1
        print('do you want to try again? type "1" for yes and "0" for no :')
        user_check=input()

    elif check=='no':
        print('Thankyou , Exiting.....')
        break

    else:
        print('invalid input')
        break