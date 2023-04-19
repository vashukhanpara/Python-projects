class Bikeshop:
    def __init__(self, stock):#we created constructor
        self.stock = stock

    def displaybike(self):
        print('    Total bikes are', self.stock)

    def rent(self, q):
        if q <= 0:
            print("    Enter the big number (greater than 0)")
        elif q > self.stock:
            print('    Enter value less than stock')
        else:
            self.stock = self.stock-ui
            print('    Total price of your rent is', q*100)
            print('    Now we have stock of bikes are', self.stock)


n = 0
while n < 10:
    obj = Bikeshop(100)
    user_input = int(input('''    
press 1 for check stock
press 2 for check rent
press 3 exit
-->'''))

    if user_input == 1:
        obj.displaybike()

    elif user_input == 2:
        ui = int(input('    enter number of bikes to rent :'))
        obj.rent(ui)

    elif user_input == 3:
        break

    else:
        print('invalid input')

    n += 1
