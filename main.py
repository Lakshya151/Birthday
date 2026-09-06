import smtplib
import datetime as dt
import pandas

import os

my_mail = os.environ["EMAIL"]
password = os.environ["APP_PASSWORD"]



today=(dt.datetime.now().month,dt.datetime.now().day)

data=pandas.read_csv("birthdays.csv")

bday_dict={(data_row["month"],data_row["day"]) :data_row for (index,data_row)  in data.iterrows()}



if today in bday_dict:
    today_bdy=bday_dict[today]
    with smtplib.SMTP("smtp.gmail.com",587) as connection:
        connection.starttls()
        connection.login(my_mail,password)
        connection.sendmail(from_addr=my_mail,to_addrs=my_mail,
                            msg=f"Subject: Birthday Reminder\nHello\nToday is the birthday of {today_bdy['name']}")