from BankAccount import BankAccount

class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount(intRate = 2, accountBalance = 0)
    # def deposit(self, amount):
    #     self.account.account_balance += amount
    #     return self
    # def withdrawal(self, amount):
    #     self.account.account_balance -= amount
    #     return self
    def userInfo(self):
        print('User:',self.name,'Account Info:')
        self.account.displayInfo()
        return self

cameron = User('cameron', 'c2323@gmail.com')
timothy = User('timothy', 't4343@gmail.com')
marissa = User('marissa', 'm212@gmail.com')
cameron.account.deposit(200).deposit(100).deposit(100).withdrawal(75).transfer(marissa,100).yieldInterest()
timothy.account.deposit(400).deposit(100).withdrawal(25).withdrawal(30).yieldInterest()
marissa.account.deposit(300).withdrawal(10).withdrawal(10).withdrawal(10).yieldInterest()
cameron.userInfo()
marissa.userInfo()
timothy.userInfo()
