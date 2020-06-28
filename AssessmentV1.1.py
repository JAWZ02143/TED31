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
questionNumber = 0

#questions stored here
plasticQuestions = []
rubberQuestions = []
polyQuestions = []
placeQuestions = []

plasticRoute = False
rubberRoute = False
polyRoute = False
placeRoute = False

class Question:
    def __init__(self, category, questionText, options, answer):
        self.category = category
        self.questionText = questionText
        self.options = options
        self.answer = answer
    
    def displayQuestion(self):
        app.removeAllWidgets()
        app.addLabel("title", self.questionText)
        app.setLabelBg("title", "black")
        app.setLabelFg("title", "lightgreen")
        app.addLabel("position", "[1,0]")    
        app.addButtons(self.options, self.checkAnswer)
    
    def checkAnswer(self, button):
        if button == self.answer:
            app.setLabel("title","CORRECT")
        else:
            app.setLabel("title","WRONG")
        app.addButton("Next", press)
        
    
######## QUESTIONS ##############
plasticQuestions.append(Question("Plastic","How much plastic is in the ocean?",["100 Million Metric Tons","150 Million Metric Tons", "200 Million Metric Tons", "500 Million Metric Tons"],"150 Million Metric Tons"))
plasticQuestions.append(Question("Plastic","Do you like plastic? #2",["Yes","No"],"Yes"))

rubberQuestions.append(Question("Plastic","Do you like rubber?",["Yes","No"],"Yes"))
#################################


# handle button events
def press(button): 
    global questionNumber, plasticRoute, rubberRoute
    
    if button == "Start":
        pickTrash()
        
    if button == "How to Play":
        howtoPlay()
    
    if button == "Plastic":
        print("Plastic pressed")
        plasticRoute = True
        plasticQuestions[questionNumber].displayQuestion()
        
    if button == "Rubber":
        rubberRoute = True
        rubberQuestions[questionNumber].displayQuestion()   

    if button == "Polystyrene":
        polyRoute = True
        polyQuestions[questionNumber].displayQuestion()   

    if button == "placeholder":
        placeRoute = True
        placeQuestions[questionNumber].displayQuestion()   
            
    if button == "Next":
        questionNumber += 1
        if plasticRoute == True:
            plasticQuestions[questionNumber].displayQuestion()
        elif rubberRoute == True:
            rubberQuestions[questionNumber].displayQuestion()
        elif polyRoute == True:
            polyQuestions[questionNumber].displayQuestion()
        elif placeRoute == True:
            placeQuestions[questionNumber].displayQuestion()
        
        
#start of picking trash    
def pickTrash():
    app.removeAllWidgets()
    app.addLabel("title", "--Pick Trash For Questions About--")
    app.setLabelBg("title", "black")
    app.setLabelFg("title", "lightgreen")   
    app.addButtons(["Plastic", "Rubber", "Polystyrene", "(placeholder)"], press)
    app.setButtonWidth("Plastic", 40)
    app.setButtonWidth("Rubber", 40)
    app.setButtonWidth("Polystyrene", 40)
    app.setButtonWidth("(placeholder)", 40)

def howtoPlay():
    app.removeAllWidgets()
    app.addLabel("title", "How To Play!")
    app.setLabelBg("title", "black")
    app.setLabelFg("title", "lightgreen")
    app.addButtons(["Start"], press)      



# create a GUI variable called app
app = gui("Main Window", "1050x400")
app.setBg("Blue")
app.setFont(18)

# add & configure widgets - widgets get a name, to help referencing them later
app.addLabel("title", "Welcome to a quiz about Trash")
app.setLabelBg("title", "black")
app.setLabelFg("title", "lightgreen")



# link the buttons to the function called press
app.addButtons(["Start", "How to Play"], press)
app.setButtonWidth("Start", 20)
app.setButtonWidth("How to Play", 20)

# start the GUI
app.go()

