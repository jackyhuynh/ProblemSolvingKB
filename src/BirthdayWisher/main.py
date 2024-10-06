import random
import smtplib
import datetime as dt

MY_EMAIL = "youremail@gmail.com"
MY_PASSWORD = 'Yourpassword'

now = dt.datetime.now()
weekday = now.weekday()
if weekday in range(1, 6):
    with open("quotes.txt") as quote_file:
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes)

    print(quote)
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        # encrypt the connection, secure it
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs='jackyhuynh87@gmail.com',
            msg=f'Subject:Monday Motivation\n\n{quote}'
        )
