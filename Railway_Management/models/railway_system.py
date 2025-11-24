import random
from .ticket import Ticket

class RailwaySystem:
    def __init__(self):
        self.trains = []
        self.tickets = []

    def add_train(self, train):
        self.trains.append(train)

    def show_trains(self):
        return [t.display_info() for t in self.trains]

    def find_train(self, train_no):
        for train in self.trains:
            if train.train_no == train_no:
                return train
        return None

    def book_ticket(self, train_no, passenger):
        train = self.find_train(train_no)
        if not train:
            return "❌ Train not found!"
        if train.book_seat():
            ticket_id = "T" + str(random.randint(1000, 9999))
            ticket = Ticket(ticket_id, train, passenger)
            self.tickets.append(ticket)
            return ticket
        else:
            return "❌ No seats available!"

    def cancel_ticket(self, ticket_id):
        for ticket in self.tickets:
            if ticket.ticket_id == ticket_id and ticket.status == "Booked":
                ticket.cancel_ticket()
                return f"✅ Ticket {ticket_id} cancelled successfully."
        return "❌ Ticket not found or already cancelled."
