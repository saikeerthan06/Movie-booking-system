from twilio.rest import Client
import random



authtoken = '124a026257f53674388335c379f7f052'
accountsid = 'AC75c52143f1ac3029c12dbf14308780f8'


def generate_otp():
  otp = ""
  for i in range(5):
     otp += str(random.randint(0, 9))
  return otp



def sending_OTP():
  #this is a function to send OTP to user's number so that he can proceed with the checkout

  otp = generate_otp()

  account_sid = accountsid
  auth_token = authtoken

  client = Client(account_sid, auth_token)

  message = client.messages.create(
        from_='+12566702723',  
        body= f"{otp}" ,  
        to= "+6581838924"    
  )

  return otp





def confirm_ticket(selected_movie, selected_format, showtime, theater):


  account_sid = accountsid
  auth_token = authtoken
  global message_content

  movie_details = f"{selected_movie} ({selected_format}) at {showtime} in {theater} theatre"

  message_content = f"Ticket(s) for {movie_details} is processed! Thank you for choosing Sai's Cinemas! "



  
  

  client = Client(account_sid, auth_token)
  message = client.messages.create(
    from_='+12566702723',  
    body=f"{message_content}",  
    to="+6581838924"   
  )

  return message_content






  

# def confirm_ticket(selected_movies, selected_formats, showtimes, theaters, bookings=[]):
#     # Function to send confirmation of tickets

#     account_sid = accountsid
#     auth_token = authtoken
#     message_content = ""

#     for booking in bookings:
#         selected_movie = booking['selected_movie']
#         selected_format = booking['selected_format']
#         showtime = booking['showtime']
#         theater = booking['theater']

#         movie_details = f"{selected_movie} ({selected_format}) at {showtime} in {theater} theatre\n"
#         message_content += movie_details  # Accumulate movie details

#     message_content += "has been processed! Thank you for watching at Sai's Cinemas!"

#     client = Client(account_sid, auth_token)
#     message = client.messages.create(
#         from_='+12566702723',   # Twilio's number, where the message comes from 
#         body=f"OTP is {message_content}",  # What the message should say
#         to="+6581838924"   # The receiver's phone number
#     )