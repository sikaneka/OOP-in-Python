class Train:
    def __init__(self, train_no, train_name, source, destination, total_seats):
        self.train_no = train_no
        self.train_name = train_name
        self.source = source
        self.destination = destination
        self.total_seats = total_seats
        self.available_seats = total_seats

    def book_seat(self):
        if self.available_seats > 0:
            self.available_seats -= 1
            return True
        return False

    def cancel_seat(self):
        if self.available_seats < self.total_seats:
            self.available_seats += 1

    def display_info(self):
        return f"{self.train_no} - {self.train_name} ({self.source} ➡ {self.destination}) | Available Seats: {self.available_seats}"
