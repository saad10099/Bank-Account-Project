from Day5.current_accounts import CurrentAccounts
from Day5.saving_accounts import SavingsAccount
from bank_account import BankAccount


def main():
    user_input = input("Which Type Of Account You Want To Open (Current or Saving) ? ")

    if user_input == "current":
        user1 = CurrentAccounts()
        user1.acc_of_customer()
    elif user_input == "saving":
        user1 = SavingsAccount()
        user1.acc_of_customer()


if __name__ == "__main__":
    main()

try:
    main()
except ValueError:
    print("Invalid Input")
    main()

