class BankAccount:
    def __init__(self, intRate = 0, accountBalance = 0):
        self.accountBalance = accountBalance
        self.intRate = intRate/100
        self.intYield = 0
    def deposit(self, amount):
        self.accountBalance += amount
        return self
    def withdrawal(self, amount):
        self.accountBalance -= amount
        return self
    def yieldInterest(self):
        self.intYield += self.accountBalance * self.intRate
        self.intYield = round(self.intYield,2)
        self.accountBalance += self.intYield
        return self
    def displayInfo(self):
        print('Balance:',self.accountBalance, 'Interest Rate:',self.intRate, 'Interest Yield:',self.intYield)
        return self
    def transfer(self, otherUser, amount):
        self.accountBalance -=amount
        otherUser.account.accountBalance += amount
        return (self) 