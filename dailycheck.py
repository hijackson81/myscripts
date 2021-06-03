import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from datetime import date

### Caculation
assigned_name = ""
assigned_email = ""
start_date = date(2000, 1, 1)
today = date.today()

delta = today - start_date

if delta.days % 5 == 0:
    assigned_name = "Jackson"
    assigned_email = "jackson@gmail.com"
if delta.days % 5 == 1:
    assigned_name = "Mal"
    assigned_email = "mal@gmail.com"
if delta.days % 5 == 2:
    assigned_name = "Alley"
    assigned_email = "alley@gmail.com"
if delta.days % 5 == 3:
    assigned_name = "Bob"
    assigned_email = "bob@gmail.com"
if delta.days % 5 == 4:
    assigned_name = "Thomas"
    assigned_email = "thosmas@gmail.com"

email_sender_account = "sender@gmail.com" #your email
email_sender_username = "sender@gmail.com"  #your email username
email_sender_password = "mypassword"#your email password
email_smtp_server = "smtp.gmail.com" #change if not gmail.
email_smtp_port = 587 #change if needed.
email_recepients = [assigned_email,"otheremail@gmail.com"] #your receipts



def SendEmail (assigned_name,today):
    email_subject = f"{assigned_name} - Please Do Daily Health Check"
    email_body = '<html><head></head><body>'
    email_body += '<style type="text/css"></style>' 
    email_body += '<h2>Daily Health Check Reminder</h2>' 
    #Performer
    email_body += f'<h1 style="color: rgb(207, 29, 29);">' 
    email_body += f'<b>Performer</b>: ' 
    email_body += f'{assigned_name}</h1>' 
    #Date
    email_body += f'<h2 style="color: rgb(96, 136, 247);">' 
    email_body += f'<b>Date</b>: ' 
    email_body += f'{today}</h2>' 

    #Link
    email_body += '<h2><a href="https://google.com">Click Here To View Schedule</a> '
    email_body += '</h2>' 

    #footer
    email_body += '<br>Reminded By' 
    email_body += '<br>PYTHON SCRIPT</body></html>'
    server = smtplib.SMTP(email_smtp_server,email_smtp_port) 
    print(f"Logging in to {email_sender_account}")
    server.starttls() 
    server.login(email_sender_username, email_sender_password)
    for recipient in email_recepients:
        print(f"Sending email to {recipient}")
        message = MIMEMultipart('alternative') 
        message['From'] = email_sender_account 
        message['To'] = recipient 
        message['Subject'] = email_subject 
        message.attach(MIMEText(email_body, 'html')) 
        server.sendmail(email_sender_account,recipient,message.as_string())
    server.quit()

SendEmail(assigned_name,today)
print(f"End")