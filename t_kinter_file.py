import tkinter as tk

# Sample movie data
movies = ["Movie 1", "Movie 2", "Movie 3"]
formats = ["Standard", "IMAX", "Dolby"]
showtimes = ["10:00 AM", "2:00 PM", "6:00 PM"]
theaters = ["Theater 1", "Theater 2"]

# Dictionary to store ticket prices
ticket_prices = {
    "Standard": 10,
    "IMAX": 15,
    "Dolby": 12,
}

# Initialize user_info dictionary (you can replace this with your own user management)
user_info = {'bookings': {}}

# Function to book a ticket
def book_ticket():
    selected_movie = movie_var.get()
    selected_format = format_var.get()
    selected_showtime = showtime_var.get()
    selected_theater = theater_var.get()
    row = row_entry.get()
    seat = seat_entry.get()

    # Calculate the ticket price
    ticket_price = ticket_prices[selected_format]

    # Create a booking key
    booking_key = f"{selected_movie}-{selected_format}-{selected_showtime}-{selected_theater}"

    # Create a new booking entry
    if booking_key not in user_info['bookings']:
        user_info['bookings'][booking_key] = []

    user_info['bookings'][booking_key].append({
        'seat': f"Row {row}, Seat {seat}",
        'price': ticket_price,
    })

    # Update the booking listbox
    update_booking_list()

    # Clear entry fields after booking
    row_entry.delete(0, tk.END)
    seat_entry.delete(0, tk.END)

    # Update a label or display a confirmation message
    confirmation_label.config(text="Booking Successful!")

# Function to update the booking listbox
def update_booking_list():
    booking_listbox.delete(0, tk.END)
    for key, bookings in user_info['bookings'].items():
        for booking in bookings:
            booking_listbox.insert(tk.END, f"Movie: {key}, {booking['seat']}, Price: ${booking['price']}")

# Create a Tkinter window
window = tk.Tk()
window.title("Movie Ticket Booking")

# Create Tkinter variables for dropdowns
movie_var = tk.StringVar(window)
format_var = tk.StringVar(window)
showtime_var = tk.StringVar(window)
theater_var = tk.StringVar(window)

# Create labels
tk.Label(window, text="Select Movie:").pack()
movie_dropdown = tk.OptionMenu(window, movie_var, *movies)
movie_dropdown.pack()

tk.Label(window, text="Select Format:").pack()
format_dropdown = tk.OptionMenu(window, format_var, *formats)
format_dropdown.pack()

tk.Label(window, text="Select Showtime:").pack()
showtime_dropdown = tk.OptionMenu(window, showtime_var, *showtimes)
showtime_dropdown.pack()

tk.Label(window, text="Select Theater:").pack()
theater_dropdown = tk.OptionMenu(window, theater_var, *theaters)
theater_dropdown.pack()

tk.Label(window, text="Enter Row:").pack()
row_entry = tk.Entry(window)
row_entry.pack()

tk.Label(window, text="Enter Seat:").pack()
seat_entry = tk.Entry(window)
seat_entry.pack()

# Booking button
book_button = tk.Button(window, text="Book Ticket", command=book_ticket)
book_button.pack()

# Confirmation label
confirmation_label = tk.Label(window, text="")
confirmation_label.pack()

# Booking listbox
booking_listbox = tk.Listbox(window, width=40, height=10)
booking_listbox.pack()

# Initialize the booking listbox
update_booking_list()

# Start the Tkinter main loop
window.mainloop()
