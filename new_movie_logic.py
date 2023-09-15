import datetime 
import re 
import sys
import Movie_SMS as MS

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

#define info about movies:

movie_info = {
    'jawan': 'A man is driven by a personal vendetta to rectify the wrongs in society, while keeping a promise made years ago. He comes up against a monstrous outlaw with no fear, who has caused extreme suffering to many',
    'oppenheimer': "During World War II, Lt. Gen. Leslie Groves Jr. appoints physicist J. Robert Oppenheimer to work on the top-secret Manhattan Project. Oppenheimer and a team of scientists spend years developing and designing the atomic bomb. Their work comes to fruition on July 16, 1945, as they witness the world's first nuclear explosion, forever changing the course of history.",
    'mission Impossible': "Ethan Hunt and the IMF team must track down a terrifying new weapon that threatens all of humanity if it falls into the wrong hands. With control of the future and the fate of the world at stake, a deadly race around the globe begins. Confronted by a mysterious, all-powerful enemy, Ethan is forced to consider that nothing can matter more than the mission -- not even the lives of those he cares about most.",
    'barbie': "Barbie and Ken are having the time of their lives in the colorful and seemingly perfect world of Barbie Land. However, when they get a chance to go to the real world, they soon discover the joys and perils of living among humans."
}
# Define theater layouts with "X" for available seats
global theater_layouts
theater_layouts = {'East': 
                   {'Jawan': 
                    { 'IMAX': [
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

                    'Oppenheimer': {
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

                    'Mission Impossible': {
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

                    'Barbie': {
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
                    }
       
    },
    'West': {
        'Jawan': { 
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

        'Oppenheimer': {
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

        'Mission Impossible': {
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

        'Barbie': {
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
        }
    },
    'North': {
        'Jawan': { 
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

        'Oppenheimer': {
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

        'Mission Impossible': {
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

        'Barbie': {
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
        }
    },
    'South': {
        'Jawan': { 
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

        'Oppenheimer': {
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

        'Mission Impossible': {
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

        'Barbie': {
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
        }
    }
}



# Function to display the theater layout
def display_theater_layout(theater_name, movie_format, selected_movie_name):

    print(f"theater:{theater_name}, format:{movie_format}, movie:{selected_movie_name}")

    print("\nTheatre Layout:")

    if movie_format in theater_layouts[theater_name][selected_movie_name]:
        layout = theater_layouts[theater_name][selected_movie_name][movie_format]
        for row in layout:
            print(' '.join(row))


customers = {}

def display_movies():
    print("\nWelcome to Sai's Cinemas! Here are the Latest Blockbusters:")
    for movie, info in movies.items():
        print(f"{movie} ({', '.join(info['formats'])} format)")

    w_ask = input("Would you like to view information about the movies?: ")

    if w_ask == 'y':
        while True:
            q_ask = input("Please type in the movie name: ").strip().lower()

            if q_ask == "jawan":
                print(f"{movie_info[q_ask]}")
                break
            elif q_ask == "oppenheimer":
                print(f"{movie_info[q_ask]}")
                break
            elif q_ask == 'mission impossible':
                print(f"{movie_info[q_ask]}")
                break
            elif q_ask == "barbie":
                print(f"{movie_info[q_ask]}")
                break
            elif q_ask in upcoming_movies:
                print("Looks like you got superpowers! Those movies aint released yet, hun. ")
            elif q_ask == 'q':
                main()
                
            else: 
                print("Wrong movie! Try again!")
                q_ask


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

    o_ask = input("Would you like to check out? ")

    if o_ask == 'y':
        print(f"An OTP has been sent to phone number ending with {customers[user_phone]['phone_num'][-4::]}")

        global otp
        otp = MS.sending_OTP()

        otp_ask = input("Please enter the OTP given to you: ")

        if otp_ask == otp:
            calculate_total_amount(ticket_price)
            main()
        
        else: 
            while otp_ask != otp:
                print("ERROR: Please retry!")










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
        global formats
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
    global selected_movie
    selected_movie, movie_info = list(movies.items())[movie_choice - 1]
 
    formats = movie_info['formats']
    showtimes = movie_info['showtimes']

    # Display the available formats for the selected movie
    print(f"\nSelected Movie: {selected_movie}")
    print(f"Available Formats: {', '.join(formats)}")

    # Ask the user to select a format
    while True:
        global selected_format
        selected_format = input("Enter the format you want to book (e.g., IMAX): ").strip()
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
        global theater
        theater = input("Enter the theater you want to book (e.g., East): ")
        if theater in theater_layouts:
            break
        else:
            print("Invalid theater or format selection. Please choose a valid combination.")

    # Display the theater layout
    display_theater_layout(theater, selected_format, selected_movie)

    # Ask the user to select a seat
    while True:
        try:
            row = int(input("Enter the row number (e.g., 1): "))
            seat = int(input("Enter the seat number (e.g., 1): "))

            
            global theater_layout
            theater_layout = theater_layouts[theater][selected_movie][selected_format]
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
    global ticket_price
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

    a_ask = input("Would you like to book another ticket?: ")

    if a_ask == 'y' or a_ask == 'yes':
        book_ticket()
    else:
        main()

def calculate_total_amount(ticket_price):
    
    GST = 0.08
    

    convinience_fee = 2

    total_price = {} #create empty dictionary for total price. 
    dict_vals = list(total_price.values())

    for price in dict_vals:
        total_price.append(ticket_price)

    subtotal_price = sum(total_price)

    #final price after GST + convinience fees

    final_price = (subtotal_price * GST) + convinience_fee

    print(f"GST is: {0.08 * (subtotal_price + convinience_fee)}\n")
    print(f"Subtotal price: {subtotal_price}")
    print(f"Convinience fee: {convinience_fee}")
    print(f"Final Price: {final_price}")

    total_price.clear()



    return total_price, subtotal_price, final_price
    






def main(): 

    while True: 
        print("\n Welcome to Sai's cinemas! Choose the below actions:")
        print("1. Display Movies/ Upcoming movies")
        print("2. Sign Up")
        print("3. Book Tickets")
        print("4. View Member Info")
        print("5. Exit")

        choice = input("Please enter your choice: ")

        if choice == '1':
            display_movies()
            z_ask = input("Would you like to view upcoming releases?: ")

            if z_ask == 'y':
                display_upcoming_movies()
            else:
                main()
        elif choice == '2':
            sign_up_for_membership()
        elif choice == '3':
            book_ticket()                    
        elif choice == '4':
            view_member_info()
        elif choice == '5':
            print("\n Thank you for visiting Sai's Cinemas! Goodbye!")

            sys.exit()
        else:
            print('Invalid choice, please try again!')

if __name__ == "__main__":
    main()



        

            
