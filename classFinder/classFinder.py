import cred
import CFscript
import emailer
import logger

if __name__ == '__main__':
    #get credentials or set up if first run
    mycred = cred.getCreds()
    #run the selenium script
    results = CFscript.searchSeats(mycred["glusername"], mycred["glpassword"], mycred["courseCode"], mycred["registered"])


    logger.createLogEntry(results)

    if results["id"] == 1 or results["id"] == 3:
        #send email immediately and clear log to restart
        entries = logger.getAll()
        if results["id"] == 1:
            emailer.doSuccessEmail(entries, mycred["gmailusername"], mycred["gmailPassword"], mycred["recipient"])
            logger.clearLog()
        else:
            emailer.doFailureEmail(entries, mycred["gmailusername"], mycred["gmailPassword"], mycred["recipient"])
            logger.clearLog()

    else:
        logSize = logger.getNumberOfEntries()
        if logSize >= 24:
            entries = logger.getAll()
            emailer.doBasicEmail(entries, mycred["gmailusername"], mycred["gmailPassword"], mycred["recipient"])
            logger.clearLog()
