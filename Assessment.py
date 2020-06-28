#20200225 quiz_V1.5.py
#jacob McClure

"""
*****Change Log*****
V1.0 - Setup
v1.5 - questions set up
********************
"""

# import the library
from appJar import gui

position = [0,0]

# handle button events
def press(button): 
    if button == "Start" and position == [0,0]:
        pickTrash()
        
    if button == "How to Play" and position == [0,0]:
        howtoPlay()
    
    if button == "Plastic" and position == [1,0]:
        plasticQuestionOne()        
        
#start of picking trash    
def pickTrash():
    app.removeAllWidgets()
    app.addLabel("title", "--Pick Trash For Questions About--")
    app.setLabelBg("title", "black")
    app.setLabelFg("title", "lightgreen")
    app.addLabel("position", "[1,0]")    
    app.addButtons(["Plastic", "Rubber", "Polystyrene", "(placeholder)"], press)
    app.setButtonWidth("Plastic", 40)
    app.setButtonWidth("Rubber", 40)
    app.setButtonWidth("Polystyrene", 40)
    app.setButtonWidth("(placeholder)", 40)
    position = [1,0]

def howtoPlay():
    app.removeAllWidgets()
    app.addLabel("title", "How To Play!")
    app.setLabelBg("title", "black")
    app.setLabelFg("title", "lightgreen")
    app.addLabel("position", "[1,1]")
    app.addButtons(["Start"], press)    
    position = [1,1]    
    
#Polystyrene Questions
def question1poly():
    app.removeAllWidgets()
    app.addLabel("title", "Choice #2")
    app.setLabelBg("title", "black")
    app.setLabelFg("title", "lightgreen")    
    app.addLabel("position", "[4,0]")
    app.addButtons(["1", "2", "3", "4"], press)
    app.setButtonWidth("1", 20)
    app.setButtonWidth("2", 20)
    app.setButtonWidth("3", 20)
    app.setButtonWidth("4", 20)    
    position = [4,0]    

#Rubber Questions
def question1rub():
    app.removeAllWidgets()
    app.addLabel("title", "Choice #2")
    app.setLabelBg("title", "black")
    app.setLabelFg("title", "lightgreen")    
    app.addLabel("position", "[3,0]")
    app.addButtons(["1", "2", "3", "4"], press)
    app.setButtonWidth("1", 20)
    app.setButtonWidth("2", 20)
    app.setButtonWidth("3", 20)
    app.setButtonWidth("4", 20)    
    position = [3,0]

#Plastic Questions
def plasticQuestionOne():
    app.removeAllWidgets()
    app.addLabel("title", "Plastic Question 1")
    app.setLabelBg("title", "black")
    app.setLabelFg("title", "lightgreen")    
    app.addLabel("position", "[2,0]")
    app.addLabel("question", "How much plastic is in the ocean?")
    app.addButtons(["100 Million Metric Tons", "500 Million Metric Tons", "200 Million Metric Tons", "150 Million Metric Tons"], press)
    app.setButtonWidth("100 Million Metric Tons", 90)
    app.setButtonWidth("500 Million Metric Tons", 90)
    app.setButtonWidth("200 Million Metric Tons", 90)
    app.setButtonWidth("150 Million Metric Tons", 90)    
    position = [2,0]

#Placeholder Questions


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

