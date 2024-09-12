# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define Osiris = Character ('Osiris', color="#aaeeff")
label start:
    "During a video tutorial"
    "Osiris" "Hi my name is Osi I love women."
    "Osiris" "This is a test \"dating sim\" where you get to date me :3"

    label sprites:
    "Osiris" "Anyway here is my sexy bodad self "
    show osiris neutral 
    "Osiris" "It's nice to finally see you face to face."
    show osiris neutral at right 
    "Osiris" "This renpy stuff isn't as hard as I thought it would be"
    show osiris happy at left 
    "Osiris" "I really.. really missed you "
    Osiris "Hehe.. my name is teal now"

    label background:
        Osiris " Anyway, ready for our date? "
        scene bg tacobell
        with fade 
        show osiris happy 
        Osiris "I heard you humans liked this place"


label choices: 
    default learned = False
    Osiris " Do you like Taco Bell? "
menu: 
    "Yes":
        jump choices1_a

    " EW TACO BELL IS ASS":
        jump choices1_b
    

label choices1_a:
    $ learned = True 
    Osiris "I'm really glad you think so."
    jump choices1_common


label choices1_b:
    show osiris neutral 
    Osiris "Oh. I'm sorry"
    jump choices1_common

    
label choices1_common:
    Osiris " It's getting pretty chilly. "
    Osiris " Let's head inside."

label flags: 
    if learned: 
        scene bg itacobell 
        with fade
        show osiris happy
        Osiris "Hehe.. I remember you being this sweet."
        Osiris " We should really hang out more. I know I said I missed you already but.."
    else:
        scene bg itacobell
        with fade
        show osiris neutral 
        Osiris " I'm sorry for bringing you here."
        Osiris " I guess I remembered wrong. "