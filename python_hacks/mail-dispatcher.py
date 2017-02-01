import smtplib
import getpass
import sys
import pandas as pd
import io
import math
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from email.MIMEBase import MIMEBase
from email import encoders

 
fromaddr=raw_input("\nenter sender's mail address:\t")
password=getpass.getpass() 

select=raw_input("\nDo you wish to send mail to multiple people?yes or no\n")
if(select=='no'):
    toaddr=raw_input("\nenter reciever's mail address\t")
    multiple='no'
    
else:
    val=raw_input("enter the filename.csv that contain email as its column\n")
    df = pd.read_csv(val, usecols=['email'])
    #print(df)
    #print type(df)

    a=df.values.tolist()




    flattened = [val for sublist in a for val in sublist]
    
    multiple='yes'
    #print flattened


    
    
    


    
subject=raw_input("\n enter the mail subject:\t")



 
msg = MIMEMultipart()
 
msg['From'] = fromaddr



msg['Subject'] = subject



print("\nenter the body of the mail:(type'quit' to send the mail it)")
buffer = []
while True:
    line = sys.stdin.readline().rstrip('\n')
    if line == 'quit':
        break
    else:
        buffer.append(line)

body=''
for i in buffer:
    i=i+'\n'
    body=body+i
    
select=raw_input("Do you need to send an attachment? yes or no\n")

if(select=='yes'):
    filename=raw_input("enter the file name to be attached make sure this file is present in same directory as this script\n")
    attachment = open(filename, "rb")
 
    part = MIMEBase('application', 'octet-stream')
    part.set_payload((attachment).read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', "attachment; filename= %s" % filename)
 
    msg.attach(part)

print("please wait the message is being sent......")
 
msg.attach(MIMEText(body, 'plain'))
 


 
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(fromaddr, password)
text = msg.as_string()

if(multiple=='no'):
    msg['To'] = toaddr
    server.sendmail(fromaddr, toaddr, text)
    
else:
    for toaddr in flattened:
        msg['To'] = toaddr
        server.sendmail(fromaddr, toaddr, text)
        
server.quit()
print("the message has been sent successfully")
