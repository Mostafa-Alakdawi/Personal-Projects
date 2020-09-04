class Account:

    def __init__(self, organisation, email, password):
        self.Organisation = organisation
        self.Email = email
        self.Password = password

#Start of Program

Accounts = {}

Organisation = input("Enter the name of the organisation: ")
email = input("Enter email: ")
password = input("Enter password: ")

account = Account(Organisation, email, password)

Accounts[account.Organisation] = account
