class Bank:

    def Amount_cast(self, Amount):
        self.Amount = Amount
        self.Remaining = int(self.Remaining) - int(self.Amount)
        return f'cast: {self.Amount} Remaining: {self.Remaining}'
    
    def Amount_deposit(self, deposit):
        self.deposit = deposit
        self.Remaining = int(self.Remaining) + int(self.deposit)
        return f'deposit: {self.deposit} Remaining: {self.Remaining}'

    def Amount_transfer(self, Amount_transfer, numberOfAccount):
        self.Amount_transfer = Amount_transfer
        self.numberOfAccount = numberOfAccount
        self.Remaining = int(self.Remaining) - int(self.Amount_transfer)
        return f'transfer to: {self.numberOfAccount}, your Remaining: {self.Remaining}'

    def __init__(self, username, Remaining, min_Remaining):
        self.username = username
        self.Remaining = int(Remaining)
        self.min_Remaining = int(min_Remaining)

masoud = Bank('masoud', 200000, 10000)

print(masoud.Amount_cast(10000))
print(masoud.Amount_deposit(50000))
print(masoud.Amount_transfer(10000, 23341212))