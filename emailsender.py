import smtplib
from email.mime.text import MIMEText

s = smtplib.SMTP("arl.azell.com", 25)
# s.set_debuglevel(1)
s.login("", "h")

sender = ''


def recipients_list_sender(recipientList:list, message,event_subject="GCP Alert"):
  try:
    s = smtplib.SMTP("arl.azell.com", 25)
    # s.set_debuglevel(1)
    print(message)
    s.starttls()
    s.login("gcp", "N")

    sender = 'gcp'
    msg = MIMEText(message,'html')
  
    recipients = recipientList
    msg['Subject'] = event_subject
    msg['From'] = sender
    msg['To'] = ", ".join(recipients)
    s.sendmail(sender, recipients, msg.as_string())
    print("email Sent!")
    s.quit()
  except:
    print("An error has occurred")
