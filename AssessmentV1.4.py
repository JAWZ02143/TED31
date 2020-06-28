#20200225 quiz_V1.5.py
#jacob McClure

"""
*****Change Log*****
V1.0 - Setup
v1.1 - questions set up
v1.2 - most questions added
v1.3-4 - all questions added
********************
"""

# import the library
from appJar import gui

questionNumber = 0

#questions stored here
plasticQuestions = []
rubberQuestions = []
polyQuestions = []

plasticRoute = False
rubberRoute = False
polyRoute = False

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
        app.addButtons(self.options, self.checkAnswer)
    
    def checkAnswer(self, button):
        for button in self.options:
            app.hideButton(button)
        if button == self.answer:
            app.setLabel("title","CORRECT")
        else:
            app.setLabel("title","WRONG")
        app.addButton("Next", press)
        
    
######## QUESTIONS ##################

#######Plastic Questions#############
plasticQuestions.append(Question("Plastic","How much plastic is in the ocean?",["100 Million Metric Tons","150 Million Metric Tons", "200 Million Metric Tons", "500 Million Metric Tons"],"150 Million Metric Tons"))
plasticQuestions.append(Question("Plastic","How Many Turtles Die of Plastic Each Year?",["1000","2000", "3000", "4000"],"1000"))
plasticQuestions.append(Question("Plastic","How Long Does Plastic Take to Decompose?",["50 years","500 years", "1000 years", "2000 years"],"1000 years"))
plasticQuestions.append(Question("Plastic","Which Plastic can be Recycled?",["1,2","3,4", "5", "6,7"],"1,2"))
plasticQuestions.append(Question("Plastic","Should we get rid of anything Plastic",["Yes", "Yes But Not Everything" ,"No","I Don't Care"],"Yes But Not Everything"))
#####################################

#######Rubber Questions##############
rubberQuestions.append(Question("Rubber","What is in Rubber Tyres that affect the enviroment?",["Benzene", "Mercury", "Arsenic", "All Of The Above"],"All Of The Above"))
rubberQuestions.append(Question("Rubber","Can Rubber Affect the Air",["Yes","No"],"Yes"))
rubberQuestions.append(Question("Rubber","Can Rubber Affect the Water?",["Yes","No"],"Yes"))
rubberQuestions.append(Question("Rubber","Can Rubber Affect the Ground?",["Yes","No"],"Yes"))
rubberQuestions.append(Question("Rubber","Are tire fires dangerous to the surrounding Enviroment",["Yes","No"],"Yes"))
#####################################

#######Polystyrene Questions#########
polyQuestions.append(Question("Polystyrene","Can you Recycle Polystyrene?",["     Yes    ","No, But On Occasions","     No     ",],"No, But On Occasions"))
polyQuestions.append(Question("Polystyrene","How long Does it Take to Decompose?",["50 Years","250 Years","500 Years","1000 Years"],"500 Years"))
polyQuestions.append(Question("Polystyrene","Is it Safe for the Oceans?",["Yes","No"],"No"))
polyQuestions.append(Question("Polystyrene","How toxic is it to us?",["Highly","Kinda","Not Really","No"],"Highly"))
polyQuestions.append(Question("Polystyrene","Does it affect the air pollution?",["Yes","No"],"Yes"))
#####################################

#####################################

# handle button events
def press(button): 
    global questionNumber, plasticRoute, rubberRoute, polyRoute
    
    if button == "Start":
        pickTrash()
        
    if button == "How to Play":
        howtoPlay()
    
    if button == "Plastic":
        plasticRoute = True
        plasticQuestions[questionNumber].displayQuestion()
        
    if button == "Rubber":
        rubberRoute = True
        rubberQuestions[questionNumber].displayQuestion()   

    if button == "Polystyrene":
        polyRoute = True
        polyQuestions[questionNumber].displayQuestion()      
            
    if button == "Next":
        questionNumber += 1
        if plasticRoute == True:
            if questionNumber < len(plasticQuestions)-1:
                plasticQuestions[questionNumber].displayQuestion()
            else:
                endScreen()
            
        elif rubberRoute == True:
            rubberQuestions[questionNumber].displayQuestion()
        elif polyRoute == True:
            polyQuestions[questionNumber].displayQuestion()
        
        
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

def howtoPlay():
    app.removeAllWidgets()
    app.addLabel("title", "How To Play!")
    app.setLabelBg("title", "black")
    app.setLabelFg("title", "lightgreen")
    app.addLabel("rules", '''
    Choose your rubbish of choice and complete the 5 questions
    When completed you will get a score out of 5
    Get at least more than 3 to go to the next stage
    Lose and redo the questions
    Start the next quiz on another rubbish
    Once answered 15 questions correctly
    You will have WON
    Otherwise you LOSE 
    ''')
    app.setLabelFg("rules", "yellow")
    app.setLabelBg("rules", "black")
    app.addButtons(["Start"], press)      

def endScreen():
    app.removeAllWidgets()
    app.addLabel("end")

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

