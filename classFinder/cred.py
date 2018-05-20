import pickle
import getpass

def getCreds():
	try:
		fp = open("cred.txt",'r')
		cred = pickle.load(fp)
		fp.close()
		return cred
	except IOError:
		# If not exists, create the file
		fp = open("cred.txt", 'w+')
		print "No cred.txt file found. Initiating setup"
		username = raw_input("Enter your gatorlink Username: ")
		password = getpass.getpass("Enter your gatorlink Password: ")
		gusername = raw_input("Enter your Gmail Username: ")
		gpass = getpass.getpass("Enter your Gmail Password: ")
		cCode = raw_input("Enter the exact course code you are looking for: ")
		sendEmail = raw_input("Enter the email you want to send to: ")

		cred = {
			"glusername": username,
			"glpassword":password,
			"gmailusername":gusername,
			"gmailPassword":gpass,
			"courseCode":cCode,
			"recipient":sendEmail
			}
		pickle.dump(cred,fp)
		fp.close()
		return None
