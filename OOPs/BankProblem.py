class Bank:

    total=[]
    def __init__(self, name, no, balance=0.0, types="current"):
        self.name = name
        self.no = no
        self.type = types.lower()
        if self.type == "savings":
            if balance < 5000:
                raise ValueError("Minimum balance for savings account is ₹5000")
        self.balance = balance
        self.details=[name,no,balance,types]
    def Accept_account(self):
        if self.type == "savings":
            if self.balance > 5000:   
                Bank.total.append(self.details)
        else:
            Bank.total.append(self.details)
    def deposit(self, amount):
        if amount <= 0:
            print("Deposit amount must be positive.")
        else:
            self.balance += amount
            self.details[2] = self.balance
            print(f"{amount} deposited. New balance: {self.balance}")

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be positive.")
            return
        if self.type == "current":
            if amount > self.balance:
                print("Insufficient funds! Withdrawal denied for current account.")
            else:
                self.balance -= amount
                self.details[2] = self.balance
                print(f"{amount} withdrawn (Current). New balance: {self.balance}")
        elif self.type == "savings":
            # Must keep ₹1000 minimum after withdrawal
            if amount + 1000 > self.balance:
                print("Withdrawal denied! Savings account must keep ₹1000 minimum after withdrawal.")
            else:
                self.balance -= amount
                self.details[2] = self.balance
                print(f"{amount} withdrawn (Savings). New balance: {self.balance}")
    
    def display(self):
        print(self.details)


b1 = Bank("Riya", 201, 8000, "savings")
b1.Accept_account()                
b1.deposit(2000)                   
b1.withdraw(9000)                  
b1.withdraw(8000)                  
b1.withdraw(5000)                  


b2 = Bank("Suresh", 202, 3000, "current")
b2.Accept_account()               
b2.deposit(1000)                   
b2.withdraw(4500)                  
b2.withdraw(4000)  

try:
    b3 = Bank("Arjun", 203, 3000, "savings")
    b3.Accept_account()           
except ValueError as e:
    print( e)





    