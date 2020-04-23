import scripts
from classes import hero, ennemy

print("welcome to RPG Text")
print("-------------------")
print("Start, Help or Quit")

theHero = hero()

gameOn = True

while gameOn :
    menuchoice = input("Choose:")
    if menuchoice.lower() == "start" :  
        theEnnemy = ennemy()
        
        result = scripts.fight(theHero,theEnnemy)
        
        print(result)
    
    elif menuchoice.lower() == "help" :
        print("Ok let me help")
    elif menuchoice.lower() == "quit" :
        exit()
    elif menuchoice.lower() == "test" :        
        NewHealth = theHero.health - 10
        theHero.changeHealth(NewHealth)
        print(theHero.health)
    else :
        print("typo or wrong choice")
    #print(menuchoice)