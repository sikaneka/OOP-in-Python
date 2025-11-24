class Ticket:
    def __init__(self, ticket_id, train, passenger):
        self.ticket_id = ticket_id
        self.train = train
        self.passenger = passenger
        self.status = "Booked"

    def cancel_ticket(self):
        self.status = "Cancelled"
        self.train.cancel_seat()

    def show_ticket(self):
        return {
            "Ticket ID": self.ticket_id,
            "Train": self.train.train_name,
            "Passenger": self.passenger.display_passenger(),
            "Status": self.status
        }
