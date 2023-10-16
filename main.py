import pandas
import datetime as dt
import random
import smtplib

date = dt.datetime.now()
today = (date.month, date.day)
USER_EMAIL = "YOUR EMAIL"
PASS = "PASS"

birth_days = pandas.read_csv("birthdays.csv")
birthdays = {(data_row['month'], data_row['day']): data_row for (index, data_row) in birth_days.iterrows()}

letters = ["letter_1.txt", "letter_2.txt", "letter_3.txt"]

if today in birthdays:
    with open(f"letter_templates/{random.choice(letters)}") as data:
        content = data.read()

    person_info = birthdays[today]
    letter = content.replace("[NAME]", person_info["name"])
    letter = letter.replace("Name", "YOUR NAME")

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=USER_EMAIL, password=PASS)
        connection.sendmail(from_addr=USER_EMAIL,
                            to_addrs=person_info["email"],
                            msg=f"Subject:Happy Birthday\n\n{letter}")
