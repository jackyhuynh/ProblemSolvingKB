import random
import smtplib
import datetime as dt


MY_EMAIL = "truclhuynh87@gmail.com"
MY_PASSWORD = 'Gookhongbiet88'

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
            to_addrs='rongcon_armani@yahoo.com',
            msg=f'Subject:Monday Motivation\n\n{quote}'
        )
