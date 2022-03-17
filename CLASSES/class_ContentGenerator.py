from CLASSES.class_location import Location
from CLASSES.class_NPC import NPC
from CLASSES.class_item import Item
from CLASSES.class_player import Player
from CLASSES.class_venue import Venue
import csv
import os


class ContentGenerator:

    def __init__(self):
        self.txt = GeneratorTXT()
        self.sql = GeneratorSQL()

    def class_generator_new(self, source: str):
        if source == 'TEXT':
            return GeneratorTXT.class_generator_txt(self.txt)
        elif source == 'SQL':
            return GeneratorSQL.class_generator_sql(self.sql)


class GeneratorTXT:
    all_directions = ("east", "west", "south", "north")

    def class_generator_txt(self):

        locations = {}
        npcs = {}
        items = {}
        venues = {}
        directories = ("TXT/LOCATIONS", "TXT/ITEMS", "TXT/NPCS", "TXT/VENUES")
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
                    self.generate_locations(features)
                    locations[filename[6:-4]] = Location(features)
                elif f"{directory}" == "TXT/NPCS":
                    self.person_stats_generator(features)
                    npcs[filename[:-4]] = NPC(features)
                elif f"{directory}" == "TXT/ITEMS":
                    self.item_stats_generator(features)
                    items[filename[:-4]] = Item(features)
                elif f"{directory}" == "TXT/VENUES":
                    self.generate_venues(features)
                    venues[filename[:-4]] = Venue(features)

        player = self.character_generator()
        return locations, npcs, items, venues, player

    def generate_locations(self, features):
        self.directions_generator(features)
        self.available_directions_generator(features)
        self.exit_locations_generator(features)
        self.features_generator(features)

    def generate_venues(self, features):
        self.features_generator(features)

    def character_generator(self):
        occupation = "priest"  # input("What is your trade? ")
        name = "Jack"  # input("What is your name? ")
        age = 38  # input("How old are you? ")
        age = int(age)
        features = {}
        with open(f"TXT/CHARACTERS/{occupation}.txt", 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                if row:
                    key, feature = row
                    features[key] = feature

        self.person_stats_generator(features)
        self.person_items_generator(features)
        self.person_skills_generator(features)
        player = Player(features, occupation, name, age)
        return player

    def person_items_generator(self, features: dict) -> dict:
        if features["items"]:
            features["items"] = [item.replace('_', ' ') for item in features["items"].split(' ')]
        else:
            features["items"] = []
        return features

    def person_skills_generator(self, features: dict) -> dict:
        if features["skills"]:
            features["skills"] = [skill.replace('_', ' ') for skill in features["skills"].split(' ')]
        else:
            features["skills"] = []
        return features

    def person_stats_generator(self, features: dict) -> dict:

        person_stats = ("attack", "defense", "intelligence", "health")
        features["stats"] = {}
        for stat in person_stats:
            if stat in features:
                features["stats"][stat] = int(features[stat])
            else:
                features["stats"][stat] = 0
        return features

    def item_stats_generator(self, features: dict) -> dict:

        item_stats = ("attack", "defense", "intelligence", "health", "durability", "weight")
        features["stats"] = {}
        for stat in item_stats:
            if stat in features:
                features["stats"][stat] = int(features[stat])
            else:
                features["stats"][stat] = "N/A"
        return features

    def directions_generator(self, features: dict) -> dict:

        features['directions'] = {}
        for direction in self.all_directions:
            features['directions'][direction] = features[f"{direction}"]
        return features

    def available_directions_generator(self, features: dict) -> dict:

        features['available_directions'] = []
        for direction in self.all_directions:
            if features[f"{direction}_exit_location"]:
                features['available_directions'].append(direction)
        return features

    def exit_locations_generator(self, features: dict) -> dict:

        features['exit_locations'] = {}
        for direction in features['available_directions']:
            features['exit_locations'][direction] = features[f"{direction}_exit_location"]
        return features

    def features_generator(self, features: dict) -> dict:

        for thing in ("items", "people", "venues"):
            if features[thing]:
                features[thing] = [unit.replace('_', ' ') for unit in features[thing].split(' ')]
            else:
                features[thing] = []
        return features


class GeneratorSQL:
    pass

    def class_generator_sql(self):
        pass
