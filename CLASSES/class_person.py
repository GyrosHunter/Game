class Person:
    max_health = 100

    def __init__(self, features: dict):

        self.name = features["name"]
        self.occupation = features["occupation"]
        self.health = self.max_health
        self.age = int(features["age"])
        self.description = features["description"]
        self.stats = features["stats"]
        self.items = features["items"]
        self.skills = features["skills"]

    def __repr__(self):
        return self.name

    def show_self(self):
        return self.description

    def gain_health(self, value: int):
        if value < 10:
            print("Nice!")
        else:
            print("Fuck, yea! I feel much better now!")
        self.health += value
        if self.health > self.max_health:
            self.health = self.max_health
        print(f"{self.name} has {self.health} health points.")

    def lose_health(self, value: int):
        if value < 10:
            print("Ouch!")
        else:
            print("Jesus, that hurt as fuck!")
        self.health -= value
        if self.health <= 0:
            print(self.die())
        else:
            print(f"{self.name} loses {value} health points and has {self.health} health points left.")

    def die(self):
        print(f"{self.name} has died")

    def show_stats(self):
        return f"Here are {self.name}'s stats:\
                Attack:       {self.stats['attack']}\
                Defense:      {self.stats['defense']}\
                Intelligence: {self.stats['intelligence']}\
                Health:       {self.stats['health']}"

    def show_skills(self):
        if self.items:
            skills = ', '.join(self.skills)
            print(f"{self.name} has mastered the following skills: {skills}.")
        else:
            print(f"{self.name} has no skills.")

    def show_items(self):
        if self.items:
            items = ', '.join(self.items)
            print(f"Here are the items {self.name} is willing to sell: {items}.")
        else:
            print(f"{self.name} has nothing to sell.")

    def add_item(self, item: str):
        self.items.append(item)

    def remove_item(self, item: str):
        if item in self.items:
            self.items.remove(item)
