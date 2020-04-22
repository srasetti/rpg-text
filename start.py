import scripts
from classes import hero, ennemy

print("welcome to RPG Text")
print("-------------------")
print("Write Start to start or Help to learn how to play")
menuchoice = input("Choose:")

if menuchoice.lower() == "start" :  
    theHero = hero()
    theEnnemy = ennemy()
    
    result = scripts.fight(theHero,theEnnemy)
    
    print(result)
elif menuchoice.lower() == "help" :
    print("Ok let me help")
else :
    print("typo or wrong choice")
#print(menuchoice)