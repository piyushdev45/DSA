class Flight:
    def __init__(self, flight_name, total_seats):
        self.flight_name = flight_name
        self.total_seats = total_seats
        self.seats = ["Empty"] * total_seats

    def show_seats(self):
        print("\nSeat Status:")
        for i in range(len(self.seats)):
            print(f"Seat {i+1}: {self.seats[i]}")

    def book_seat(self, seat_no, name):
        if seat_no < 1 or seat_no > self.total_seats:
            print("Invalid seat number!")
        elif self.seats[seat_no - 1] == "Empty":
            self.seats[seat_no - 1] = name
            print(f"Seat {seat_no} booked successfully for {name}")
        else:
            print("Seat already booked!")

    def cancel_seat(self, seat_no):
        if seat_no < 1 or seat_no > self.total_seats:
            print("Invalid seat number!")
        elif self.seats[seat_no - 1] == "Empty":
            print("Seat already empty!")
        else:
            print(f"Booking for {self.seats[seat_no - 1]} cancelled")
            self.seats[seat_no - 1] = "Empty"


# Main Program
flight = Flight("Air India AI-202", 10)

while True:
    print("\n--- Airplane Booking System ---")
    print("1. Show Seats")
    print("2. Book Seat")
    print("3. Cancel Seat")
    print("4. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        flight.show_seats()

    elif choice == 2:
        seat = int(input("Enter seat number: "))
        name = input("Enter your name: ")
        flight.book_seat(seat, name)

    elif choice == 3:
        seat = int(input("Enter seat number: "))
        flight.cancel_seat(seat)

    elif choice == 4:
        print("Thank you!")
        break

    else:
        print("Invalid choice!")