# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define Osiris = Character ('Osiris', color="#aaeeff")
default osiris_affection = 0
default vikiName = False




label start:
    "This is a really shitty test ok.."
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
        $ osiris_affection += 1
        jump choices1_a

    " EW TACO BELL IS ASS":
        $ osiris_affection += -1
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
        show osiris overjoyed
        Osiris "Hehe.. I remember you being this sweet."
        Osiris " We should really hang out more. I know I said I missed you already but.."
    else:
        scene bg itacobell
        with fade
        show osiris neutral 
        Osiris " I'm sorry for bringing you here."
        Osiris " I guess I remembered wrong. "
    

    label conversation1: 
    show osiris happy
    Osiris "Let's get to know eachother better."
    Osiris " But before we start, let's get some music in here. "
    play music "audio/bgm_gymno.mp3" fadein 1.0 volume 0.5
    

    label choices2:
    Osiris "I'll ask a question first"
    Osiris "Do you like birds?"

    menu:
        "I love birds.":
            show osiris overjoyed
            $ osiris_affection +=2
            "She seemed to be really excited by this."
            Osiris "I do too!!!"
            jump choices2_common

        " I like birds.":
            show osiris happy
            $ osiris_affection +=1
            "She perked up at your response, seemingly happier."
            Osiris "They're neat, aren't they."
            jump choices2_common

        "I don't care really care for them.":
            show osiris neutral
            "She seemed a little dissapointed with your answer."
            Osiris "To each their own, I suppose."
            jump choices2_common



    label choices2_common:
    show osiris neutral
    Osiris "Anyway I think I should ask the next question."

    label choices3:
    Osiris "Hmm.. I should ask something more personal."
    Osiris "Are you ready?"
    Osiris "Who am I kidding.. of course you are!"
    Osiris "Do you like pancakes or waffles?"

    menu:
        "PANCAKES 4 LYFFEEE":
            $ osiris_affection +=2
            show osiris overjoyed
            "She found your reaction cute."
            Osiris "You're awfully enthusiastic about this!"
            jump choices3_common

        "I'm more of a waffle fan.":
            show osiris happy
            $ osiris_affection +=1
            "She nodded in agreement."
            Osiris "Yeah, waffles are pretty good."
            jump choices3_common

        "I don't care for either.":
            show osiris neutral
            "She stared at you, seemingly bored."
            Osiris "I guess."
            jump choices3_common

    label choices3_common:
        show osiris neutral
    Osiris "Okay!! Time for the last questtionnn.."

    label choices4:
    Osiris "This is my final and MOST important question."
    Osiris "Do you fw Baja Blast?"
        
    menu: 
        "Ew no that shit is poison!!":
            show osiris angry
            $ osiris_affection += -3
            Osiris "...."

        "It's good.":
            show osiris happy
            $ osiris_affection += 1
            "She seemed to agree with you."
            Osiris "Yeah, it's pretty great."

        "I FUCKING LOVE BAJA BLAST!!!!!!!":
            show osiris happy
            $ osiris_affection += 2
            "She beamed at your reaction."
            Osiris "BAJA BLAST IS THE FUCKIN BEST!"

    label choices5:
    Osiris " I know i said it was the last one but humor me."
    Osiris "Is your name viki??"
    

    menu:
        "Yea":
            $ vikiName = True
        
        "Nah":
            Osiris "My mistake!"
        


    label ending_evaluation:
        if osiris_affection >= 5 and vikiName == True:
            jump osiris_marriage_ending

        elif osiris_affection >= 5:
            jump osiris_best_ending
        
        elif osiris_affection >=4:
            jump osiris_neutral_ending

        elif osiris_affection <=0:
            jump osiris_bad_ending

    label osiris_marriage_ending:
        show osiris lovestruck
        Osiris "PLS MARRY ME VIKI!!!"
        Osiris " I LOVE YOU SOO MUCCHHHh!!!!!!!!!!!"
        jump the_end

    label osiris_best_ending:
        Osiris "Tonight was really great"
        Osiris "I know this is sudden but.."
        show osiris lovestruck
        Osiris "I THINK I LOVE U!"
        jump the_end

    label osiris_neutral_ending:
        show osiris happy
        Osiris "This was fun."
        Osiris "Let's do this again?"
        jump the_end

    label osiris_bad_ending:
        show osiris angry
        Osiris "God you're so fucking boring."
        Osiris "Don't ever talk to me again."
        jump the_end

    label the_end:
        hide osiris
        hide bg  
        " THE END!! "
        
    


