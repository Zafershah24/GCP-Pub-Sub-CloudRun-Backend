
import smtplib
from email.mime.text import MIMEText
# import webex
s = smtplib.SMTP("arl.azell.com", 25)
# s.set_debuglevel(1)
s.login("", "")

sender = ''


def recipients_list_sender(recipient, message,event_subject="GCP Alert"):
  try:
    s = smtplib.SMTP("", )
    # s.set_debuglevel(1)
    print(message)
    s.starttls()
    s.login("", "")
    recipientList=[]
    recipientList.append(recipient)
    sender = ''
    msg = MIMEText(message,'html')
  
    recipients = recipientList
    msg['Subject'] = event_subject
    msg['From'] = sender
    msg['To'] = ", ".join(recipients)
    s.sendmail(sender, recipients, msg.as_string())
    # webex.webexpush(recipientList,event_subject,message)
    print("email Sent!")
    s.quit()
  except:
    print("An error has occurred")
