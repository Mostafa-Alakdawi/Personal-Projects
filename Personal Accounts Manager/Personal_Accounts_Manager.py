import random
from datetime import datetime

Accounts = {}
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

class Account:

    def __init__(self, organisation, email, password):
        self.Organisation = organisation
        self.Email = email
        self.Password = password

#To view account info if possible
def viewAccount(Organisation):
    print(Accounts[Organisation].Email)
    print(Accounts[Organisation].Password)

#To view account info if possible
def viewAccount(Organisation):
    print("e-mail: ",Accounts[Organisation].Email)
    print("password: ",Accounts[Organisation].Password)

#To generate a random password
def generatePassword():
    password = ""
    random.seed(datetime.now())
    randomFactor = 987561247.95312

    for i in range(0,10):
        random.seed(datetime.now())
        randomIndex = int(random.random()*randomFactor*(i+1))%91
        password += Characters[randomIndex]

    return password

#to manage the whole flow of the code
def accountsManager():

    Organisation = input("Enter the name of the organisation: ")

    if(Organisation in Accounts.keys()):
        viewAccount(Organisation)

    else:
        email = input("Enter email: ")
        #password = input("Enter pass: ")
        password = generatePassword()
        account = Account(Organisation, email, password)
        Accounts[account.Organisation] = account

#Start of Program
Input = input("Enter anything but 0\n")

while (Input != "0"):
    accountsManager()
    #print(len(Characters))
    Input = input("Enter anything but 0\n")



