class Atm:
    #constructor (here init is a constructor is a special method in which when code is
    # written is executed automatically whe we create an object of class)
    
    def __init__(self):
        self.pin = ""
        self.balance = 0
        self.menu()
    
    def menu(self):
        user_input = input("""
        Hello How would you like to proceed?
        1. Enter 1 to create pin
        2. Enter 2 to deposit
        3. Enter 3 to withdraw
        4. Enter 4 to check balance
        5. Enter 5 to exit
        """)
        if(user_input == 1):
            self.create_pin()
        elif(user_input == 2):
            self.deposit()
        elif(user_input == 3):
           self.withdraw()   
        elif(user_input == 4):
            self.check_balance()
        else:
            print("Bye")
            
            
    def create_pin(self):
        self.pin= input("Enter your Pin")
        print("Print set succesfully")
        
        
        
    def deposit(self):
        temp = input("Enter your pin")
        if(temp == self.pin):
            amount = int(input("Enter amount to deposit"))
            self.balance= self.balance + amount
        else:
            print("Invalid pin")
       
            
    def Withdraw(self):
        temp = input("Enter your pin")
        if (temp == self.pin):
            amount = int(input("Enter amount to Withdraw"))
            if(amount<self.balance):
                self.balance = self.balance - amount
                print("Operation Successful")
                
            else:
                print("Insufficient funds")
        else:
            print("Invalid pin")
            
                    
            
            
        def check_balance(self):
            temp = input("Enter your pin")
            if(temp == self.pin):
                print(self.balance)
            else:
                print("Invalid Pin")
            

sbi = Atm()
sbi.check_balance()