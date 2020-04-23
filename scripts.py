from random import randrange

def fight(hero,ennemy):
    attackCount = 0
    while ennemy.health > 0 :
        round=attack(hero,ennemy)
        round2=attack(ennemy,hero)     
        attackCount = attackCount + 1
        print("attack {} : hero Health {} Ennemy Health {}".format(attackCount,hero.health,ennemy.health))
        if hero.health <= 0 :
            result = "you died after defeating {} ennemies".format(hero.ennemiesKilled)
            return result
            break
    
    hero.ennemiesKilled += 1
    
    result = "it took {} round(s) to defeat the ennemy. You have {} health left".format(attackCount,hero.health)
    return result



def attack(fighter,victim) :
    victim.health = victim.health - randrange(1,fighter.strength)
    return victim.health
