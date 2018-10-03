from entries import AbstractAmountChange


class CreditEntry(AbstractAmountChange):
    def __init__(self, amount):
        super().__init__(amount)
        self.typename = "credit_entry"

    def __eq__(self, other):
        return self.amount == other.amount

    def __str__(self):
        return str(self.amount)