import datetime 
import re 
import sys

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
        if month == 2 and day > 29:
            return False

        # Check for months with 30 days
        if month in [4, 6, 9, 11] and day > 30:
            return False

        return True
    
    except ValueError:
        return False
        


#ticket prices:

ticket_prices = {

    'IMAX': 20,
    'Dolby': 15,
    'Standard': 10
}

#there are 4 different theatres: 

theatres = {
    'East': {
        'IMAX Hall': 421,
        'Dolby Hall': 250,
        'Standard 1': 150,
        'Standard 2': 250
    },

    'West': {

        'IMAX Hall': 500,
        'Dolby Hall': 288,
        'Standard 1': 150,
        'Standard 2': 250
    },

    'North': {
        'IMAX Hall': 500,
        'Dolby Hall': 300,
        'Standard 1': 200,
        'Standard 2': 300
    },

    'South': {
        'IMAX Hall': 475,
        'Dolby Hall': 300,
        'Standard 1': 250,
        'Standard 2': 145
    }
}

#defining movie schedule

movies = {

    'Jawan': {
        'formats': ['IMAX', 'Dolby', 'Standard'],
        'showtimes': {

            'IMAX': ['10:00', '14:00', '18:00'],
            'Dolby': ['12:00', '15:00'],
            'Standard': ['08:00', '11:00']
        },
    },

    'Oppenheimer': {

        'formats': ['IMAX', 'Dolby', 'Standard'],
        'showtimes': {

            'IMAX': ['08:00', '12:00', '16:00', '20:00'],
            'Dolby': ['16:00', '21:00'],
            'Standard': ['09:00', '13:00', '15:00', '23:00']

        },

    },

    'Mission Impossible': {

        'formats': ['IMAX', 'Dolby', 'Standard'],
        'showtimes': {

            'IMAX': ['21:00', '23:00'],
            'Dolby': ['08:00', '22:00'],
            'Standard': ['10:00', '14:00', '17:00', '23:00']
        },
    },

    'Barbie': {

        'formats': ['Dolby', 'Standard'],

        'showtimes': {

            'Dolby': ['10:00', '13:00', '17:00', '19:00', '21:00', '23:00'],
            'Standard': ['12:00', '16:00', '22:00']
        },
    },
    
}

upcoming_movies = {

    'Killers Of The Flower Moon(IMAX)': {'Release Date': ['October 2023']},
    'Napoleon(IMAX)': {'Release Date': ['November 2023']},
    'Salaar(IMAX)': {'Release Date': ['November 2023']},
    'Aquaman(IMAX, Dolby)': {'Release Date': ['December 2023']},
    'Wonka(Dolby)': {'Release Date': ['December 2023']}    
}

# Define theater layouts with "X" for available seats
theater_layouts = {
    'East': {
        'IMAX': [
            ['X', 'X', 'X', 'X', 'X'],
            ['X', 'X', 'X', 'X', 'X'],
            ['X', 'X', 'X', 'X', 'X'],
            ['X', 'X', 'X', 'X', 'X']
        ],
        'Dolby': [
            ['X', 'X', 'X', 'X', 'X'],
            ['X', 'X', 'X', 'X', 'X'],
            ['X', 'X', 'X', 'X', 'X'],
            ['X', 'X', 'X', 'X', 'X']
        ],
        'Standard': [
            ['X', 'X', 'X', 'X', 'X'],
            ['X', 'X', 'X', 'X', 'X'],
            ['X', 'X', 'X', 'X', 'X'],
            ['X', 'X', 'X', 'X', 'X']
        ]
    },
    'West': {
        'IMAX': [
            ['X', 'X', 'X', 'X'],
            ['X', 'X', 'X', 'X'],
            ['X', 'X', 'X', 'X'],
            ['X', 'X', 'X', 'X']
        ],
        'Dolby': [
            ['X', 'X', 'X', 'X'],
            ['X', 'X', 'X', 'X'],
            ['X', 'X', 'X', 'X'],
            ['X', 'X', 'X', 'X']
        ],
        'Standard': [
            ['X', 'X', 'X', 'X'],
            ['X', 'X', 'X', 'X'],
            ['X', 'X', 'X', 'X'],
            ['X', 'X', 'X', 'X']
        ]
    },
    'North': {
        'IMAX': [
            ['X', 'X', 'X'],
            ['X', 'X', 'X'],
            ['X', 'X', 'X']
        ],
        'Dolby': [
            ['X', 'X', 'X'],
            ['X', 'X', 'X'],
            ['X', 'X', 'X']
        ],
        'Standard': [
            ['X', 'X', 'X'],
            ['X', 'X', 'X'],
            ['X', 'X', 'X']
        ]
    },
    'South': {
        'IMAX': [
            ['X', 'X', 'X'],
            ['X', 'X', 'X'],
            ['X', 'X', 'X']
        ],
        'Dolby': [
            ['X', 'X', 'X'],
            ['X', 'X', 'X'],
            ['X', 'X', 'X']
        ],
        'Standard': [
            ['X', 'X', 'X'],
            ['X', 'X', 'X'],
            ['X', 'X', 'X']
        ]
    }
}

# Function to display the theater layout
def display_theater_layout(theater, selected_format):
    if theater in theater_layouts and selected_format in theater_layouts[theater]:
        print("\nTheatre Layout:")
        layout = theater_layouts[theater][selected_format]
        for row in layout:
            print(' '.join(row))
    else:
        print("Theater or format not found in the layout data.")


customers = {}

def display_movies():
    print("\nWelcome to Sai's Cinemas! Here are the Latest Blockbusters:")
    for movie, info in movies.items():
        print(f"{movie} ({', '.join(info['formats'])} format)")

def display_upcoming_movies():
    print("\nHere are the upcoming Blockbusters:")
    for movie, info in upcoming_movies.items():
        print(f"{movie} (Release Date: {', '.join(info['Release Date'])})")



def sign_up_for_membership():

    print("\n === SIGN UP ===")

    new_user = {}

    while True:

        phone_number = input("Please enter your phone number(press 'q' to quit): ")

        if phone_number.lower() == 'q':
            sys.exit()

        if is_valid_phone_number(phone_number):
            new_user['phone_num'] = phone_number
            break
        print("Invalid Phone number format. Please enter a valid one. ")

    email = input('Please input your email address(press q to quit): ')

    if email.lower() == 'q':
        print("Thank you for visitng Sai's Cinemas!")
        sys.exit()

    while not is_valid_email(email):
        print("Invalid email format. Please retry. ")

        email = input("Please enter your email address: ")

        if email == 'q':
            print("Thank you for visitng Sai's Cinemas!")
            sys.exit()

    else: 
        new_user['email'] = email

    full_name = input("Please enter your full name as per the NRIC: ")

    new_user['name'] = full_name

    while True: 

        age_str = input("Please enter your age: ")

        if age_str.isdigit(): 
            age = int(age_str)
            new_user['age'] = age
            break
        else: 
            print('Invalid age. Please enter a valid number. ')

    while True:

        credit_card = input('Please enter your 16 digit credit card number: ')

        if len(credit_card) != 16:
            print("ERROR: Please enter a valid 16 digit credit card number: ")
        
        else: 
            print("Credit Card Successfully added! ")

            new_user['credit_card_num'] = credit_card
            break 

    while True: 

        CVV_number = input("Please enter your CVV Number: ")

        if len(CVV_number) != 3: 

            print("Please enter a valid CVV number")

        else: 

            print("CVV Number successfully added!")

            new_user['CVV_num'] = CVV_number
            break

    #assign ph number to access member info 

    customers[new_user['phone_num']] = new_user
    print("\n User registeration successfull!")


def view_member_info():
    print("\n === MEMBER INFO ===")

    user_phone = input("Please enter your Phone Number: ")

    if user_phone in customers:

        user_info = customers[user_phone]

        print(f"Name: {user_info['name']}")
        print(f"Age: {user_info['age']}")
        print(f"Email: {user_info['email']}")
        print(f"Phone Number: {user_info['phone_num']}")

        if 'bookings' in user_info: 
            print("\n Your Bookings: ")

            for booking_key, booking_list in user_info['bookings'].items():
                selected_movie, selected_format, showtime, theater = booking_key.split('-')

                for booking_details in booking_list:
                    print(f"Movie Name: {selected_movie}")
                    print(f"Format: {selected_format}")
                    print(f"Showtime: {showtime}")
                    print(f"Theatre: {theater}")
                    print(f"Seat Number: {booking_details['seat']}")
                    print(f"Price: ${booking_details['price']}")
        else: 
            a_ask = input("\n No Bookings found yet! Press '1' to book tickets or '2' to go to main: ")

            if a_ask == '1':
                book_ticket()
            elif a_ask == '2':
                main()
            else:
                print("Invalid choice.")

    else: 
        print("\n User not found. Please sign up or enter a valid Phone Number!")




def book_ticket():
    print("\n=== BOOK TICKET ===")

    # Ask for user's phone number to identify the customer
    user_phone = input("Please enter your phone number: ")

    if user_phone not in customers:
        print("User not found. Please sign up or enter a valid phone number.")
        return

    # Get user information
    user_info = customers[user_phone]
    user_name = user_info['name']

    # Display available movies and formats
    print("\nMovies Now Playing:")
    for i, (movie, info) in enumerate(movies.items(), start=1):
        formats = ', '.join(info['formats'])
        print(f"{i}. {movie} ({formats} format)")

    # Ask the user to select a movie
    while True:
        try:
            movie_choice = int(input("Enter the number of the movie you want to book: "))
            if 1 <= movie_choice <= len(movies):
                break
            else:
                print("Invalid movie selection. Please choose a valid movie number.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    # Access movie details directly from the 'movies' dictionary
    selected_movie, movie_info = list(movies.items())[movie_choice - 1]
    formats = movie_info['formats']
    showtimes = movie_info['showtimes']

    # Display the available formats for the selected movie
    print(f"\nSelected Movie: {selected_movie}")
    print(f"Available Formats: {', '.join(formats)}")

    # Ask the user to select a format
    while True:
        selected_format = input("Enter the format you want to book (e.g., IMAX): ")
        if selected_format in formats:
            break
        else:
            print("Invalid format selection. Please choose a valid format.")

    # Display the available showtimes for the selected movie and format
    print("Available Showtimes:", ', '.join(showtimes[selected_format]))

    # Ask the user to select a showtime
    while True:
        showtime = input("Enter the showtime you want to book (e.g., 10:00): ")
        if showtime in showtimes[selected_format]:
            break
        else:
            print("Invalid showtime selection. Please choose a valid showtime.")

    # Ask the user to select a theater
    while True:
        theater = input("Enter the theater you want to book (e.g., East): ")
        if theater in theater_layouts and selected_format in theater_layouts[theater]:
            break
        else:
            print("Invalid theater or format selection. Please choose a valid combination.")

    # Display the theater layout
    display_theater_layout(theater, selected_format)

    # Ask the user to select a seat
    while True:
        try:
            row = int(input("Enter the row number (e.g., 1): "))
            seat = int(input("Enter the seat number (e.g., 1): "))

            theater_layout = theater_layouts[theater][selected_format]
            if 1 <= row <= len(theater_layout) and 1 <= seat <= len(theater_layout[row - 1]):
                if theater_layout[row - 1][seat - 1] == 'X':
                    theater_layout[row - 1][seat - 1] = 'O'
                    break
                else:
                    print("Seat is already booked. Please choose another seat.")
            else:
                print("Invalid seat selection. Please choose a valid seat.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    # Calculate the ticket price based on the selected format
    ticket_price = ticket_prices[selected_format]

    # Initialize the bookings dictionary if it doesn't exist
    if 'bookings' not in user_info:
        user_info['bookings'] = {}

    # Create a key for the selected movie, format, showtime, and theater combination
    booking_key = f"{selected_movie}-{selected_format}-{showtime}-{theater}"

    # Check if the key already exists in the bookings
    if booking_key not in user_info['bookings']:
        user_info['bookings'][booking_key] = []

    # Add the booking details to the user's bookings
    user_info['bookings'][booking_key].append({
        'seat': f"Row {row}, Seat {seat}",
        'price': ticket_price,
    })

    print("\nBooking Successful!")
    print(f"Movie: {selected_movie}")
    print(f"Format: {selected_format}")
    print(f"Showtime: {showtime}")
    print(f"Theater: {theater}")
    print(f"Seat: Row {row}, Seat {seat}")
    print(f"Price: ${ticket_price}")





def main(): 

    while True: 
        print("\n Welcome to Sai's cinemas! Choose the below actions:")
        print("1. Display Movies")
        print("2. Display upcoming movies")
        print("3. Sign Up")
        print("4. Book Tickets")
        print("5. View Member Info")
        print("6. Exit")

        choice = input("Please enter your choice: ")

        if choice == '1':
            display_movies()
        elif choice == '2':
            display_upcoming_movies()
        elif choice == '3':
            sign_up_for_membership()
        elif choice == '4':
            while True:
                book_ticket()
                another_ticket = input("Do you wish to book another ticket?")
                if (another_ticket.lower() == 'yes') or (another_ticket.lower() == 'y'):
                    book_ticket()
                else:
                    main()
                    
        elif choice == '5':
            view_member_info()
        elif choice == '6':
            print("\n Thank you for visiting Sai's Cinemas! Goodbye!")

            sys.exit()
        else:
            print('Invalid choice, please try again!')

if __name__ == "__main__":
    main()



        

            
