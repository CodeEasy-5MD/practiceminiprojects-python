class bank:
    def __init__(self, b):
        self.bbalance = b
    def Check_Balance(self):
        print("Your bank balance is", self.bbalance)
# instantiate the class
amount = float(input("Enter amount to deposit\n"))
w = bank(amount)

#delete property
del w.bbalance
w.Check_Balance()
#update the value
w.bbalance = 20000.00

w.Check_Balance()
