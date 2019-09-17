# Title: Monopoly
# Created by: Leighton Lauton
# Date: 17/09/2019

# SUMMARY
# This python file will setup the game with the required amount of cash
# and the token selection. This will also be used to initialise the banker

# Module Imports
from random import randint

# Constant Variables
MAX_PLAYERS = 8

# Variables
booBotPlaying = False
intNumOfPlayers = 0

players = []

# Classes
class Player:
    def __init__(self, name):
        self.token = "Player ({})".format(name)
        self.cash = 1500
        self.properties = []
        self.cards = []

class Bot(Player):
    def __init__(self, name):
        self.token = "Computer AI ({})".format(name)
        self.cash = 1500
        self.properties = []
        self.cards = []

# Functions
# Gets the number of players playing the game
def getNumOfPlayers():
    intNumOfPlayers = int(input("Please enter how many players would like to join the game: "))
    booBotPlaying = False
    
    if (intNumOfPlayers > 8):
        print("[GAME MANAGER]: There are too many players. Please reduce the number of players to proceed. ".format(intNumOfPlayers))
        exit()
        
    elif (intNumOfPlayers == 1):
        print("[GAME MANAGER]: That's sad that you are playing by yourself. ")
        booBotInclude = input("[GAME MANAGER]: Would you like to include some Computer AI to play as well? (Y/N) ")
        if (booBotInclude == "Y") or (booBotInclude == "y"):
            booBotPlaying = True
        else:
            booBotPlaying = False
        
    elif (intNumOfPlayers < 0):
        print("[GAME MANAGER]: There cannot be less than 0 people playing. It is impossible. ")

    elif (intNumOfPlayers == 8):
        print("[GAME MANAGER]: There are {} players ready to begin playing. ".format(intNumOfPlayers))
    
    elif (intNumOfPlayers < 8):
        print("[GAME MANAGER]: There are {} players ready to begin playing. ".format(intNumOfPlayers))
        booBotInclude = input("[GAME MANAGER]: Would you like to include some Computer AI to play as well? (Y/N) ")
        if (booBotInclude == "Y") or (booBotInclude == "y"):
            booBotPlaying = True
        else:
            booBotPlaying = False

    return intNumOfPlayers, booBotPlaying

# Creates the players
def initPlayers(intNumOfPlayers, booBotPlaying):
    for i in range(intNumOfPlayers):
        p = Player(i)
        players.append(p)

    intNumOfBots = MAX_PLAYERS - intNumOfPlayers

    if (intNumOfBots > 0):
        for i in range(intNumOfBots):
            b = Bot(i)
            players.append(b)

    return players

# Code
intNumOfPlayers, booBotPlaying = getNumOfPlayers()
players = initPlayers(intNumOfPlayers, booBotPlaying)

# DEBUGGING
for p in players:
    print(p.token)
