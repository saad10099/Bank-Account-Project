from bank_account import BankAccount


class SavingsAccount(BankAccount):

    def __init__(self):
        super().__init__()

    def interest_rate(self):

        interest = (self.getbalance() / 100) * 0.8
        self.setbalance(self.getbalance() + interest)
        print(f"Your Interest On Total Balance Is: {interest}PKR\n")

    def minimum_deposit_for_1st_time(self, amount):

        if self.getbalance() == 0:
            if amount >= 50_000:
                self.setbalance(amount)
                self.interest_rate()
                self.transaction += 1
            else:
                print("Minimum 50,000PKR Is Required At First Deposit.\n")
        else:
            self.deposit(amount)
            self.interest_rate()
            self.transaction += 1

    def limit_withdraw(self):

        if self.transaction > 10:
            self.setbalance(self.getbalance() - 25)
            print("You Have Cross Your Saving Account Transaction Limit,So 25PKR Is Deducted From Your Balance.\n")
        elif self.transaction > 15:
            self.setbalance(self.getbalance() - 30)
            print("You Have Cross Your Saving Account Transaction Limit,So 30PKR Is Deducted From Your Balance.\n")
        elif self.transaction >= 20:
            self.setbalance(self.getbalance() - 35)
            print("You Have Cross Your Saving Account Transaction Limit,So 35PKR Is Deducted From Your Balance.\n")


    def acc_of_customer(self):


        while self.run:

            print(
                "Option 1 : Deposit Amount.\nOption 2 : Withdraw Amount.\nOption 3 : Check Balance.\nOption 4 : Exit.\n")
            user_input = input("What do You Want To Do ?  ").lower()

            if user_input == "deposit":
                print(f"If U are Depositing Money 1st Time In This Bank,Make Sure tO Deposit At Least 50,000PKR ")
                self.minimum_deposit_for_1st_time(int(input("Enter Amount to Deposit: ")))
            elif user_input == "withdraw":
                self.withdraw(int(input("Enter Amount : ")))
                self.limit_withdraw()
            elif user_input == "check ":
                self.check_balance()
            elif user_input == "exit":
                self.run = False
            else:
                print("This Option Is Not In List.Please Select From List.\n")