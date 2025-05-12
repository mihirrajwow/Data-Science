class Train:
    def __init__(self,name,fare,seats):
        self.name = name
        self.fare = fare
        self.seats = seats

    def getStatus(self):
        print("*********")
        print(f"The name of the train is {self.name}.")
        print(f"The seats available in the train is {self.seats}.")
        print("*********")

    def fareInfo(self):
        print(f"The price of the ticket is: Rs {self.fare}")

    def bookTicket(self):
        if(self.seats>0):
            print("Your ticket has been booked!")
            self.seats -= 1
        else:
            print(f"Sorry this train is full. Kindly try in tatkal.")
    
    # def cancelTicket(self,seatNo):
    #     pass

intercity = Train("Intercity Express 14016",90,1)
intercity.getStatus()
intercity.bookTicket()
intercity.getStatus()
intercity.bookTicket()
intercity.fareInfo()