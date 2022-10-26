#this file is used for testing the balance of the combat
#Monster List is the order everyhting will be in
import random
from re import M
import time
monList = ['Slime','Blorb','Runner','Vulkar','Grundle','Pyro','Hatchling','Spider','Mud Golem','Bony Boi']
monHp = [5,3,10,6,50,15,1,15,80,15]
monDam = [random.randint(1,3),random.randint(0,1),random.randint(1,6),random.randint(6,9),random.randint(2,8),random.randint(20,40),random.randint(1,2),random.randint(2,6),random.randint(10,20),random.randint(2,7)]
monDef = [0,0,1,2,16,-2,-10,3,5,3]
monSpd = [1,random.randint(0,1),random.randint(2,3),random.randint(7,10),1,1,1,random.randint(1,2),1,random.randint(1,1)]
monAcc = [85,70,40,20,60,250,80,85,75,68]
monSelected = 0
playerHp = 1
playerDam = 1
playerDef = 1
playerSpd = 1
playerAcc = 1

def pickStats():
#Now for the player's stats, this allows setting the expected stats of a player on levels 1-6 or to manually set stats
    print('Default Player stats?')
    print(' ')
    defaultStat = int(input('1-6 for presents, 0 for manual '))
    if(defaultStat == 0):
        playerHp = int(input('Player hp:'))
        playerDam = int(input('Player Damage:'))
        playerDef = int(input('Player Defense:'))
        playerSpd = int(input('Player Speed:'))
        playerAcc = int(input('Player Accuracy:'))
        print('Hp:',playerHp,' Damage:',playerDam,' Defense:',playerDef,' Speed:',playerSpd,' Accuracy:',playerAcc)
    elif(defaultStat == 1):
        playerHp = 20
        playerDam = 2
        playerDef = 1
        playerSpd = 1
        playerAcc = 50
        print('Hp:',playerHp,' Damage:',playerDam,' Defense:',playerDef,' Speed:',playerSpd,' Accuracy:',playerAcc)
    elif(defaultStat == 2):
        playerHp = 45
        playerDam = 5
        playerDef = 3
        playerSpd = 2
        playerAcc = 65
        print('Hp:',playerHp,' Damage:',playerDam,' Defense:',playerDef,' Speed:',playerSpd,' Accuracy:',playerAcc)
    elif(defaultStat == 3):
        playerHp = 80
        playerDam = 10
        playerDef = 10
        playerSpd = 1
        playerAcc = 75
        print('Hp:',playerHp,' Damage:',playerDam,' Defense:',playerDef,' Speed:',playerSpd,' Accuracy:',playerAcc)
    elif(defaultStat == 4):
        playerHp = 120
        playerDam = 15
        playerDef = 15
        playerSpd = 2
        playerAcc = 80
        print('Hp:',playerHp,' Damage:',playerDam,' Defense:',playerDef,' Speed:',playerSpd,' Accuracy:',playerAcc)
    elif(defaultStat == 5):
        playerHp = 160
        playerDam = 30
        playerDef = 25
        playerSpd = 2
        playerAcc = 85
        print('Hp:',playerHp,' Damage:',playerDam,' Defense:',playerDef,' Speed:',playerSpd,' Accuracy:',playerAcc)
    elif(defaultStat == 6):
        playerHp = 200
        playerDam = 45
        playerDef = 35
        playerSpd = 3
        playerAcc = 95
        print('Hp:',playerHp,' Damage:',playerDam,' Defense:',playerDef,' Speed:',playerSpd,' Accuracy:',playerAcc)
    else:
        print('I didn\'t understand that... Have set 2')
        playerHp = 45
        playerDam = 5
        playerDef = 3
        playerSpd = 2
        playerAcc = 65
        print('Hp:',playerHp,' Damage:',playerDam,' Defense:',playerDef,' Speed:',playerSpd,' Accuracy:',playerAcc)
        

#Now we get to the monster selection
def pickFight():
    print(' ')
    print(monList,' or Random')
    choice = input('Which monster would you like to fight? ')
    if(choice == 'Slime'):
        print(choice,' Selected')
        monSelected = 0
        combat(monSelected)
    elif(choice == 'Blorb'):
        print(choice,' Selected')
        monSelected = 1
        combat(monSelected)
    elif(choice == 'Runner'):
        print(choice,' Selected')
        monSelected = 2
        combat(monSelected)
    elif(choice == 'Vulkar'):
        print(choice,' Selected')
        monSelected = 3
        combat(monSelected)
    elif(choice == 'Grundle'):
        print(choice,' Selected')
        monSelected = 4
        combat(monSelected)
    elif(choice == 'Pyro'):
        print(choice,' Selected')
        monSelected = 5
        combat(monSelected)
    elif(choice == 'Hatchling'):
        print(choice,' Selected')
        monSelected = 6
        combat(monSelected)
    elif(choice == 'Spider'):
        print(choice,' Selected')
        monSelected = 7
        combat(monSelected)
    elif(choice == 'Mud Golem'):
        print(choice,' Selected')
        monSelected = 8
        combat(monSelected)
    elif(choice == 'Bony Boi'):
        print(choice,' Selected')
        monSelected = 9
        combat(monSelected)
    elif(choice == 'Random'):
        print(choice,' Selected')
        monSelected = random.randint(0,9)
        combat(monSelected)
    else:
        print('I don\'t know what you mean... Doing Random instead')
        print(choice,' Selected')
        monSelected = random.randint(0,9)
        combat(monSelected)
    
#Function to show the mob stats
def showMonStats(monStats):
    print(' ')
    print('Fight with:',monStats[0])
    print(monStats[0],'| Hp:',monStats[1],' Damage:',monStats[2],' Defense:',monStats[3],' Speed:',monStats[4],' Accuracy:',monStats[5])

#A transition function to choose what move to take
def combat(monSelected):
    #now we will make a new group for the monster stats
    monStats = [monList[monSelected],monHp[monSelected],monDam[monSelected],monDef[monSelected],monSpd[monSelected],monAcc[monSelected]]
    showMonStats(monStats)
    print(' ')
    initiative = random.randint(0,3)
    if(initiative == 1) | (initiative == 2) | (initiative == 3):
        choice = input('So what do you want to do? ')
        if(choice == 'Attack'):
            print('Attacking')
            playerAttack(monStats)
        elif(choice == 'Run'):
            print('Trying to run away')
        elif(choice == 'Redo'):
            pickStats()
            pickFight()
    else:
        print('The ',monStats[0],' ambushes you!')
        monAttack(monStats)

#when the mob attacks
def monAttack(monStats):
    print(' ')
    print('The',monStats[0],'Attacks!')
    trueDamage = (monStats[2] - playerDef)
    playerHp -= trueDamage
    
#when the player attacks
def playerAttack(monStats):
    print('')
    print('You attack the ',monStats[0])
    trueDamage = (playerDam - monStats[3])
    monStats[1] -= trueDamage
    combat(monStats)
    
    
    
    
pickStats()
pickFight()
