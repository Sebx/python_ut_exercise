
class Rent(object):

    def __init__(self):
        self.total = 0
        self.rents = 0

    def by_hour(self, qty=1):
        #charging $5 per hour
        self.total += qty * 5
        self.rents += 1
        return self

    def by_day(self, qty=1):
        #charging $20 a day
        self.total += qty * 20
        self.rents += 1
        return self

    def by_week(self, qty=1):
        #changing $60 a week
        self.total += qty * 60
        self.rents += 1
        return self

    def apply_family_promotion(self):
        #include 3 to 5 Rentals with a discount of 30% total price
        if self.rents in range(3, 6):
            self.total -= self.total * 0.3
        else:
            raise ValueError('Promotion does not apply')

    @property
    def total_amount(self):
        return self.total