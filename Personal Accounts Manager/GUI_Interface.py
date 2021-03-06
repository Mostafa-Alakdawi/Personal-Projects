from tkinter import *
from Personal_Accounts_Manager import *

# Creating the GUI elements
master = Tk()

# Creating the GUI text fields
organisationText = Text(master, height=1, width=30)
emailText = Text(master, height=1, width=30)
passwordText = Text(master, height=1, width=30)

#To view account info in the specified text fieds
def viewAccountInfoText(accountInfo):
    eraseText()
    organisationText.insert(INSERT, accountInfo[0])
    emailText.insert(INSERT, accountInfo[1])
    passwordText.insert(INSERT, accountInfo[2])

#call mainFunction() passing the value of organisation from
#Personal_Accounts_Manager to get/generate account info
def accountManagerStart():
    emailText.delete('1.0', END)
    passwordText.delete('1.0', END)
    organisation = organisationText.get("1.0",'end-1c')
    viewAccountInfoText(mainFunction(organisation))

#To erase account info from the specified text fieds
def eraseText():
    organisationText.delete('1.0', END)
    emailText.delete('1.0', END)
    passwordText.delete('1.0', END)

#To save all the accounts info to a specific text field by calling
#writeToOutputFile() from Personal_Accounts_Manager.py file
def saveData():
    #Writing the info of the Accounts dictionary to an external text file
    #to save this info for future use
    writeToOutputFile()

#To initialize of the GUI elements
def GUI_Init():

    #Setting the size of the window
    master.geometry("1000x400")

    # Creating the GUI labels
    Label(master, width = 15, text='Organisation: ', font=("Times New Roman", 20, "bold")).grid(row=0)
    Label(master, width = 15, text='E-mail: ', font=("Times New Roman", 20, "bold")).grid(row=1)
    Label(master, width = 15, text='Password: ', font=("Times New Roman", 20, "bold")).grid(row=2)
    Label(master, width = 20, text='Password Options', font=("Times New Roman", 20, "bold")).grid(row=0, column=2)

    # Configuring the font for the GUI text fields
    organisationText.configure(font=("Times New Roman", 15))
    emailText.configure(font=("Times New Roman", 15))
    passwordText.configure(font=("Times New Roman", 15))

    # locating the GUI text fields
    organisationText.grid(row=0, column=1, padx=10, pady=10)
    emailText.grid(row=1, column=1, padx=10, pady=10)
    passwordText.grid(row=2, column=1, padx=10, pady=10)

    # Creating the GUI buttons
    generateButton = Button(master, text ="Generate", width = 10, font = ("Times New Roman", 20, "bold"),
                            command = accountManagerStart)
    eraseButton = Button(master, text ="Erase", width = 10, font = ("Times New Roman", 20, "bold"),
                         command = eraseText)
    saveButton = Button(master, text ="Save", width = 10, font = ("Times New Roman", 20, "bold"),
                         command = saveData)

    # locating the GUI buttons
    generateButton.grid(row=5, column=0, padx=10, pady=10)
    eraseButton.grid(row=6, column=0, padx=10, pady=10)
    saveButton.grid(row=7, column=0, padx=10, pady=10)

#To start the execution of the GUI_Interface module
def GUI_Start():

    #Read the already existing info of the accounts
    #from the input text file
    readInputFile()

    #Initialization of the GUI elements
    GUI_Init()

    #Starting the loop of the GUI
    mainloop()

    #Writing the info of the Accounts dictionary to an external text file
    #to save this info for future use
    writeToOutputFile()

#Starting the execution of the GUI
GUI_Start()
