from pymongo import MongoClient
import datetime
import emailer


def createLogEntry(results):
    client = MongoClient("mongodb://classfinder:cfinder@ds135552.mlab.com:35552/classfinder")
    db = client.classfinder
    log = db.log
    logEntry = {
        "returnCode": results["id"],
        "seats": results["seats"],
        "runTime": datetime.datetime.now()
    }
    log.insert_one(logEntry)
    client.close()

def getNumberOfEntries():
    client = MongoClient("mongodb://classfinder:cfinder@ds135552.mlab.com:35552/classfinder")
    db = client.classfinder
    log = db.log

    count = log.find({}).count()

    client.close()
    return count

def clearLog():
    client = MongoClient("mongodb://classfinder:cfinder@ds135552.mlab.com:35552/classfinder")
    db = client.classfinder
    log = db.log

    log.delete_many({})

    client.close()

def getAll():
    client = MongoClient("mongodb://classfinder:cfinder@ds135552.mlab.com:35552/classfinder")
    db = client.classfinder
    log = db.log

    entries = log.find({})

    client.close()

    return entries
def getAllAsString():
    entries = getAll()
    str = ""
    for entry in entries:
        print entry
