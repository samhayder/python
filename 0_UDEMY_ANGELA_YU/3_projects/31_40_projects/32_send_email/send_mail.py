import smtplib

my_mail = "sams.seul@gmail.com"
password = "ugji mwpp xaig kacr"

""" Gmail: smtp.gmail.com
Hotmail: smtp.live.com
Outlook: outlook.office365.com
Yahoo: smtp.mail.yahoo.com """

with smtplib.SMTP(host="smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=my_mail, password=password)
    connection.sendmail(
        from_addr=my_mail,
        to_addrs="sams.seul@hotmail.com", 
        msg="Subject:SMTP\n\n to send mail by testing.")
    