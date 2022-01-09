from CLASSES.class_location import Location
from CLASSES.class_NPC import NPC
from CLASSES.class_item import Item
from CLASSES.class_player import Player
from CLASSES.class_venue import Venue
import csv
import os


class ContentGenerator:

    def class_generator(self):
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
                    features = self.compile_features(reader, features)

                if f"{directory}" == "TXT/LOCATIONS":
                    self.generate_locations(features)
                    locations[filename[6:-4]] = Location(features)

                elif f"{directory}" == "TXT/NPCS":
                    self.generate_npcs(features)
                    npcs[filename[:-4]] = NPC(features)

                elif f"{directory}" == "TXT/ITEMS":
                    self.generate_items(features)
                    items[filename[:-4]] = Item(features)

                elif f"{directory}" == "TXT/VENUES":
                    self.generate_venues(features)
                    venues[filename[:-4]] = Venue(features)

        player = self.generate_character()
        return locations, npcs, items, venues, player

    def compile_features(self, reader, features: dict) -> dict:
        for row in reader:
            if row:
                key, feature = row
                features[key] = feature
        return features

    def generate_locations(self, features: dict):
        self.directions_generator(features)
        self.available_directions_generator(features)
        self.exit_locations_generator(features)
        self.location_features_generator(features)

    def generate_npcs(self, features: dict):
        self.person_stats_generator(features)

    def generate_items(self, features: dict):
        self.item_stats_generator(features)

    def generate_venues(self, features: dict):
        pass

    def generate_character(self):

        occupation = "nightrunner"  # input("What is your trade? ")
        first_name = "John"         # input("What is your name? ")
        last_name = "Wayne"         # input("Last name? ")
        age = 38                    # input("How old are you? ")
        age = int(age)

        features = {}
        with open(f"TXT/CHARACTERS/{occupation}.txt", 'r') as file:
            reader = csv.reader(file)
            features = self.compile_features(reader, features)

        self.person_stats_generator(features)
        return Player(features, occupation, first_name, last_name, age)

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

    def location_features_generator(self, features: dict) -> dict:

        # Generates items, people and venues of the location
        things = ("items", "people", "venues")
        for thing in things:
            if thing in features:
                features[thing] = [unit.replace('_', ' ') for unit in features[thing].split(' ')]
            else:
                features[thing] = []
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

    def person_stats_generator(self, features: dict) -> dict:

        person_stats = ("attack", "defense", "intelligence", "health")
        features["stats"] = {}
        for stat in person_stats:
            if stat in features:
                features["stats"][stat] = int(features[stat])
            else:
                features["stats"][stat] = 0
        return features


class GeneratorSQL:

    def class_generator_sql(self):
        return NotImplementedError()
