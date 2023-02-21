import time
import sys
import random


def wrongKeying():                                                  #If the user mistypes
    print("You Have Made Incomplate or Incorrect Keying!")


def addDot():  # Made to Give Game Look
    print(".")
    time.sleep(.5)
    print("..")
    time.sleep(.5)
    print("...")
    time.sleep(.5)


def damageValue():                              # Here we generate random damage value between (1-29)
    return random.choice(range(1, 29))


class player:
    def __init__(self, name, life=100, power=100):
        self.name = name
        self.life = life
        self.power = power

    def showKnowledges(self):                                   
        print("""
        Name : {}
        Life : {}
        Power : {}
        """.format(self.name, self.life, self.power))

    def attack(self, enemy):
        conclusion = self.attack_DefendDecisive()
        if conclusion == 1:
            print("The Attack Has Begun...")
            time.sleep(1)
            print("Attack Successful!")
            self.power -= 10
            damage = damageValue()
            enemy.life -= damage
            self.showKnowledges()
            enemy.showKnowledges()
        else:
            print("The Attack Has Begun...")
            time.sleep(1)
            print("Attack Failed!")
            self.power -= 8
            self.showKnowledges()
            enemy.showKnowledges()

    def defense(self, enemy):
        conclusion = self.attack_DefendDecisive()
        if conclusion == 1:
            print("The Defense Has Begun...")
            time.sleep(1)
            print("Defense Successful!")
            enemy.power -= 10
            damage = damageValue()
            enemy.life -= damage
            self.showKnowledges()
            enemy.showKnowledges()
        else:
            print("The Defense Has Begun...")
            time.sleep(1)
            print("Defense Failed!")
            enemy.power -= 8
            damage = damageValue()
            self.life -= damage
            self.showKnowledges()
            enemy.showKnowledges()

    def attack_DefendDecisive(self):  # With This Function We Determine Whether To Fight or Defend
        return random.randint(1, 2)

    def exit(self):
        print("Game Is Closing...")
        addDot()
        sys.exit()


print("The Game Is Starting")
addDot()
player1 = player(input("Please Enter The Name Of First Player : "))
player2 = player(input("Please Enter The Name Of Second Player : "))


while True:
    move = input("""
    1-Attack
    2-Defend
    3-Exit
    Choose : """)

    if move == "1":
        player1.attack(player2)
        
    elif move == "2":
        player1.defense(player2)
        
    elif move == "3":
        player1.exit()
        
    else:
        wrongKeying()
        exit()

    if player2.life <= 0 or player2.power <= 0:
        print("Winner Of The Game : ", player1.name)
        break
    if player1.life <= 0 or player1.power <= 0:
        print("Winner Of The Game : ", player2.name)
        break
