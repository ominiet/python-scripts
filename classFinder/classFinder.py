import cred
import CFscript
import emailer
import logger


if __name__ == '__main__':
    #get credentials or set up if first run
    mycred = cred.getCreds()
    #run the selenium script
    results = CFscript.searchSeats(mycred["glusername"], mycred["glpassword"], mycred["courseCode"])

    print results["id"]
    print results["seats"]

    switch
    #
    #stop running if registered
    #

    #create a log entry for success and failures
    # dbReturnValues = createLogEntry(results)
    #
    # #send appropriate email if success or chosen amount of failures has happened
    # doEmail(dbReturnValues, mycred["gmailusername"], mycred["gmailPassword"],mycred["recipient"])
