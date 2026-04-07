import random

class BusReservation:
    def __init__(self):
        self.routes = {
            1: {"route": "Mumbai to Pune", "price": 500},
            2: {"route": "Delhi to Jaipur", "price": 600},
            3: {"route": "Ahmedabad to Surat", "price": 400},
            4: {"route": "Chennai to Bangalore", "price": 700}
        }
        self.tickets = []

    def show_routes(self):
        print("*"*60)
        print("Available Routes:")
        for key, value in self.routes.items():
            print(f"{key}. {value['route']} - ₹{value['price']}")
        print("*"*60)

    def book_ticket(self):
        print("*"*60)
        print("Booking Ticket")
        print("*"*60)

        name = input("Enter Name: ")
        age = input("Enter Age: ")
        mobile = input("Enter Mobile: ")
        self.show_routes()
        choice = int(input("Select route number: "))

        if choice not in self.routes:
            print("Invalid route!")
            return

        route_name = self.routes[choice]["route"]
        seat_count = sum(1 for t in self.tickets if t["route"] == route_name)

        if seat_count >= 40:
            print("Sorry! Bus is full.")
            return

        seat_number = seat_count + 1
        ticket_id = "T" + str(random.randint(1000, 9999))

        ticket = {
            "id": ticket_id,
            "name": name,
            "age": age,
            "mobile": mobile,
            "route": route_name,
            "seat": seat_number
        }

        self.tickets.append(ticket)

        print("*"*60)
        print("Ticket Booked Successfully!")
        print(f"Ticket ID: {ticket_id}")
        print(f"Seat Number: {seat_number}")
        print("*"*60)

    def view_ticket(self):
        tid = input("Enter Ticket ID: ")
        found = False

        for t in self.tickets:
            if t["id"] == tid:
                print("*"*60)
                print("Ticket Details:")
                print(f"Name: {t['name']}")
                print(f"Route: {t['route']}")
                print(f"Seat: {t['seat']}")
                print("*"*60)
                found = True
                break

        if not found:
            print("Ticket not found!")

    def cancel_ticket(self):
        tid = input("Enter Ticket ID to cancel: ")
        found = False

        for t in self.tickets:
            if t["id"] == tid:
                self.tickets.remove(t)
                print("Ticket Cancelled Successfully!")
                found = True
                break

        if not found:
            print("Ticket not found!")

    def menu(self):
        while True:
            print("\n===== Bus Reservation System =====")
            print("1. Show Routes")
            print("2. Book Ticket")
            print("3. View Ticket")
            print("4. Cancel Ticket")
            print("5. Exit")

            choice = int(input("Enter your choice: "))

            if choice == 1:
                self.show_routes()
            elif choice == 2:
                self.book_ticket()
            elif choice == 3:
                self.view_ticket()
            elif choice == 4:
                self.cancel_ticket()
            elif choice == 5:
                print("Thank you for using the system!")
                break
            else:
                print("Invalid choice!")

b = BusReservation()
b.menu()