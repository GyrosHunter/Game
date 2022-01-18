from CLASSES.class_location import Location
from CLASSES.class_NPC import NPC
from CLASSES.class_item import Item
from CLASSES.class_player import Player
import csv
import os


class ContentGenerator:

    def class_generator(self):
        locations = {}
        npcs = {}
        items = {}
        directories = ("TXT/LOCATIONS", "TXT/ITEMS", "TXT/NPCS")
        for directory in directories:
            for filename in os.listdir(directory):
                features = {}
                with open(f"{directory}/{filename}", 'r') as file:
                    reader = csv.reader(file)
                    for row in reader:
                        if row:
                            key, feature = row
                            features[key] = feature

                if f"{directory}" == "TXT/LOCATIONS":
                    locations[filename[:-4]] = Location(features)
                elif f"{directory}" == "TXT/NPCS":
                    npcs[filename[:-4]] = NPC(features)
                elif f"{directory}" == "TXT/ITEMS":
                    items[filename[:-4]] = Item(features)

        return locations, npcs, items

    def character_generator(self):
        occupation = "nightrunner"      # input("What is your trade? ")
        first_name = "John"             # input("What is your name? ")
        last_name = "Wayne"             # input("Last name? ")
        age = 38                        # input("How old are you? ")
        age = int(age)
        features = {}
        with open(f"TXT/CHARACTERS/{occupation}.txt", 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                if row:
                    key, feature = row
                    features[key] = feature
        player = Player(features, occupation, first_name, last_name, age)
        return player
