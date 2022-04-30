import smtplib
import datetime as dt
import random

MY_EMAIL = "Removed Regals Email"
MY_PASSWORD = "Removed Regals PW"

now = dt.datetime.now()
weekday = now.weekday()
if weekday == 0: #0 would be Monday, 1 would be Tuesday, 2 would be Wednesday.
    with open("quotes.txt") as quote_file:
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes)

    print(quote)
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL,
                            to_addrs=MY_EMAIL, msg=f"Subject:Monday Motivation\n\n{quote}")






#smpt info , smpt.gmail.com , smtp.live.com for hotmail, smtp.mail.yahoo.com

# my_email = "bape615@gmail.com"
# password = "regal7410"
#
# with smtplib.SMTP("smtp.gmail.com")as connection:
#     connection.starttls()
#     connection.login(user=my_email, password=password)
#     connection.sendmail(from_addr=my_email,
#                         to_addrs="regalchhit@gmail.com", msg="Subject:Hello\n\nThis is the body of my email.")

# now = dt.datetime.now()
# year = now.year
# month = now.month
# day_of_week = now.weekday()
# if year == 2021:
#     print("Wear a mask")
#     print(now)
#     print(year)
# print(day_of_week)
# date_of_birth = dt.datetime(year=1995, month=12, day=15, hour=4)
# print(date_of_birth)