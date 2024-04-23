import datetime
import re


def is_valid_phone_number(phone_number):
    return re.match(r"^\d{8}$", phone_number)

def is_valid_email(email):
    return re.match(r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$", email)

def is_valid_birthdate(birthdate):
    try:
        year, month, day = map(int, birthdate.split('-'))
        date_obj = datetime.date(year, month, day)
        current_year = datetime.date.today().year

        if year < 1900 or year > current_year:
            return False

        if month < 1 or month > 12:
            return False

        if day < 1 or day > 31:
            return False

        # Check for February 30 and February 31
        if month == 2 and day > 29:
            return False

        # Check for months with 30 days
        if month in [4, 6, 9, 11] and day > 30:
            return False

        return True

    except ValueError:
        return False



users_info = {}  
#we append any new information to the empty cart above
def sign_up_for_membership():
    print("\n=== SIGN UP  ===")

    #user specific ditionary 
    new_user = {}

    while True:
        phone_number = input("Enter your phone number (or 'q' to quit): ")
        if phone_number.lower() == 'q':
            return False
        if is_valid_phone_number(phone_number):
            new_user['phone_num'] = phone_number
            break
        print("Invalid phone number format. Please enter a valid phone number.")

    email = input("Enter your email (or 'q' to quit): ")
    if email.lower() == 'q':
        return False
    while not is_valid_email(email):
        print("Invalid email format. Please enter a valid email address.")
        email = input("Enter your email (e.g., example@example.com, or 'q' to quit): ")
        if email.lower() == 'q':
            return False
    else:
        new_user['email'] = email

    full_name = input("Enter your full name as on NRIC: ")
    new_user['name'] = full_name

    while True:
        age_str = input("Enter your age: ")
        if age_str.isdigit():
            age = int(age_str)
            new_user["age"] = age
            break
        else:
            print("Invalid age. Please enter a valid number.")

    while True:
        credit_card = input("Please enter your 16 digit credit card number: ")
        if len(credit_card) != 16:
            print('ERROR: Please input a valid 16 digit Credit Card Number')
        else: 
            new_user['credit_card_num'] = credit_card
            break

    while True:
        CVV_number = input("Please enter your CVV Number: ")
        if len(CVV_number) != 3:
            print("ERROR: Please input Valid CVV number")
        else:
            new_user['cvv_num'] = CVV_number
            break

if __name__ == "__main__":
    sign_up_for_membership()