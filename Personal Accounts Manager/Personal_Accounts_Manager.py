import os
import random
from datetime import datetime

#A dictionary to contain all the info of the accounts
Accounts = {}

#A list to contain all the characters used for generating
#the random password (91 character)
Characters = ['Q','W','E','R','T','Y','U','I','O','P',
              'A','S','D','F','G','H','J','K','L','Z',
              'X','C','V','B','N','M','1','2','3','4',
              '5','6','7','8','9','~','!','@','#','$',
              '%','^','&','*','(',')','_','+','=','-',
              'q','w','e','r','t','y','u','i','o','p',
              '[',']','a','s','d','f','g','h','j','k',
              ';','\'','\\','z','x','c','v','b','n',
              'm',',','.','/','{','}',':','"','|','<',
              '>','?']

#Name of the input/output file
inputFileName = "testOutputFile.txt"

#Updated name of the input/output file
inputFileNameUpdated = "testOutputFileOLD.txt"

#A class for the Account object
class Account:

    def __init__(self, organisation, email, password):
        self.Organisation = organisation
        self.Email = email
        self.Password = password

#To print the dictionary of Accounts for debugging purposes
def printAccounts():
    for key in Accounts.keys():
        print("Organisaion: " + Accounts[key].Organisation)
        print("e-mail: ",Accounts[key].Email)
        print("password: ",Accounts[key].Password)
        print("\n")

#To view account info if the account is present in the Accounts dictionary
def viewAccount(Organisation):
    print("e-mail: ",Accounts[Organisation].Email)
    print("password: ",Accounts[Organisation].Password)

#To generate and return a string that represents a random password
def generatePassword():
    password = ""
    random.seed(datetime.now())
    randomFactor = 987561247.95312

    for i in range(0,10):
        random.seed(datetime.now())
        randomIndex = int(random.random()*randomFactor*(i+1))%91
        password += Characters[randomIndex]

    return password

#To manage the whole flow of the code
def accountsManager():

    Organisation = input("Enter the name of the organisation: ")

    if(Organisation in Accounts.keys()):
        viewAccount(Organisation)

    else:
        email = input("Enter email: ")
        password = generatePassword()
        account = Account(Organisation, email, password)
        Accounts[account.Organisation] = account

#To write the contents of the Accounts dictionary to an external file
def writeToOutputFile():
    inputFile = open(inputFileName,"w+")
    accountsData = ""
    for key in Accounts.keys():
        accountsData += "Organsation: "+ key + "\n"
        accountsData += "E-mail: " + Accounts[key].Email + "\n"
        accountsData += "Password: " + Accounts[key].Password + "\n"
        accountsData += "\n\n"
    inputFile.write(accountsData)
    inputFile.close()
    os.remove("./" + inputFileNameUpdated)

#To read info of User accounts from an external file and save it to
# Accounts dictionary
def readInputFile():

    if( not os.path.isfile("./" + inputFileName) ):
        print("No Previous Data Found")
        return

    inputFile = open(inputFileName,"r")
    accountsData = inputFile.readlines()
    inputFile.close()
    os.rename("./" + inputFileName, "./" + inputFileNameUpdated)

    for lineIndex in range(0,len(accountsData),5):

        organisation = accountsData[lineIndex].replace("Organsation: ","").replace("\n","")
        email = accountsData[lineIndex+1].replace("E-mail: ","").replace("\n","")
        password = accountsData[lineIndex+2].replace("Password: ","").replace("\n","")

        account = Account(organisation, email, password)
        Accounts[organisation] = account

#Start of Program
Input = input("Enter anything but 0\n")
readInputFile()

#printAccounts()

while (Input != "0"):
    accountsManager()
    Input = input("Enter anything but 0\n")

writeToOutputFile()