import scripts


print("welcome to RPG Text")
print("-------------------")
print("Write Start to start or Help to learn how to play")
menuchoice = input("Choose:")

if menuchoice.lower() == "start" :  
    ennemy_str = 100
    result = scripts.fight(ennemy_str)
    print(result)
elif menuchoice.lower() == "help" :
    print("Ok let me help")
else :
    print("typo or wrong choice")
#print(menuchoice)