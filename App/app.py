import sys, os
sys.path.append(os.path.abspath(os.path.join('..', 'utils')))

from tkinter import *
from datetime import datetime
from click import style
from PIL import ImageTk, Image
from data import Data
from pie import Pie

#
# Application loading
#

root = Tk()
root.title("CP")
root.geometry("525x800")
ico = Image.open('./static/logo.png')
photo = ImageTk.PhotoImage(ico)
root.wm_iconphoto(False, photo)

#
# Global variables
#

imageLoaded = False
covidInfo = Data.getData()

def onClick(inputChar):
    global imageLoaded
    global covidInfo
    global tableLabel
    global titleLabel
    global countryEntry
    global errorLabel

    if inputChar == "Enter":
        countryName = countryEntry.get()
    countryName = countryName.capitalize()
    
    try:
        tmp = covidInfo[countryName]
    except:
        errorLabel.configure(text = "Invalid Input", fg = "red")
        return
    
    titleLabel.configure(text = f"Covid statistics for {countryName}", font = ("Calibri", 16, "bold"), fg = "red")
    

    if imageLoaded == False:
        #
        # Constructing Tables
        #
        global totalCaseImg # Preventing Garbage Collection, for some reason
        totalCaseImg = ImageTk.PhotoImage(Image.open("./static/virus_icon.png"))

        tableLabel[3][1].configure(image = totalCaseImg)
        tableLabel[4][1].configure(text = "Total Cases", font = ("Calibri", 14, "bold"))

        global activeCaseImg 
        activeCaseImg = ImageTk.PhotoImage(Image.open("./static/warning_icon.png"))
        tableLabel[3][2].configure(image = activeCaseImg)
        tableLabel[4][2].configure(text = "Active", font = ("Calibri", 14, "bold"))

        global recoveredCaseImg 
        recoveredCaseImg = ImageTk.PhotoImage(Image.open("./static/healing_icon.png"))
        tableLabel[3][3].configure(image = recoveredCaseImg)
        tableLabel[4][3].configure(text = "Recovered", font = ("Calibri", 14, "bold"))

        global deathCaseImg 
        deathCaseImg = ImageTk.PhotoImage(Image.open("./static/skull_icon.png"))
        tableLabel[3][4].configure(image = deathCaseImg)
        tableLabel[4][4].configure(text = "Deaths", font = ("Calibri", 14, "bold"))

        tableLabel[5][0].configure(text = "Count", font = ("Calibri", 14, "bold"))
        tableLabel[6][0].configure(text = "Total/1M\npopulation", font = ("Calibri", 14, "bold"))

        imageLoaded = True

    #
    # Constructing Raw Data
    #
    
    totalCasesInt = int(covidInfo[countryName]['TotalCases'].replace(',', '').replace('N/A', '0'))
    activeCasesInt = int(covidInfo[countryName]['ActiveCases'].replace(',', '').replace('N/A', '0'))
    totalRecoveredInt = int(covidInfo[countryName]['TotalRecovered'].replace(',', '').replace('N/A', '0'))
    totalDeathsInt = int(covidInfo[countryName]['TotalDeaths'].replace(',', '').replace('N/A', '0'))
    popCount = int(covidInfo[countryName]['TotalCases'].replace(",", ""))//int(covidInfo[countryName]['TotCases/1M pop'].replace(",", ""))

    tableLabel[5][1].configure(text = f"{totalCasesInt:,}")
    tableLabel[5][2].configure(text = f"{activeCasesInt:,}")
    tableLabel[5][3].configure(text = f"{totalRecoveredInt:,}")
    tableLabel[5][4].configure(text = f"{totalDeathsInt:,}")

    tableLabel[6][1].configure(text = f"{covidInfo[countryName]['TotCases/1M pop']}")
    tableLabel[6][2].configure(text = f"{totalCasesInt//popCount:,}")
    tableLabel[6][3].configure(text = f"{totalRecoveredInt//popCount:,}")
    tableLabel[6][4].configure(text = f"{covidInfo[countryName]['Deaths/1M pop']}")


    #
    # Constructing Pie Chart Data
    #

    Pie(activeCasesInt, totalRecoveredInt, totalDeathsInt).pieChart()

    global pieChartImg 
    pieChartImg = ImageTk.PhotoImage(Image.open("./static/potato.png"))

    pieChartLabel = Label(root)
    pieChartLabel.grid(row = 7, column = 0, columnspan = 5)
    pieChartLabel.configure(image = pieChartImg)
        

def onEnter(event):         
    onClick("Enter")


#countryLabel = Label(root, text = "Country", width = 40, anchor = "w")

countryLabel = Label(root, text = "Country", width = 35, font = ("Calibri", 12, "bold"))
countryLabel.grid(row = 0, column = 0, columnspan = 3, padx = 10)

countryEntry = Entry(root, width = 46)
countryEntry.focus_set()
countryEntry.grid(row = 1, column = 0, columnspan = 3, pady = 5)

enterButton = Button(root, text = "Check!", command = lambda: onClick("Enter"))
enterButton.grid(row = 1, column = 3, pady = 5)

errorLabel = Label(root)
errorLabel.grid(row = 1, column = 4, pady = 5)

tableLabel = [[], [], []]
for i in range(3, 8):
    tableLabel.append([])
    for j in range(7):
        tableLabel[i].append(Label(root))
        tableLabel[i][j].grid(row = i, column = j)

titleLabel = Label(root)
titleLabel.grid(row = 2, column = 0, columnspan = 5)

"""
totalCaseLabel = Label(root)
totalCaseLabel.grid(row = 3, column = 1)
totalCaseTextLabel = Label(root)
totalCaseTextLabel.grid(row = 4, column = 1)
totalCaseCountLabel = Label(root)
totalCaseCountLabel.grid(row)

activeCaseLabel = Label(root)
activeCaseLabel.grid(row = 3, column = 2)
activeCaseTextLabel = Label(root)
activeCaseTextLabel.grid(row = 4, column = 2)

recoveredCaseLabel = Label(root)
recoveredCaseLabel.grid(row = 3, column = 3)
recoveredCaseTextLabel = Label(root)
recoveredCaseTextLabel.grid(row = 4, column = 3)

deathCaseLabel = Label(root)
deathCaseLabel.grid(row = 3, column = 4)
deathCaseTextLabel = Label(root)
deathCaseTextLabel.grid(row = 4, column = 4)

countLabel = Label(root)
countLabel.grid(row = 5, column = 0)

ratioLabel = Label(root)
ratioLabel.grid(row = 6, column = 0)


countryStringMenu = StringVar()
countryStringMenu.set("Select A Country")

countryOptionMenu = OptionMenu(root, countryStringMenu, *sorted([i.string for i in country]))
countryOptionMenu.grid(row = 1, column = 0, pady = 5)

resultLabel = Label(root)
resultLabel.grid(row = 0, column = 4, columnspan = 2)

dateLabel = Label(root, text = "Date (DD/MM/YYYY)", width = 20, anchor = "w")
dateLabel.grid(row = 0, column = 1, padx = 10)

dateEntry = Entry(root, text = datetime.now(), width = 23)
dateEntry.grid(row = 1, column = 1, pady = 5)
dateEntry.insert(0, datetime.now().strftime("%d/%m/%Y"))
"""

root.bind('<Return>', onEnter)
root.mainloop()
