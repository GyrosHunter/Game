import csv


class Person:
    max_health = 100

    def __init__(self, name):

        self.features = {}
        with open(f"./PEOPLE/{name}.txt", 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                if row:
                    key, feature = row
                    self.features[key] = feature

        self.first_name = self.features["first_name"]
        self.last_name = self.features["last_name"]
        self.full_name = ' '.join([self.first_name, self.last_name])

        self.health = self.max_health
        self.age = int(self.features["age"])

        if self.features["items"]:
            self.items = [item.replace('_', ' ') for item in self.features["items"].split(' ')]
        else:
            self.items = []

    def __repr__(self):
        return f"Meet {self.full_name}."

    def look_at(self):
        print(f"{self.features['description']}")

    def gain_health(self, value: int):
        if value < 10:
            print("Nice!")
        else:
            print("Fuck, yea! I feel much better now!")
        self.health += value
        if self.health > self.max_health:
            self.health = self.max_health
        print(f"{self.full_name} has {self.health} health points.")

    def lose_health(self, value: int):
        if value < 10:
            print("Ouch!")
        else:
            print("Jesus, that hurt as fuck!")
        self.health -= value
        if self.health <= 0:
            print(self.die())
        else:
            print(f"{self.full_name} loses {value} health points and has {self.health} health points left.")

    def die(self):
        print(f"{self.full_name} has died")

    def show_items(self):
        if self.items:
            items = ', '.join(self.items)
            print(f"Here are the items {self.full_name} is willing to sell: {items}.")
        else:
            print(f"{self.full_name} has nothing to sell.")

    def add_item(self, item: str):
        self.items.append(item)

    def remove_item(self, item: str):
        if item in self.items:
            self.items.remove(item)

    def sell_item(self, item: str):
        if item in self.items:
            self.remove_item(item)
            print("Here you are, kind sir!")
        else:
            print(f"I have no such thing for sale!")
