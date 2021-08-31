import datetime as dt
import pandas 
import random
import smtplib

MY_EMAIL = "test95018@gmail.com"
MY_PASSWORD = "Abcd@9876"

now = dt.datetime.now()
today_month = now.month
today_day = now.day
today_tuple = (today_month , today_day)

data = pandas.read_csv("birthdays.csv")

birthday_dict = {(data_row["month"], data_row["day"]) : data_row for (index , data_row) in data.iterrows()}


if today_tuple in birthday_dict:
    birthday_person = birthday_dict[today_tuple]
    file_path = f"letter_tempelates/letter_{random.randint(1,3)}.txt"
    with open(file_path) as letter_file:
        contents = letter_file.read()
        contents.replace("[NAME]" , birthday_person["name"])
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(MY_EMAIL , MY_PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL , to_addrs=birthday_person["email"] , msg=f"Subject:Happy Birthday!\n\n{contents}")

        



