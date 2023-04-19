# num1 = int(input("press 1 and enter for start quize :"))

# while num1<22:
#     num1 = int(input("please enter your number  :"))
#     print("you enter small number please try again")
# else:
#     pass

# while num1>25:
#     num1 = int(input("please enter your number :"))
#     print("you entered big number please try again")
# else:
#     print("congratulation, you won")


# that was my logik which is not right
# now we will write real program for this



n=18
number_of_guesses=1
print("number of guesses is limited to only 9 times")
while (number_of_guesses<=9):
    guess_number = int(input("guess the number:" ))
    if guess_number<18:
        print("----sorry, select big number")
    elif guess_number>18:
        print("----sorry, select samll number")
    else:
        print("you won")
        print(number_of_guesses,"took to finish")
        break#here we can also use of break
    print(9-number_of_guesses,"no.of guesses left")
    number_of_guesses = number_of_guesses+1

if (number_of_guesses>9):
    print("sorry, you have tried many times")




