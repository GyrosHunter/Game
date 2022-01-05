from CLASSES.class_ContentGenerator import ContentGenerator


class Person:
    max_health = 100
    base_stats = ("attack", "defense", "intelligence", "health")
    _Generator = ContentGenerator()

    def __init__(self, name: str):

        self.features = self._Generator.generate_from_txt(name)

        self.first_name = self.features["first_name"]
        self.last_name = self.features["last_name"]
        self.full_name = ' '.join([self.first_name, self.last_name])

        self.occupation = self.features["occupation"]
        self.health = self.max_health
        self.age = int(self.features["age"])
        self.description = self.features["description"]

        if self.features["stats"]:
            person_stats = [stat for stat in self.features["stats"].split(' ')]
            person_stats.append(self.health)
            self.stats = {self.base_stats[i]: int(person_stats[i]) for i in range(0, len(self.base_stats))}
        else:
            self.stats = dict.fromkeys(self.base_stats, "N/A")

        if self.features["skills"]:
            self.skills = [skill.replace('_', ' ') for skill in self.features["skills"].split(' ')]
        else:
            self.skills = []

        if self.features["items"]:
            self.items = [item.replace('_', ' ') for item in self.features["items"].split(' ')]
        else:
            self.items = []

        # METHODS

    def __repr__(self):
        return f"Meet {self.full_name}."

    def look_at_self(self):
        print(self.description)

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

    def show_stats(self):
        print(f"Here are {self.full_name}'s stats:")
        print(f"Attack:       {self.stats['attack']}")
        print(f"Defense:      {self.stats['defense']}")
        print(f"Intelligence: {self.stats['intelligence']}")
        print(f"Health:       {self.stats['health']}")

    def show_skills(self):
        if self.items:
            skills = ', '.join(self.skills)
            print(f"{self.full_name} has mastered the following skills: {skills}.")
        else:
            print(f"{self.full_name} has no skills.")

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
