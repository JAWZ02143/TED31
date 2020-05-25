#20200225 MultichoiceWindow_V1.0.py
#jacob McClure

"""
*****Change Log*****
V1.0 - Setup
********************
"""

# import the library
from appJar import gui

position = [0,0]

# handle button events
def press(button): 
    if button == "Start" and position == [0,0]:
        question1()
    if button == "1" and position == [1,0]:
        choice3()
    if button == "2" and position == [0,0]:
        choice2()
    if button == "2" and position == [1,0]:
        choice4()        
    
def question1():
    app.setLabel("title", "Choice #2")
    app.setLabel("position", "[1,0]")
    app.hidebuttons(["Start", "How to Play"])
    app.addButtons(["1", "2", "3", "4"], press)
    app.setButtonWidth("1", 20)
    app.setButtonWidth("2", 20)
    app.setButtonWidth("3", 20)
    app.setButtonWidth("4", 20)    
    position = [1,0]
'''def choice2():
    app.setLabel("title", "Choice #2")
    app.setLabel("position", "[2,0]")
    app.addButton("3", press)
    app.setButtonWidth("3", 20)
    position [2,0]'''    
def choice2():      
    app.setLabel("title","Choice #3")
    app.setLabel("position","[1,1]")
    position [1,1]
def choice4():
    app.setLabel("title", "Choice #2")
    app.setLabel("position", "[1,2]")
    position = [1,2]    
    
# create a GUI variable called app
app = gui("Main Window", "600x400")
app.setBg("Blue")
app.setFont(18)

# add & configure widgets - widgets get a name, to help referencing them later
app.addLabel("title", "Welcome to Choice")
app.setLabelBg("title", "black")
app.setLabelFg("title", "lightgreen")
app.addLabel("position", "[0,0]")



# link the buttons to the function called press
app.addButtons(["Start", "How to Play"], press)
app.setButtonWidth("Start", 20)
app.setButtonWidth("How to Play", 20)

# start the GUI
app.go()

