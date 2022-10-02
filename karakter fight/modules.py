import random


class hero:

    def __init__(self,strengt,health,defense,speed):
        
        self.strengt = strengt
        self.health = health
        self.defense = defense
        self.speed = speed
        
    def attack(self):
        print("attack")

    def heal(self):
        print("heal")

def cpumove():
    cpuesely = random.randint(0,1)

    print("cpu jön")
    if cpuesely == 0:
        print("cpu tamad")
        
    elif cpuesely == 1:
        print("cpu healel")



