

#importing re and date and time

import re
from datetime import datetime

class BankAccount:
    def __init__(self, account_number, f_name, l_name, email_id, date_of_birth, permanent_address, residential_address, adhaar_number, pan_number, account_balance):
        self.account_number = account_number
        self.f_name = f_name
        self.l_name = l_name
        self.email_id = email_id
        self.date_of_birth = date_of_birth
        self.permanent_address = permanent_address
        self.residential_address = residential_address
        self.adhaar_number = adhaar_number
        self.pan_number = pan_number
        self.account_balance = account_balance

    def display_info(self):
        print("---welcome to our bank---")

        print("--- Account Details ---")
        print(f"Account Number: {self.account_number}")
        print(f"Name: {self.f_name} {self.l_name}")
        print(f"Email: {self.email_id}")
        print(f"Date of Birth: {self.date_of_birth}")
        print(f"Permanent Address: {self.permanent_address}")
        print(f"Residential Address: {self.residential_address}")
        print(f"Aadhaar Number: {self.adhaar_number}")
        print(f"PAN Number: {self.pan_number}")
        print(f"Balance: ₹{self.account_balance}")

    def deposit(self, amount):
        if amount > 0:
            self.account_balance += amount
            print(f"An amount of ₹{amount} deposited successfully! your New balance is : ₹{self.account_balance}")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if 0 < amount <= self.account_balance:
            self.account_balance -= amount
            print(f"An amount of ₹{amount} withdrawn successfully! your Remaining bank balance is: ₹{self.account_balance}")
        else:
            print("Invalid withdrawal amount or insufficient balance in your account.")

    def get_balance(self):
        print(f"Your Current account Balance is: ₹{self.account_balance}")
        return self.account_balance


#it is the dictionary to store all the accounts
accounts = {}


#to validate the conditions we given for the adhaar and pan and age


def is_valid_account_number(acc_number):
    return acc_number.isdigit() and len(acc_number) == 16


def is_valid_name(name):
    return name.isalpha() and len(name) > 1  # Only letters, minimum 2 characters

def is_valid_aadhaar(aadhaar):
    return aadhaar.isdigit() and len(aadhaar) == 12  # Exactly 12 digits

def is_valid_pan(pan):
    pattern = r'^[A-Z]{5}[0-9]{4}[A-Z]$'
    return re.match(pattern, pan) is not None


def is_valid_age(dob):
    try:
        birth_date = datetime.strptime(dob, "%d-%m-%Y")
        today = datetime.today()
        age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
        return age >= 18
    except ValueError:
        return False

def is_valid_email(email):
    return re.match(r"[^@]+@[^@]+\.[^@]+", email)


def create_account():
    print("--- Welcome to Our Bank! ---")

    while True:
        acc_number = input("Enter your  16-digit account number here: ")
        if not is_valid_account_number(acc_number):
            print("Invalid account number! It must be exactly 16 digits.")
        elif acc_number in accounts:
            print("Account number already exists. Try again.")
        else:
            break

    fname = input(" Please Enter your first name: ")
    if not is_valid_name(fname):
        print("Invalid first name! Only letters are allowed.")
        return

    lname = input("Please Enter your last name: ")
    if not is_valid_name(lname):
        print("Invalid last name! Only letters are allowed.")
        return

    email = input("Please Enter your  email ID: ")
    if not is_valid_email(email):
        print("You have entered the Invalid email format! please check again ")
        return

    dob = input("Please Enter date of birth here (DD-MM-YYYY): ")
    if not is_valid_age(dob):
        print("You must be at least 18 years old to open an account.")
        return

    perm_address = input("Please Enter your permanent address here: ")
    res_address = input(" Please Enter your residential address here: ")

    aadhaar = input("Please Enter your Aadhaar number here: ")
    if not is_valid_aadhaar(aadhaar):
        print("Invalid Aadhaar number! It must be exactly 12 digits please try again!!.")
        return

    while True:
        pan = input("Please Enter your PAN number here (Format should be like this please check once--CMWPV7907H): ")
        if is_valid_pan(pan):
            break  # Valid PAN, exit loop
        else:
            print("You have entered Invalid PAN format. Please Try again.")

    balance = float(input("Enter your  initial deposit amount to be added to your account: "))
    print("you have sucessfully created your account have a nice day")

    # accounts[acc_number] = BankAccount(acc_number, fname, lname, email, dob, perm_address, res_address, aadhaar, pan, balance)
    # print("You have Successfully created your account Have a nice day!")
    # accounts[acc_number].display_info()



def access_account():
    acc_number = input("Enter account number: ")
    if acc_number in accounts:
        account = accounts[acc_number]
        while True:
            print("\n--- Account Menu ---")
            print("1. Deposit")
            print("2. Withdraw")
            print("3. Check Balance")
            print("4. View Account Details")
            print("5. Exit")

            choice = input("Choose an option: ")
            if choice == '1':
                amount = float(input("Enter deposit amount: ₹"))
                account.deposit(amount)
            elif choice == '2':
                amount = float(input("Enter withdrawal amount: ₹"))
                account.withdraw(amount)
            elif choice == '3':
                account.get_balance()
            elif choice == '4':
                account.display_info()
            elif choice == '5':
                print("Exiting account menu...")
                break
            else:
                print("Invalid choice! Try again.")
    else:
        print("Account not found.")


#main programm
while True:
    print("---SBI Bank Account Application ---")
    print("1. Create an Account")
    print("2. Access your Account")
    print("3. Exit")

    option = input("Select an option: ")
    if option == '1':
        create_account()
    elif option == '2':
        access_account()
    elif option == '3':
        print("Exiting... Thank you for banking with SBI! have a nice day ")
        break
    else:
        print("Invalid option! Please try again.")



