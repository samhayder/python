import pandas
import smtplib
import datetime
import random

##################### Extra Hard Starting Project ######################
PATH = r"0_UDEMY_ANGELA_YU/3_projects/31_40_projects/32_send_email/birthday_wisher/birthdays.csv"
HOST_MAIL = "smtp.gmail.com"
MY_EMAIL = "sams.seul@gmail.com"
MY_PASSWORD = "ugji mwpp xaig kacr"

# 1. Update the birthdays.csv
data = pandas.read_csv(PATH)
birthday_data = {(data_row["month"],data_row["day"]): data_row for (index,data_row) in data.iterrows()}

# 2. Check if today matches a birthday in the birthdays.csv
today = datetime.datetime.now()
today_tuple = (today.month, today.day)

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
if today_tuple in birthday_data:
    birthday_person =birthday_data[today_tuple]["name"]
    birthday_person_email =birthday_data[today_tuple]["email"]
    wish_path = f"0_UDEMY_ANGELA_YU/3_projects/31_40_projects/32_send_email/birthday_wisher/letter_templates/letter_{random.randint(1,3)}.txt"
    
    with open(wish_path) as file:
        content = file.read()
        content = content.replace("[NAME]",birthday_person)

# 4. Send the letter generated in step 3 to that person's email address.
    with smtplib.SMTP(host=HOST_MAIL) as conn:
        conn.starttls()
        conn.login(user=MY_EMAIL, password=MY_PASSWORD)
        conn.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=birthday_person_email,
            msg=f"Subject:Happy Birthday!\n\n{content}"
        )



