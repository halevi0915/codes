import time
import random
from modules import hero

név = input("válassz nevet: ")
time.sleep(1)
print("----------------------------------------")
time.sleep(1)

def randomPercentage(percent): 
    perc = float(percent)
    num = float(random.randint(0, 100))
    if num <= perc:
        return True
    return False

tank = hero(4,35,0.50,30)          # str hp def speed
assasin = hero(7,25,1,70)
heavy = hero(9,30,0.75,40)
paladin = hero(6,40,1,50)

herok = ["tank","assasin","heavy","paladin"]
computer = random.choice(herok)
print("az ellenfeled:",computer)

time.sleep(1)

player = None
while player not in herok:
    player = input("válassz egy karaktert: ").lower()
    while player == computer:
        player = input("válassz egy karaktert: ").lower()

if player == "tank":
    strengt = tank.strengt
    health = tank.health
    defense = tank.defense
    speed = tank.speed
elif player == "assasin":
    strengt = assasin.strengt
    health = assasin.health
    defense = assasin.defense
    speed = assasin.speed
elif player == "heavy":
    strengt = heavy.strengt
    health = heavy.health
    defense = heavy.defense
    speed = heavy.speed
elif player == "paladin":
    strengt = paladin.strengt
    health = paladin.health
    defense = paladin.defense
    speed = paladin.speed

if computer == "tank":
    cstrengt = tank.strengt
    chealth = tank.health
    cdefense = tank.defense
    cspeed = tank.speed
elif computer == "assasin":
    cstrengt = assasin.strengt
    chealth = assasin.health
    cdefense = assasin.defense
    cspeed = assasin.speed
elif computer == "heavy":
    cstrengt = heavy.strengt
    chealth = heavy.health
    cdefense = heavy.defense
    cspeed = heavy.speed
elif computer == "paladin":
    cstrengt = paladin.strengt
    chealth = paladin.health
    cdefense = paladin.defense
    cspeed = paladin.speed

print("----------------------------------------")
time.sleep(1)
print(player,": ",strengt," str ",health," hp ",defense*100," def ",speed," speed ","\n              VS\n",computer,": ",cstrengt," str ",chealth," hp ",cdefense*100," def ",cspeed," speed ",sep='')
time.sleep(1)
print("----------------------------------------")
time.sleep(1)

def cpumove():
    global health
    global chealth
    print("cpu jön")
    time.sleep(1)
    if randomPercentage(70):
        print("cpu támad")
        time.sleep(1)
        if randomPercentage(100-speed):
            if randomPercentage(50):
                health -= cstrengt*2
                print("criteltek!","hp:",health + cstrengt*2,"-->",health)
                time.sleep(1)
                print("----------------------------------------")
                time.sleep(3)

            else:
                health -= cstrengt*defense
                print("eltaláltak!","hp:",health + cstrengt*defense,"-->",health)
                time.sleep(1)
                print("----------------------------------------")
                time.sleep(3)

        else:
            print("nem találtak el!")
            time.sleep(1)
            print("----------------------------------------")
            time.sleep(3)

        if health <= 0:
            print("vesztettél!")
            time.sleep(30)
        
    else:
        print("cpu healel")
        time.sleep(1)
        chealth += 5
        print("ellenség hp:",chealth - 5,"-->",chealth)
        time.sleep(1)
        print("----------------------------------------")
        time.sleep(3)

def playermove():
    global nextmove
    global chealth
    global health
    print(név," jön")

    time.sleep(1)

    lepes = ["attack","heal","quit"]
    nextmove = None
    while nextmove not in lepes:
        nextmove = input("Mit lépsz?: ").lower()
    time.sleep(1)
    if nextmove == "attack":
        if randomPercentage(100-cspeed):
            if randomPercentage(50):
                chealth -= strengt*2
                print("critelt!","ellenség hp:",chealth + strengt*2,"-->",chealth)
                time.sleep(1)
                print("----------------------------------------")
                time.sleep(3)

            else:
                chealth -= strengt*cdefense
                print("talált!","ellenség hp:",chealth + strengt*cdefense,"-->",chealth)
                time.sleep(1)
                print("----------------------------------------")
                time.sleep(3)

        else:
            print("nem talált!")
            time.sleep(1)
            print("----------------------------------------")
            time.sleep(3)

        if chealth <= 0:
            print("nyertél!")
            time.sleep(30)
    elif nextmove == "heal":
        health += 10
        print("hp:",health - 10,"-->",health)
        time.sleep(1)
        print("----------------------------------------")
        time.sleep(1)

esely = random.randint(0,1)

if esely == 0:
    playermove()
        
    
elif esely == 1:
    cpumove()
time.sleep(1)        
while True:
    if esely == 0:
        cpumove()
        esely = 1
        time.sleep(2)
    elif esely == 1:
        playermove()
        esely = 0
        if nextmove == "quit":
            break
        time.sleep(1)




