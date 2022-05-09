class parkingLot():
    tickets = [100]
    parkingSpaces = [100]
    currentTicket = {
        'paid' : False
    }

    payment = 5

    # def __init__(self):
    #     self.

    def takeTicket(self):
        self.tickets[0] -= 1
        self.parkingSpaces[0] -= 1

    def payForParking(self):

        self.payment -= int(input("A ticket costs $5, please enter 5 to pay for it."))
        if self.payment <= 0:
            print("Your ticket has been paid, you have 15 minutes to leave.")
            self.currentTicket['paid'] = True

    def leaveGarage(self):
        if self.currentTicket['paid'] == True:
            input("Thank you, have a nice day!")
            self.tickets[0] += 1
            self.parkingSpaces[0] += 1
        else:
            self.payment -= int(input("A ticket costs $5, please enter 5 to pay for it."))

def run(astring):
    while True:
        response = input('Welcome to the Parking Garage, what do you want to do? "take/pay/leave/quit ')
        if response.lower() == 'quit':
            break
        elif response.lower() == 'take':
            astring.takeTicket()
        elif response.lower() == 'pay':
            astring.payForParking()
        elif response.lower() == 'leave':
            astring.leaveGarage()
        else:
            print("Try another command")

astring = parkingLot()
run(astring)