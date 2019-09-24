# Title: Monopoly
# Created by: Leighton Lauton
# Date: 17/09/2019

# SUMMARY
# This python file will setup the game with the required amount of cash
# and the token selection. This will also be used to initialise the banker

# Module Imports
from random import randint
import pandas as pd

# Constant Variables
MAX_PLAYERS = 8
PLAYER_CSV_FILE = 'players.csv'

# Variables
booBotPlaying = False
intNumOfPlayers = 0
intDifficulty = 'Easy'
intDifficultyModifier = 1

arrPlayers = []

# Classes
class Player:
    def __init__(self, name):
        self.token = "Player ({})".format(name)
        self.cash = 1500
        self.properties = []
        self.cards = []

class Bot:
    def __init__(self, name):
        self.token = "Computer AI ({})".format(name)
        self.cash = 1500
        self.properties = []
        self.cards = []

# Functions
def selectDifficulty(index):
    difficulty = {
            1:'Easy',
            2:'Medium',
            3:'Hard'
        }

    return difficulty.get(index, "[ERROR]: Please choose one of the following:\nEasy being '1'\nMedium being '2'\nHard being '3'.")

# Gets the number of players playing the game, the difficulty wished to be played and asks for input to establish
# whether the player would like to add bots to be added to the game.
def getNumOfPlayers():
    intNumOfPlayers = int(input("Please enter how many players would like to join the game: "))
    booBotPlaying = False
    
    if (intNumOfPlayers > MAX_PLAYERS):
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

    elif (intNumOfPlayers == MAX_PLAYERS):
        print("[GAME MANAGER]: There are {} players ready to begin playing. ".format(intNumOfPlayers))
    
    elif (intNumOfPlayers < 8):
        print("[GAME MANAGER]: There are {} players ready to begin playing. ".format(intNumOfPlayers))
        booBotInclude = input("[GAME MANAGER]: Would you like to include some Computer AI to play as well? (Y/N) ")
        if (booBotInclude == "Y") or (booBotInclude == "y"):
            booBotPlaying = True
        else:
            booBotPlaying = False

    __ = input("Please enter what difficulty you would like to play on (Easy = 1, Medium = 2, Hard = 3): ")
    intDifficulty = selectDifficulty(__)

    

    return intNumOfPlayers, booBotPlaying, intDifficulty

# Creates the players
def initPlayers(intNumOfPlayers, booBotPlaying, intDifficulty):
    for i in range(intNumOfPlayers):
        player = Player(i)
        arrPlayers.append({'Token': player.token, 'Cash': player.cash,
                        'Properties': player.properties, 'Cards': player.cards})

    intNumOfBots = MAX_PLAYERS - intNumOfPlayers

    if (intNumOfBots > 0 and booBotPlaying == True):
        for i in range(intNumOfBots):
            bot = Bot(i)
            arrPlayers.append({'Token': bot.token, 'Cash': bot.cash,
                        'Properties': bot.properties, 'Cards': bot.cards})
        
    __ = pd.DataFrame(arrPlayers)
    print(__)

    return __
# Code
intNumOfPlayers, booBotPlaying, intDifficulty = getNumOfPlayers()
arrPlayers = initPlayers(intNumOfPlayers, booBotPlaying, intDifficulty)
arrPlayers.to_csv(PLAYER_CSV_FILE)
print("[SYSTEM]: SUCCESSFULLY SAVED PLAYER CSV FILE")

# DEBUGGING
print(selectDifficulty(1))
