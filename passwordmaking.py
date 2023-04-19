password='vashu'
user_try = 0
print('you can 10 try')


while user_try<10:
    user_enter = input('enter your password:')
    if user_enter!=password:
        print('you lose , try again')
        user_try=user_try+1
        print('now , you have' , 10-user_try, 'chances')

    else:
        print('you won')
        user_try=user_try+10#ahiya break use karie to pan chale 
       


