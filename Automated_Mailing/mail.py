import pandas as pd
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Sender's email credentials
from_addr = 'nitanrana43@gmail.com'
email = 'nitanrana43@gmail.com'   # Enter Your email id here
password = 'Welcome@1234'           # Enter your Password

# Read recipient data from CSV
data = pd.read_csv("C:/Users/User/PycharmProjects/pythonPractice/Automated_Mailing/Email_List.csv")
to_addr = data['email'].tolist()
name = data['name'].tolist()

# Iterate through recipients
for i in range(len(name)):
    # Create email message
    msg = MIMEMultipart()
    msg['From'] = from_addr
    msg['To'] = to_addr[i]
    msg['Subject'] = 'Just to Check'

    # Email body
    body = f"{name[i]}, Hi Nitan,\nThis email is automated via Python.\nThanks!!!"
    msg.attach(MIMEText(body, 'plain'))

    # Send email
    with smtplib.SMTP('smtp.gmail.com', 587) as mail:
        mail.ehlo()
        mail.starttls()
        mail.login(email, password)
        text = msg.as_string()
        mail.sendmail(from_addr, to_addr[i], text)
