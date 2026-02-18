import smtplib
import random
import datetime

HOST_MAIL = "smtp.gmail.com"
MY_EMAIL = "sams.seul@gmail.com"
MY_PASSWORD = "ugji mwpp xaig kacr"
PATH = r"0_UDEMY_ANGELA_YU/3_projects/31_40_projects/32_send_email/quotes.txt"

now = datetime.datetime.now()
weekday = now.weekday()

if weekday == 2:
    with open(PATH, encoding="utf-8", errors="ignore") as quote_file:
        quote_lists = quote_file.read().splitlines()
        quote = random.choice(quote_lists)
    
    with smtplib.SMTP(host=HOST_MAIL) as conn:
        conn.starttls()
        conn.login(user=MY_EMAIL, password=MY_PASSWORD)
        conn.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg=f"Subject:Motivational Quote\n\n{quote.encode("ascii", errors="replace")}"
            )