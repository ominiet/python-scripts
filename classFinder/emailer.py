import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def entryToString(entry):
    myString = "------------------------------------------\n"
    myString += "Run " + str(entry["_id"]) + " exited with code [%i]. " % entry["returnCode"]
    codeMeanings = {
        1:"Success! You are now registered for the Class",
        2:"Script success, but there were 0 seats",
        3:"Open Seat but script Failure. Please sign up now!",
        4:"Script failure after Login",
        5:"Script failure at Login"
    }
    myString += "\n Excecution Time: " + entry["runTime"].strftime("%B %d, %Y %I:%M") + "\n" + "Status Code Meaning: "
    myString += codeMeanings[entry["returnCode"]]
    myString += "------------------------------------------\n"

    return myString

def doSuccessEmail(entries, username, password,recipient):
    SMTPserver = "smtp.gmail.com:587"

    #create message object to be sent
    msg = MIMEMultipart()
    #read template file
    fp = open("./Templates/success.txt", 'rb')
    #read file
    fileString = fp.read()
    for entry in entries:
        fileString += entryToString(entry)


    txt = MIMEText(fileString)
    fp.close()
    # setup the parameters of the message
    msg['From']= username
    msg['To']= recipient
    msg['Subject']= "Success!"

    msg.attach(txt)

    s = smtplib.SMTP(SMTPserver)
    s.starttls()
    s.login(username, password)

    s.sendmail(username,recipient,msg.as_string())

    s.quit()

def doFailureEmail(entries, username,password,recipient):
    SMTPserver = "smtp.gmail.com:587"

    #create message object to be sent
    msg = MIMEMultipart()
    #read template file
    fp = open("./Templates/failure.txt", 'rb')
    #read file
    fileString = fp.read()
    for entry in entries:
        fileString += entryToString(entry)


    txt = MIMEText(fileString)
    fp.close()
    # setup the parameters of the message
    msg['From']= username
    msg['To']= recipient
    msg['Subject']= "Alert!"

    msg.attach(txt)

    s = smtplib.SMTP(SMTPserver)
    s.starttls()
    s.login(username, password)

    s.sendmail(username,recipient,msg.as_string())

    s.quit()

def doBasicEmail(entries, username,password,recipient):
    SMTPserver = "smtp.gmail.com:587"

    #create message object to be sent
    msg = MIMEMultipart()
    #read template file
    fp = open("./Templates/basic.txt", 'rb')
    #read file
    fileString = fp.read()
    for entry in entries:
        fileString += entryToString(entry)


    txt = MIMEText(fileString)
    fp.close()
    # setup the parameters of the message
    msg['From']= username
    msg['To']= recipient
    msg['Subject']= "Last 48 log entries"

    msg.attach(txt)

    s = smtplib.SMTP(SMTPserver)
    s.starttls()
    s.login(username, password)

    s.sendmail(username,recipient,msg.as_string())

    s.quit()
