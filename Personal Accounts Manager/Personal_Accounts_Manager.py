import os
import random
from datetime import datetime

#A dictionary to contain all the info of the accounts
Accounts = {}

#A list to contain all the characters used for generating
#the random password (91 character)
charactersSet1 = ['Q','W','E','R','T','Y','U','I','O','P',
                  'A','S','D','F','G','H','J','K','L','Z',
                  'X','C','V','B','N','M','1','2','3','4',
                  '5','6','7','8','9','~','!','@','#','$',
                  '%','^','&','*','(',')','_','+','=','-',
                  'q','w','e','r','t','y','u','i','o','p',
                  '[',']','a','s','d','f','g','h','j','k',
                  ';','\'','\\','z','x','c','v','b','n',
                  'm',',','.','/','{','}',':','"','|','<',
                  '>','?']

numberOfCharactersInSet1 = 91

#A list to contain a set of characters used for generating
#the random password (83 character)
charactersSet2 =    ['Q','W','E','R','T','Y','U','I','O','P',
                    'A','S','D','F','G','H','J','K','L','Z',
                    'X','C','V','B','N','M','1','2','3','4',
                    '5','6','7','8','9','~','!','@','#','$',
                    '%','^','&','*','(',')','_','+','=','-',
                    'q','w','e','r','t','y','u','i','o','p',
                    '[',']','a','s','d','f','g','h','j','k',
                    'z','x','c','v','b','n','m','{','}','|',
                    '<','>','?']

numberOfCharactersInSet2 = 83

#Name of the input/output file
inputFileName = "testOutputFile.txt"

#Updated name of the input/output file
inputFileNameUpdated = "testOutputFileOLD.txt"

#The default e-mail
defaultEmail = "default.email@mail.com"

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
    numberOfCharactersInSet = numberOfCharactersInSet2

    for i in range(0,10):
        random.seed(datetime.now())
        randomIndex = int(random.random()*randomFactor*(i+1))%numberOfCharactersInSet
        password += charactersSet2[randomIndex]

    return password

#To manage the whole flow of the code
def accountsManager(organisation):

    #Organisation = input("Enter the name of the organisation: ")
    Organisation = organisation

    if not (Organisation in Accounts.keys()):
        #For debugging purposes
        #viewAccount(Organisation)

        email = defaultEmail
        password = generatePassword()
        account = Account(Organisation, email, password)
        Accounts[account.Organisation] = account

    return (Organisation, Accounts[Organisation].Email, Accounts[Organisation].Password)

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
    #os.remove("./" + inputFileNameUpdated)

#To read info of User accounts from an external file and save it to
# Accounts dictionary
def readInputFile():

    if( not os.path.isfile("./" + inputFileName) ):
        print("No Previous Data Found")
        return

    inputFile = open(inputFileName,"r")
    accountsData = inputFile.readlines()
    inputFile.close()
    #os.rename("./" + inputFileName, "./" + inputFileNameUpdated)

    for lineIndex in range(0,len(accountsData),5):

        organisation = accountsData[lineIndex].replace("Organsation: ","").replace("\n","")
        email = accountsData[lineIndex+1].replace("E-mail: ","").replace("\n","")
        password = accountsData[lineIndex+2].replace("Password: ","").replace("\n","")

        account = Account(organisation, email, password)
        Accounts[organisation] = account


#Start of Program
def mainFunction(organisation):

    #Receive input from User
    #Input = input("Enter anything but 0\n")

    #Read the already existing info of the accounts
    #from the input text file
    #readInputFile()

    #Print the read data for debugging purposes
    #printAccounts()

    #The main loop of the program
    #Will continue to ask for User's input till the User enters 0
    #while (Input != "0"):

    return accountsManager(organisation)

        # Receive input from User
        #Input = input("Enter anything but 0\n")
