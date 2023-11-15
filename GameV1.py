import os, time, random

roomsList = [[0, "outside", "the exit is locked"],
             [1, "Dark Room", "dark room with 4 walls painted black, and a dim flickering lanter on the ceiling. It has loose wooden beans scattered on the floor"],
            [2, "Damp Room", "damp room with the smell of fungus in the air. the limewashed walls have damp and mold slowly creeping up them, and the ceiling slowly drips a rust coloured liquid"],
            [3, "Wooden Room", "large room with wood panelled walls and an ornate ceiling that has definetly seen better days. There are tables full of rotting food lined up in it."]]

items = [[0, "Stone", "dmg", 1],
            [1, "Wooden Stick", "dmg", 2],
            [2, "APPle", "heal", 10],
            [3, "Amulet", "heal", 20],
            [4, "Sword of Lost Souls", "dmg", 10],
            [5, "Mystery Potion", "mstr", -3],
            [6, "Mystery Potion", "mstr", -3],
            [7, "Mystery Potion", "mstr", -1],
            [8, "Mystery Potion", "mstr", -1],
            [9, "Mystery Potion", "mstr", 3],
            [10, "Mystery Potion", "mstr", 1],
            [11, "Iron Sword", "dmg", 2],
            [12, "Wooden Stick", "dmg", 1],
            [13, "Wooden Stick", "dmg", 2],
            [14, "Wooden Stick", "dmg", 1],
            [15, "Wooden Stick", "dmg", 2],
            [16, "Wooden Stick", "dmg", 1],
            [17, "Wooden Stick", "dmg", 2],
            [18, "Wooden Stick", "dmg", 1],
            [19, "Iron Sword", "dmg", 3],
            [20, "Iron Sword", "dmg", 4],
            [21, "Iron Sword", "dmg", 3]]

enemies = [[1, "Zombie", "dead zombie", 10, 30],
            [2, "Skeleton", "dead skeleton", 13, 30],
            [3, "Nightmare Eater", "la creatura", 19, 70],
            [4, "Zombie", "dead zombie", 10, 30],
            [5, "Skeleton", "dead skeleton", 13, 30],
            [6, "Zombie", "dead zombie", 10, 30],
            [7, "Skeleton", "dead skeleton", 13, 30],
            [9, "Angry Dinosaur", "its angry, what do you expect", 17, 30],
            [9, "Angry Dinosaur", "its angry, what do you expect", 16, 30]
            ]

class Room:
    num = 0
    name = ""
    contentsType = ""
    contents = []
    contentsThere = True
    description = ""
    N = ""
    E = ""
    s = ""
    w = ""

    def __init__(self, id, num):
        self.num = num
        id = id = 1
        self.name = roomsList[id][1]
        self.description = roomsList[id][2]

        #thing = random.choice(["item", "item", "item", "item", "enemy", "enemy", "enemy", "enemy", "enemy", "enemy"])
        thing = random.choice(["item", "enemy"])
        #thing = "enemy"
        if thing == "item":
            self.contentsType = "item"
            self.contents = items[random.randint(0, len(items)-1)]
        else:
            self.contentsType = "enemy"
            self.contents = enemies[random.randint(0, len(enemies)-1)]
        


    def setN(self,room):
        self.N = room

    def setE(self,room):
        self.E = room

    def setS(self,room):
        self.S = room

    def setW(self,room):
        self.W = room

    def setEnterance(self):
        self.name = "enterance"
        self.description = "enterance to the dungeon. The Exit is locked."
        #self.contentsType = "Item"
        #self.contents = 0
        self.contentsThere = False
        self.S = Room(0, 0)





class Player:
    hp = 100
    str = 10
    inv= []

    def __init__(self):
        self.hp = 100
        self.strength = 10   

    def changeStr(self, amnt):
        self.strength += int(amnt)

    def changeHp(self,amnt):
        self.hp += int(amnt)



def roomGenID():
    return random.randint(1, roomsList.len()-1)


def hpCheck(player):
    #print("HP check------------------------------------------------------------------------")
    if player.hp <= 0:
        print("You Died")
        time.sleep(3)
        os.remove("GameCopy.py")
        return False
    else:
        return True




rooms=[""]
currentRoomNum = 0
player = Player()
life = True
#difficulty = 1

print("start")
print("welcome to the dungeon")


rooms[0] = Room(0, 0)
rooms[0].setEnterance()

while life:
    print()
    print("you are in the "+rooms[currentRoomNum].name+". This is a "+rooms[currentRoomNum].description+". You can go N, E, S or W. ")
    
    if currentRoomNum != 0 and rooms[currentRoomNum].contentsType == "item":
        item = rooms[currentRoomNum].contents
        #print(index)
        #item = items[index]
        print("There is something inide this room, it is a "+str(item[1]))
        if item[2] == "dmg":
            player.inv.append([item[1], item[3]])
            print(str(item[1])+" added to inventory.")
        if item[2] == "heal":
            player.hp = player.hp + item[3]
            print("Healed "+str(item[3])+" hp.")
        if item[2] == "mstr":
            player.strength = player.strength + item[3]
            print("Strength changed by "+str(item[3])+". Your strength is now "+str(player.strength))

    elif currentRoomNum != 0 and rooms[currentRoomNum].contentsType == "enemy":
        enemy = rooms[currentRoomNum].contents
        print("you found a "+enemy[1]+"!")
        #print(player.inv)
        #print(len(player.inv))

        statement = "what would you like to fight it with? You have: fists(strength +0, enter \"0\")"
        for i in range (0, len(player.inv)):
            statement = statement + ", "+str(player.inv[i][0])+"(strength +"+str(player.inv[i][1])+", enter \""+str(i+1)+"\")"
        statement = statement + "."
        print(statement)
        use = input()
        if use !="0":
            try:
                use = int(use) -1
                playerTempStrength = player.strength + player.inv[use][1]
                print("fighting with "+player.inv[use][0])
                del player.inv[use]
            except:
                print("fighting with fists")
                playerTempStrength = player.strength
        else:
            print("fighting with fists")
            playerTempStrength = player.strength

        playerVal = random.randint(1, 20) + playerTempStrength
        enemyVal = random.randint(1, 20) + enemy[3]
        if playerVal >= enemyVal:
            print("The enemy attacked with "+str(enemyVal)+", but you won with "+str(playerVal)+"!")
            print("Your hp is now "+str(player.hp))
        else:
            print("you attacked with "+str(playerVal)+", but the enemy won with "+str(enemyVal)+"!")
            player.hp = player.hp - enemy[4]
            print("Your hp is now "+str(player.hp))
        
    life = hpCheck(player)
    #print("")
    #print(str(life))
    #print("")
    #print("why-------------------------------------")

    if life:
        direction = input("Where do you want to go next? (N, E, S, W)").upper()
        nextRoomNum = len(rooms)
        if direction == "N":
            if rooms[currentRoomNum].N != "":
                currentRoomNum = rooms[currentRoomNum].N.num
            rooms.append(Room(roomGenID, nextRoomNum))
            rooms[currentRoomNum].setN(rooms[nextRoomNum])
            currentRoomNum = nextRoomNum
        elif direction == "E":
            rooms.append(Room(roomGenID, nextRoomNum))
            rooms[currentRoomNum].setE(rooms[nextRoomNum])
            currentRoomNum = nextRoomNum
        elif direction == "S":
            rooms.append(Room(roomGenID, nextRoomNum))
            rooms[currentRoomNum].setS(rooms[nextRoomNum])
            currentRoomNum = nextRoomNum
        elif direction == "W":
            rooms.append(Room(roomGenID, nextRoomNum))
            rooms[currentRoomNum].setW(rooms[nextRoomNum])
            currentRoomNum = nextRoomNum
        else: 
            print("That's not an accepted input")
    #pos=0
    #rooms[currentRoomNum+1] = Room(str("currentRoomNum"))
    #rooms[currentRoomNum+1].link(rooms[currentRoomNum], pos)


#print("you lost")


#os.remove("FileRemoveTest.py")