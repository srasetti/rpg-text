from random import randrange

def fight(hero,ennemy):
    round=attack(hero,ennemy) 
    result = "The health of the ennemy is now {}".format(round)
    return result

def attack(fighter,victim) :
    victim.health = victim.health - randrange(1,fighter.strength)
    return victim.health
