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

# Classes
class Property:
    def __init__(self):
        self.name = ""
        self.cost = 0
        self.rent = 0
        self.mortgage = 0
        self.group = ""

        self.house1 = False
        self.house2 = False
        self.house3 = False
        self.house4 = False
        self.hotel = False

        self.bought = False

    def Buy(self, name):
        for index, title, cost, rent in PROPERTIES.iterrows():
            if (title['Title'] == name):
                # Add each property value to an array if the property is bought
                arrProperties.append(name)


# DEBUGGING
p = Property()
p.Buy("Mediterranean Ave. ")
print(arrProperties)
