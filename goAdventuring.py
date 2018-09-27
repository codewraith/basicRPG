# -*- coding: utf-8 -*-
"""
Created on Mon Sep 24 15:45:33 2018

@author: ISInc
"""
from flask import Flask
import DungeonDie
import Encounter
import Character
import random
import os



def fightTurn(attacker,defender):

    if d20.roll() + attacker.atkBonus >= defender.toHit:
        atkDie = DungeonDie.Die(attacker.damageDieType)
        dmg = 0
        for i in range(1, attacker.damageDieNumber + 1):
            dmg = dmg + atkDie.roll()
            i = i + i - i #stupid statement to stop it complaining that i isn't used
        
        dmg = dmg + attacker.damageBonus
        defender.hp = defender.hp - dmg
        attacker.atkSuccess = True
        attacker.atkDamage = dmg

        msgChunks = {"hit":True,
                     "dmg":dmg}
    else:
        msgChunks = {"hit":False}
    return(msgChunks)







        
""" TO DO:
Change function to accept a dictionary of objects in the form "enemy": enemy, 
"pc": pc etc., and to parse 
tags in the format <object.property> to access the property from the 
specified object and subsitute the resulting value for the tag. property
must be a string   """      
def displayText(msg, obj):  
    import re
    matchCount = 0
    formatMsg = msg

    # matches a <tag> or <tag.tag> in a string
    matchTags = re.compile(r'''
    <       # opening bracket of the tag
    \S+     # one or more non-whitespace characters, immediately...
    >       # ... followed by the closing bracket of the tag
    ''', re.VERBOSE) # returns the entire match, including brackets

    # matches <tag~tag> but only retrieves the contents, without brackets
    matchTagContents = re.compile(r'''
    <       # same as the above except for the ()
    (\S+)   # return the letter groupings before and after a tilde delimiter
    ~
    (\S+)   # so this will return a tuple of ('key','value') from each tag <key~value>
    >       
    ''', re.VERBOSE)

    # find all instances that match the above regular expressions
    moTag = matchTags.findall(msg)
    moContents = matchTagContents.findall(msg)
    # print(repr(moTag))
    # print(repr(moContents))
    if moTag and moContents:
        for index, match in enumerate(moTag):
            matchCount = matchCount + 1
            # compile the search expression matching a specific tag
            subPattern = re.compile(match)
            # print("subPattern: ", repr(subPattern), "count: ", repr(matchCount))
            which = moContents[index][0]
            key = moContents[index][1]
            getFrom = obj[which]
            if isinstance(getFrom[key],str):
                value = getFrom[key]
            else:
                value = str(getFrom[key])
            # print("getFrom[", repr(key), "] = ", repr(getFrom[key]))
            # print("which", repr(which), ", key = ", repr(key))
            # replace <match> in formatMsg with stats["key"] ... the key to pass
                    # to the stats dictionary is retrieved from moContents[index]
            formatMsg = subPattern.sub(value, formatMsg)
  
    print(formatMsg)


def formatText(msg, obj, objType = "derive"):  
    import re
    stats = vars(obj)
   # matches a <tag> in a string
    matchTags = re.compile(r'''
    <       # opening bracket of the tag
    \S+     # one or more non-whitespace characters, immediately...
    >       # ... followed by the closing bracket of the tag
    ''', re.VERBOSE) # returns the entire match, including brackets

    # matches a <tag> but only retrieves the contents of the tag, no brackets
    matchTagContents = re.compile(r'''
    <       # same as the above except for the ()
    (\S+)   # () indicates this is the part of the match string we want to grab
    >       # so the brackets don't get returned
    ''', re.VERBOSE)

    # find all instances that match the above regular expressions
    moTag = matchTags.findall(msg)
    moContents = matchTagContents.findall(msg)

    formatMsg = msg

    if moTag and moContents:
        for index, match in enumerate(moTag):
            # compile the search expression matching a specific tag from the match object
            subPattern = re.compile(match)

            # replace <match> in formatMsg with stats["key"] ... the key to pass
                    # to the stats dictionary is retrieved from moContents[index]
            formatMsg = subPattern.sub(str(stats[moContents[index]]), formatMsg)
        print(formatMsg)        
    else:
        # if no matches, just return the original string
        print(msg) 







def getStrings(obj,strType):
    chooseFrom = obj.strings[strType]
    choice = random.choice(list(chooseFrom))
    string = chooseFrom[choice]
    return string







        

def main():

    goAdventuring = True

    while goAdventuring:
        
        foe = Encounter.Foe()
        # stats is a SimpleNamespace object, which allows access to the creature's properties,
        # which are actually in a dictionary, as if they were properties -- so the pc and the enemy
        # can be referenced by this code in the same way regardless of the internal object structure
        enemy = foe.stats
        objDict = {"enemy":vars(enemy),"pc":vars(pc)}

        displayText("\n\nYou have encountered <enemy~article> <enemy~name>! Ready your <pc~weapon>!", 
                    objDict)
        print(enemy.description)
          
        pc.init = d20.roll()
        enemy.init = d20.roll()
        pcInit = pc.init
        enemyInit = enemy.init

        displayText("\nRolling for initiative! You roll... <pc~init>",objDict)
        
        if pcInit < enemyInit:
            displayText("Too late -- while you stand there in terror, the <enemy~name> attacks!",objDict)
            playerTurn = False
        else:
            text = getStrings(pc,"encounterScream")
            msg = "As you attack, you scream " + text
            displayText(msg,objDict)
            playerTurn = True
            
        notDeadYet = True
        
        while notDeadYet:
            # fight or flee
            if playerTurn:
                chickenOption = input("\nPress C to run away, or hit Enter to fight!\t")
                if chickenOption.lower() != "c":
                    outcome = fightTurn(pc,enemy)
                else:
                    chickenFlee = "\n\nYou bravely run away, clucking at the top of your lungs," \
                    + " as \nthe <enemy~name> rages behind you. Somehow you know " \
                    + "it is daring you to \ngrow a spine someday and face it again."
                    displayText(chickenFlee,objDict)
                    if pc.treasure > 0:
                        chickenDrop = "\nAlthough you manage to keep a grip on your " \
                        + "weapon, you leave \nscattered behind you the grotesque " \
                        + "trophies that would have \nbrought you <pc~treasure> gold."
                        displayText(chickenDrop,objDict)
                    displayText("\nYou had <pc~hp> hit points remaining.",objDict)
                    goAdventuring = False
                    input("\n\n\nPress any key to exit")
                    break
                    
            else:
                outcome = fightTurn(enemy,pc)
                
            # If fighting, handle a hit 
            if outcome["hit"]:
                if playerTurn:
                    msg = "You swing your <pc~weapon> and hit the creature " \
                    + "for <pc~atkDamage> damage!"
                    playerTurn = False
                    
                else:
                    msg = "The <enemy~name> hits you for <enemy~atkDamage> damage!"
                    playerTurn = True

            # If fighting, handle a miss
            else:
                if playerTurn:
                    msg = "You miss the <enemy~name>!"
                    playerTurn = False
                else:
                    msg = "The <enemy~name> misses!"
                    playerTurn = True
            displayText(msg,objDict)
                
            # see if anyone died
            if pc.hp <= 0 or enemy.hp <= 0:
                notDeadYet = False
                lastGaspRoll = d20.roll()
        # if you died...
        if pc.hp <= 0:
            goAdventuring = False
            if lastGaspRoll > pc.lastGaspThreshold:
                msg = "\n\nYou fall, mortally wounded, and with a whiny bleat you lash out one more time... "
                outcome = fightTurn(pc,enemy)
                if enemy.hp <= 0:
                    msg = msg + "\n\nSomehow, you manage to take down your mighty foe " \
                    + "the <enemy~name> even as you fall beneath its vicious onslaught. "
                else:
                    msg = msg + "\n\nYour resistance is futile, though. Your weapon falls to " \
                    + "the ground \nand you lie crushed and bleeding, the light fading from " \
                    + "your eyes. "
            else:
                msg = "\nYou fall beneath the <enemy~name>'s vicious onslaught. Your weapon " \
                + "falls to the ground \nand you lie crushed and bleeding, the light fading " \
                + "from your eyes. "
            
            msg = msg + "\n\nThe <enemy~name> begins to feast. "

            displayText(msg,objDict)

            input("\n\n\nPress any key to exit. Come kill more things soon! ")

        # if the monster died...
        elif enemy.hp <= 0:
            if lastGaspRoll >= enemy.lastGaspThreshold:
                msg = "\nWith an unearthly shriek, the <enemy~name> keels " \
                    + "over and breathes its last, \ntaking a final swipe at you " \
                    + "before slamming into the earth. "
                fightTurn(enemy,pc)

                if pc.hp <= 0:
                    msg = msg + "\n\nIts blow rakes your face and your world turns red, " \
                    + "then \ntilts sideways and you thump to the ground facing the " \
                    + "<enemy~name> \nwhere you remain, one dead thing staring at another. "
                
                else:
                   msg = msg + "\n\nYou narrowly avoid what might have been a death blow, and take " \
                    + "\na few moments to recover your composure before approaching the still-warm \ncorpse. "
   
                msg = msg + "<enemy~dropDescription> which you estimate will bring " \
                    + "you <enemy~dropValue> gold."
            else:
                msg = "<enemy~dropDescription> which you estimate \nwill bring " \
                    + "you <enemy~dropValue> gold. "
            displayText(msg,objDict)
            pc.treasure = pc.treasure + enemy.dropValue
            if pc.hp < 10:
                print("\nYou're hurt so badly you're walking like a drunken Jack Sparrow.")
            elif pc.hp < 20:
                print("\nYou're starting to feel pretty banged up.")
            elif pc.hp < 30:
                print("\nYou feel a little tired.")
            elif pc.hp < 40:
                print("\nYou feel pretty good.")
            hunt = input("\nContinue adventure? (Y/N)\t")
            if hunt.lower() != "y":
                goAdventuring = False
                msg = "\nYou decide your grisly haul worth <pc~treasure> gold pieces " \
                + "is enough for one day. Whistling, \nyou shoulder your " \
                + "trusty <pc~weapon> and head for home " \
                + "where, \nyou hope, no monsters lurk."
                displayText(msg,objDict)
                input("\n\n\nPress any key to exit. Come kill more things soon!")
    













if __name__ == "__main__":
    #app = Flask(__name__)
    #@app.route('/')

    os.system('cls')

    PC = True
    FOE = False
    playerTurn = True
    
    d20 = DungeonDie.Die(20)
    d10 = DungeonDie.Die(10)
    d8 = DungeonDie.Die(8)
    d6 = DungeonDie.Die(6)
    d4 = DungeonDie.Die(4)
    

    pc = Character.Adventurer()
    #test = Encounter.Foe()
    #displayText("This is <article> <name> test string.",test,"enemy")
    
    main()
    # https://stackoverflow.com/questions/4979542/python-use-list-as-function-parameters

    
    