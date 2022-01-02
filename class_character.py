import csv


class Character:
    max_health = 100

    def __init__(self, occupation: str, first_name: str, last_name: str, age: int):

        self.features = {}
        with open(f"./CHARACTERS/{occupation}.txt", 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                if row:
                    key, feature = row
                    self.features[key] = feature

        self.first_name = first_name
        self.last_name = last_name
        self.full_name = ' '.join([self.first_name, self.last_name])
        self.bio = self.features["bio"]

        self.occupation = occupation
        self.health = self.max_health
        self.age = age

        if self.features["items"]:
            self.items = [item.replace('_', ' ') for item in self.features["items"].split(' ')]
        else:
            self.items = []

        if self.features["skills"]:
            self.skills = [skill.replace('_', ' ') for skill in self.features["skills"].split(' ')]
        else:
            self.skills = []

        self.stats = [stat for stat in self.features["stats"].split(' ')]
        self.attack = int(self.stats[0])
        self.defense = int(self.stats[1])
        self.intelligence = int(self.stats[2])

    def __repr__(self):
        return f"Meet {self.full_name}, an average {self.occupation} motherfucker..."

    def look_at(self):
        print(f"{self.features['description']}")

    def gain_health(self, value: int):
        print(f"You have gained {value} health points")
        self.health += value
        if self.health > self.max_health:
            self.health = self.max_health
        print(f"You now have {self.health} health points.")

    def lose_health(self, value: int):
        print (f"You have lost {value} health points")
        self.health -= value
        if self.health <= 0:
            print(self.die())
        else:
            print(f"You have lost {value} health points and now have {self.health} left.")

    def die(self):
        print(f"You dead, bro.")

    def show_items(self):
        if self.items:
            items = ', '.join(self.items)
            print(f"Currently your inventory consists of the following items: {items}.")
        else:
            print(f"Your inventory is empty.")

    def add_item(self, item: str):
        self.items.append(item)
        print(f"{item.title()} has been added to your inventory.")

    def remove_item(self, item: str):
        if not self.items:
            print("Your inventory is empty.")
        elif item in self.items:
            self.items.remove(item)
            print(f"{item.title()} has been removed from your inventory.")
        elif item not in self.items:
            print("You don't have it!")
