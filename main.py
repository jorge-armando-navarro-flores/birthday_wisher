import datetime as dt
import pandas as pd
import random
import smtplib
from keys import *

now = dt.datetime.now()
# Create a tuple from today's month and day using datetime. e.g.
today = (now.month, now.day)
from_name = "Jorge"
from_email = email
from_password = password
birthdays_data = pd.read_csv("birthdays.csv")
birthdays_dict = {(data_row.month, data_row.day): data_row for (index, data_row) in birthdays_data.iterrows()}

# Check if today matches a birthday in the birthdays.csv
if today in birthdays_dict:
    file_path = f"letter_templates/letter_{random.randint(1, 3)}.txt"
    with open(file_path) as letter_file:
        birthdays_person = birthdays_dict[today]
        letter_template = letter_file.read()
        letter = letter_template.replace("[NAME]", birthdays_person["name"])
        letter = letter.replace("[FROM_NAME]", from_name)
        print(letter)

# Send email
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=from_email, password=from_password)
        connection.sendmail(
            from_addr=from_email,
            to_addrs=birthdays_person["email"],
            msg=f"Subject:Happy Birthday!\n\n{letter}"
        )




