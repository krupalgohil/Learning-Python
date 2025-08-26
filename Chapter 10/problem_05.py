'''

5. Write a Class ‘Train’ which has methods to book a ticket, get status (no of seats) 
and get fare information of train running under Indian Railways. 

'''
class Train:
    def __init__(self, name, fare, seats):
        self.name = name          # Train name
        self.fare = fare          # Ticket price
        self.seats = seats        # Available seats

    def get_status(self):
        """Show available seats"""
        print(f"The train {self.name} has {self.seats} seats available.")

    def get_fare_info(self):
        """Show ticket price"""
        print(f"The ticket price of {self.name} is Rs. {self.fare}")

    def book_ticket(self):
        """Book a ticket if seats are available"""
        if self.seats > 0:
            print(f"Your ticket has been booked! Your seat number is {self.seats}.")
            self.seats -= 1
        else:
            print("Sorry, the train is full. No seats available.")


# -------- Example usage --------
intercity = Train("Intercity Express: 14015", 90, 2)

intercity.get_status()
intercity.get_fare_info()
intercity.book_ticket()
intercity.book_ticket()
intercity.book_ticket()   # this will show no seats available
intercity.get_status()
