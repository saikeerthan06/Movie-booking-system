import sign_up_page as GS
from sign_up_page import is_valid_phone_number, is_valid_email





movies = {

    'Jawan': {'format': "IMAX", "showtimes": ['10:00', '14:00', '18:00']},
    'Oppenheimer': {'format': "IMAX", "showtimes": ['11:00', '15:00', '19:00']},
    "Mision Impossible: Dead Reckoning Part One": {'format': "Dolby", "showtimes": ['10:30', '14:30', '18:30']},
    "Barbie": {'format': "Dolby", "showtimes": ["09;30", "13:30", "17:30"]}
}

theatres ={

    'IMAX': 150,
    'Dolby': 100,
    'Standard 1': 55,
    'Standard 2': 60

}


upcoming_movies = {
    'Napoleon(IMAX):': {'Release Date': ['November 22 2023']},
    'Aquaman(IMAX):': {'Release Date': ['December 16 2023']},
    'Salaar (IMAX):': {'Release Date': ['November 2023']},
    'Wonka (Dolby):': {'Release Date': ['December 15 2023']},
    'Killers Of The Flower Moon:': {'Release Date': ['October 2023']}
}


customers = {}

def display_movies():
    print("\nHere are the movies Now Playing:")
    for movie, info in movies.items():
        print(f"{movie} ({info['format']} format)")


def display_upcomingmovies():
    print("\nHere are the upcoming releases:")
    for movie, info in upcoming_movies.items():
        print(f"{movie} {', '.join(info['Release Date'])}")


def sign_up():
    print("\n=== SIGN UP ===")

    # User-specific dictionary
    new_user = {}

    while True:
        phone_number = input("Enter your phone number: ")
        if phone_number in customers:
            print("User with this phone number already exists. Please sign in.")
            return
        if is_valid_phone_number(phone_number):
            new_user['phone_num'] = phone_number
            break
        print("Invalid phone number format. Please enter a valid phone number.")

    email = input("Enter your email: ")
    while not is_valid_email(email):
        print("Invalid email format. Please enter a valid email address.")
        email = input("Enter your email (e.g., example@example.com): ")
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
        credit_card = input("Please enter your 16-digit credit card number: ")
        if len(credit_card) != 16:
            print('ERROR: Please input a valid 16-digit Credit Card Number')
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

    # Add an empty 'bookings' dictionary for the new user
    new_user['bookings'] = {}

    # Add the new user to the customers dictionary
    customers[new_user['phone_num']] = new_user
    print("Customer registered successfully.")


def view_member_info():
    phone_number = input("Enter your phone number: ")
    phone_number = str(phone_number)  # Convert to string

    if phone_number in customers:
        user = customers[phone_number]
        print("\nMember Information:")
        print(f"Name: {user['name']}")
        print(f"Phone Number: {user['phone_num']}")
        print(f"Email: {user['email']}")
        print(f"Age: {user['age']}")

        if 'bookings' in user and user['bookings']:
            print("\nYour Bookings:")
            for i, (movie, details) in enumerate(user['bookings'].items(), start=1):
                print(f"{i}. Movie: {movie}")
                print(f"   Format: {details['format']}")
                print(f"   Showtime: {details['showtime']}")
                print(f"   Theatre: {details['theatre']}")
        else:
            print("\nYou have no bookings.")
    else:
        print("User not found.")




def book_ticket():
    print("\n=== BOOK TICKET ===")

    # Display movies and their formats
    print("\nMovies Now Playing:")
    for movie, info in movies.items():
        print(f"{movie} ({info['format']} format)")

    movie = input("Enter the movie you want to book: ").strip()  # Remove leading/trailing spaces

    # Check if the selected movie is playing
    if movie in movies:
        format = movies[movie]['format']
        showtimes = ", ".join(movies[movie]['showtimes'])
        print(f"\nSelected Movie: {movie}")
        print(f"Selected Format: {format}")
        print(f"Available Showtimes: {showtimes}")
    else:
        print("\nInvalid movie selection. Please choose a valid movie.")
        return

    showtime = input("Enter the showtime you want to book (e.g., 10:00): ")

    # Check if the entered showtime is valid
    if showtime not in movies[movie]['showtimes']:
        print("\nInvalid showtime selection. Please choose a valid showtime.")
        return

    theatre = input("Enter the theatre you want to book (IMAX, Dolby, Standard 1, Standard 2): ")

    # Check if the entered theatre is valid
    if theatre not in theatres:
        print("\nInvalid theatre selection. Please choose a valid theatre.")
        return

    # Check if the selected theatre matches the movie's format
    if (theatre == 'IMAX' and format != 'IMAX') or (theatre == 'Dolby' and format != 'Dolby'):
        print("\nThe selected format is not available in this theatre.")
        return

    # Check if there are available seats in the selected theatre
    if theatres[theatre] <= 0:
        print(f"\nNo available seats left in {theatre} theatre for {movie}.")
        return

    # Reduce the available seats in the selected theatre
    theatres[theatre] -= 1

    # Prompt the user for their phone number to associate the booking
    user_phone = input("Enter your phone number: ")
    user_phone = str(user_phone)  # Convert to string
    if user_phone in customers:
        if 'bookings' not in customers[user_phone]:
            customers[user_phone]['bookings'] = {}
        customers[user_phone]['bookings'][movie] = {
            'format': format,
            'showtime': showtime,
            'theatre': theatre
        }
        print("\nTicket booked successfully.")
    else:
        print("\nUser not found. Please sign up or enter a valid phone number.")



            



def main():
    while True:
            
            if not customers:
                print('Please sign up first: ')
                sign_up()
                continue 

            print("\nWelcome to the Movie Booking System")
            print("1. Display Movies")
            print("2. Display Upcoming Movies")
            print("3. Book Ticket")
            print("4. View Member Info")
            print("5. Exit")
            choice = input("Enter your choice: ")

            if choice == '1':
                display_movies()
            elif choice == '2':
                display_upcomingmovies()
            elif choice == '3':
                book_ticket()
            elif choice == '4':
                view_member_info()
            elif choice == '5':
                print("Thank you for using the Movie Booking System. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")
                return 

if __name__ == "__main__":
    main()

