class BankAccount:

    def __init__(self):

        self.__balance = 0
        self.run = True
        self.transaction = 0


    def getbalance(self):
        return self.__balance

    def  setbalance(self, amount):
        self.__balance += amount


    def deposit(self, amount):

        if amount == 0:
            print("You Can't Deposit Zero.Please Add Some Valid Amount.\n")
        elif amount < 0:
            print("YOur Amount Is In Negative.Please Add Some Valid Amount.\n")
        else:
            self.setbalance(amount)
            self.transaction += 1

    def withdraw(self, amount):

        if self.getbalance() >= amount:
            self.setbalance(self.getbalance() - amount)
            print(f"You Have Successfully Withdrawed : {amount}\n")
            self.transaction += 1
        else:
            print("Your Account Balance isn't enough.\n")

    def check_balance(self):

        print(f"Your Current Account Balance : {self.getbalance()}\n")

    def acc_of_customer(self):

        while self.run:

            print(
                "Option 1 : Deposit Amount.\nOption 2 : Withdraw Amount.\nOption 3 : Check Balance.\nOption 4 : Exit.\n")
            user_input = input("What do You Want To Do ?  ").lower()

            if user_input == "deposit":
                self.deposit(int(input("Enter Amount to Deposit: ")))
            elif user_input == "withdraw":
                self.withdraw(int(input("Enter Amount : ")))
            elif user_input == "check":
                self.check_balance()
            elif user_input == "exit":
                self.run = False
            else:
                print("This Option Is Not In List.Please Select From List.\n")
