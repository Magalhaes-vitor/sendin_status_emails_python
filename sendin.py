from smtplib import SMTP

email_to = ["recipients",'separate with a comma and put a comma after the last one']   
email_template = open("Email.html", "r", encoding="UTF-8").read()
body_text = "editable text <en>"

if body_text:
    email_template = email_template.format( "stream name", body_text )
else:
    email_template = email_template.format( "stream name","" )

try:
    msg = MIMEMultipart("alternative")
    msg['From'] = "sender"
    msg['To'] = ", ".join(email_to)
    msg['Subject'] = "email title"
    msg.attach(MIMEText(email_template, 'html'))
    
    smtp = smtplib.SMTP("smtp", 993)
    smtp.sendmail(email_from, email_to, msg.as_string()) 
    smtp.quit()
----------------------------------------------------------------------------------------------------------------------------------------------------
   ''' add your script here if it returns an error the error email will be directed to your recipient'''
----------------------------------------------------------------------------------------------------------------------------------------------------
except Exception as ex: 
    print("There was a problem sending the error email:", ex)
    raise Exception("Problem sending error email.")
else:
    print("Error email sent successfully!")}
