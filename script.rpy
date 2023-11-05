# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.
# $ uncle = Character('uncle', color="#E03B8B")
default Uncle = Character('Uncle', color="#ff0000")       
# The game starts here.
label start:

    "Man" "Hello Beta!"
    scene bg
    show uncle

    Uncle "I am your father's friend."
    Uncle "He asked me to take you to him."
    menu kya_krna:
        "What will you do?"
        "Go with him.":
            jump game_over
            

        "Don't go and call for help!":
            jump good_job
            
label game_over:
    scene game_over
    "Sorry better luck next time."
    show black with dissolve
    jump explaination 

label good_job:
    scene good_job
    "You have done a great job."
    show black with dissolve
    jump explaination

label explaination:
    "Here's what to do"
    scene explaination
    "Do Not Engage: The child should avoid engaging in conversation or any form of interaction with the stranger."  
    "The child should not provide personal information, accept gifts, or go anywhere with the stranger."
    "Call for Help: The child should be encouraged to shout or call for help if they feel threatened or uncomfortable." 
    "Drawing attention to the situation is a critical step in deterring the stranger."
    "Remember Details: If the child can do so without endangering themselves, they should try to remember specific details about the stranger,"
    "such as their appearance, clothing, any distinctive features, and any identifiers, like a vehicle's license plate number."
    "Report to Authorities: It's important to report the incident to the local law enforcement authorities."
    "The child, along with a trusted adult, should provide the details of the incident and any information about the stranger."
    
    scene the_law
    "The POCSO Act, in particular, provides legal protection and remedies for children who have experienced sexual offenses."
    "Any attempt to sexually exploit or harm a child is a serious offense under this law, and it is important to involve the authorities to ensure that the child is protected and that the offender faces legal consequences."
    return
























