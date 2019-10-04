# Title: Monopoly - Properties
# Created by: Leighton Lauton
# Date: 04/10/2019

# SUMMARY
# This python script will handle the properties, housing
# costs, rent and anything else to do with the properties

# Module Imports
import pandas as pd

# Constant Variables
PROPERTY_CSV_PATH = 'data/'
PROPERTY_CSV_NAME = 'properties.csv'
PROPERTY_CSV_FILE = PROPERTY_CSV_PATH + PROPERTY_CSV_NAME

PROPERTY_COUNT = 28

PROPERTIES = pd.read_csv(PROPERTY_CSV_FILE)

# Variables
arrProperties = []

cash = 100000

# Classes
class Property:
    def __init__(self):
        self.name = ""
        self.cost = 0
        self.rent = 0
        self.mortgage = 0
        self.group = ""

        self.boughtHouse1 = False      
        self.boughtHouse2 = False
        self.boughtHouse3 = False
        self.boughtHouse4 = False
        self.boughtHotel = False

        self.bought = False

    def BuyProperty(self, name, cash):
        for index, prop in PROPERTIES.iterrows():
            if (prop['Title'] == name):
                prop['Bought?'] = True
                
                cost = prop['Cost']
                rent = prop['Rent']
                mortgage = prop['Mortgage']
                group = prop['Group']
                bought = prop['Bought?']
                
                # Add each property value to an array if the property is bought
                self.name = name
                self.cost = cost
                self.rent = rent
                self.mortgage = mortgage
                self.group = group
                self.bought = bought
                
                arrProperties.append(self.name)
                arrProperties.append(self.cost)
                arrProperties.append(self.rent)
                arrProperties.append(self.mortgage)
                arrProperties.append(self.group)
                arrProperties.append(self.bought)

                cash = cash - cost

                print("[GAME MANAGER]: {} has now been bought. ".format(self.name))

                return cash


# DEBUGGING
p = Property()
props = ["Mediterranean Ave. ", "Baltic Ave."]
for i in range(2):
    cash = p.BuyProperty(props[i], cash)
print(arrProperties, cash)
