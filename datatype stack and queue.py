# list vadu works in lifo
l = []
f= 0
while f < 10 :
    user_input = int(input('''
press 1 for Push element
Press 2 for pop element
Press 3 for peek element
Press 4 for Display full stack
Press 5 for Exit

---->'''))
    if user_input == 1:
        n = input('    Enter the push value:')
        if n == (''):
            print('    you enterd nothig')
        else:
            l.append(n)
        print('    Your new stack is' , l)

    elif user_input == 2:
        if len(l)==0:
            print('    Empty stack')
        else:
            p = l.pop()
            print('    Your deleted stack is' ,p)
            print ('    Your new stack is' ,l)
     
    elif user_input == 3:
        if len(l)==0:
            print('    Empty stack')
        else:
            print('    Last stack value is ' , l[-1])

    elif user_input==4:
        if len(l)==0:
            print('    Empty stack')
        else:
            print("    Full stack is",l)

    elif user_input ==5:
        break

    else:
        print('    Sorry , invalid input')
         
    f += 1
else:
    print('    sorry , out of moves')




# queue wadu works in lilo or fifo
q = []
f= 0
while f < 10 :
    user_input = int(input('''
press 1 for Push element
Press 2 for pop element
Press 3 for first element
Press 4 for last element
Press 5 for Display complete queue
Press 6 for Exit

---->'''))
    if user_input == 1:
        n = input('    Enter the push value:')
        q.append(n)
        print('    Your new queue is' , q)

    elif user_input == 2:
        if len(q)==0:
            print('    Empty queue')
        else:
            first_element = q[0] 
            del q[0]
            print('    Your deleted queue is' ,first_element)
            print ('    Your new queue is' ,q)
     
    elif user_input == 3:
        if len(q)==0:
            print('    Empty queue')
        else:
            print('    First  queue Element is ' , q[0])

    elif user_input==4:
        if len(q)==0:
            print('    Empty queue')
        else:
            print("    Last  queue Element is",q[-1])

    elif user_input==5:
        if len(q)==0:
            print('    Empty queue')
        else:
            print('Full Queue is' , q)
        
    elif user_input ==6:
        break

    else:
        print('    Sorry , invalid input')
         
    f += 1
else:
    print('--------sorry , out of moves----------------------------')
