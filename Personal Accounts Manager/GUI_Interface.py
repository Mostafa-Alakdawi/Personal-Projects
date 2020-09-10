from tkinter import *
from Personal_Accounts_Manager import *

#To view account info in the specified text fieds
def viewAccountInfoText(accountInfo):
    organisationText.insert(INSERT, accountInfo[0])
    emailText.insert(INSERT, accountInfo[1])
    passwordText.insert(INSERT, accountInfo[2])

#call mainFunction() from Personal_Accounts_Manager to get/generate
#account info
def accountManagerStart():
    viewAccountInfoText(mainFunction())

#To erase account info from the specified text fieds
def eraseText():
    organisationText.delete('1.0', END)
    emailText.delete('1.0', END)
    passwordText.delete('1.0', END)


def GUI_Init():

    #Setting the size of the window
    master.geometry("1000x400")

    # Creating the GUI labels
    Label(master, width = 20, text='Organisation: ', font=("Times New Roman", 20, "bold")).grid(row=0)
    Label(master, width = 20, text='E-mail: ', font=("Times New Roman", 20, "bold")).grid(row=1)
    Label(master, width = 20, text='Password: ', font=("Times New Roman", 20, "bold")).grid(row=2)
    Label(master, width = 20, text='Password Options', font=("Times New Roman", 20, "bold")).grid(row=0, column=2)

    # Configuring the font for the GUI text fields
    organisationText.configure(font=("Times New Roman", 20))
    emailText.configure(font=("Times New Roman", 20))
    passwordText.configure(font=("Times New Roman", 20))

    # locating the GUI text fields
    organisationText.grid(row=0, column=1, padx=10, pady=10)
    emailText.grid(row=1, column=1, padx=10, pady=10)
    passwordText.grid(row=2, column=1, padx=10, pady=10)

    # Creating the GUI buttons
    generateButton = Button(master, text ="Generate", width = 10, font = ("Times New Roman", 20, "bold"),
                            command = accountManagerStart)
    eraseButton = Button(master, text ="Erase", width = 10, font = ("Times New Roman", 20, "bold"),
                         command = eraseText)

    # locating the GUI buttons
    generateButton.grid(row=5, column=0, padx=10, pady=10)
    eraseButton.grid(row=6, column=0, padx=10, pady=10)

def GUI_Start():
    #Initialization of the GUI elements
    GUI_Init()

    #Starting the loop of the GUI
    mainloop()

    #Writing the info of the Accounts dictionary to an external text file
    #to save this info for future use
    writeToOutputFile()

# Creating the GUI elements
master = Tk()

# Creating the GUI text fields
organisationText = Text(master, height=1, width=15)
emailText = Text(master, height=1, width=15)
passwordText = Text(master, height=1, width=15)

#Starting the execution of the GUI
GUI_Start()
