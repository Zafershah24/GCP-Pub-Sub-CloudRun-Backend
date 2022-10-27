
import smtplib
from email.mime.text import MIMEText

s = smtplib.SMTP("arl.xxxxx.com", 25)
# s.set_debuglevel(1)
s.login("xxxx@ford.com", "hQvWxxxxxxJTHN")

sender = 'gxxxxxe@ford.com'


def recipients_list_sender(recipientList:list, message):
  msg = MIMEText(message)
  
  recipients = recipientList
  msg['Subject'] = "GCP Alert"
  msg['From'] = sender
  msg['To'] = ", ".join(recipients)
  s.sendmail(sender, recipients, msg.as_string())
  print("email Sent!")


# recipients_list_sender(['szafersa'],'hello')
