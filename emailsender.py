
import smtplib
from email.mime.text import MIMEText

s = smtplib.SMTP("arl.xxxxx.com", 25)
# s.set_debuglevel(1)
s.login("xxxx@ford.com", "hQvWxxxxxxJTHN")

sender = 'gxxxxxe@ford.com'


def recipients_list_sender(recipientList:list, message):
  try:
    s = smtplib.SMTP("arxxxxxx.com", 25)
    s.set_debuglevel(1)
    s.starttls()
    s.login("gxxxxxxxxxxxx@ford.com", "xxxxxxxxxxxxxxxxxxTHN")

    sender = 'gxxxxxxxxxxxx@ford.com'
    msg = MIMEText(message)
  
    recipients = recipientList
    msg['Subject'] = "GCP Alert"
    msg['From'] = sender
    msg['To'] = ", ".join(recipients)
    s.sendmail(sender, recipients, msg.as_string())
    print("email Sent!")
    s.quit()
  except:
    print("An error has occurred")


# recipients_list_sender(['szafersa'],'hello')
