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
        break
    print(9-number_of_guesses,"no.of guesses left")
    number_of_guesses = number_of_guesses+1

if (number_of_guesses>9):
    print("sorry, you have tried many times")




