import smtplib
from email.message import EmailMessage

def email_alert(subject,body,to):
    msg=EmailMessage()
    msg.set_content(body)
    msg['subject']  =subject
    msg['to']=to

    user = ""#mail id input
    password ="" #password input
    msg ['from']= user

    server = smtplib.SMTP("smtp.gmail.com",587)
    server.starttls()
    server.login(user,password)
    server.send_message(msg)
    server.quit


mail=["surenthirakumark.ece2023@citchennai.net,vishald.ece2023@citchennai.net"]
if __name__ == '__main__':
    subject = input("subject of the mail: ")  # subject input
    message = input("what is the message: ") #content input 
    print("sending...")
    for i in mail:
        email_alert(subject,message,i)
    print("message has been successfully send")
test_test=input()

