from CLASSES.class_person import Person


class Player(Person):

    def __init__(self, features, occupation: str, name: str, age: int):
        super().__init__(features)

        self.name = name.title()
        self.age = age
        self.bio = features["bio"]
        self.occupation = occupation

    def __repr__(self):
        return self.name

    def my_story(self):
        return self.bio

    def look_at_self(self):
        print(self.description)

    def gain_health(self, value: int):
        print(f"You have gained {value} health points.")
        self.health += value
        if self.health > self.max_health:
            self.health = self.max_health
        print(f"You now have {self.health} health points.")

    def lose_health(self, value: int):
        print(f"You have lost {value} health points.")
        self.health -= value
        if self.health <= 0:
            self.die()
        else:
            print(f"You have lost {value} health points and now have {self.health} left.")

    def die(self):
        print(f"You dead, bro.")

    def show_inventory(self):
        if self.items:
            items = ', '.join(self.items)
            print(f"Currently your inventory consists of the following items: {items}.")
        else:
            print(f"Your inventory is empty.")

    def show_items(self):
        self.show_inventory()

    def add_item(self, item: str):
        self.items.append(item)
        print(f"{item.capitalize()} has been added to your inventory.")

    def remove_item(self, item: str):
        if not self.items:
            print("Your inventory is empty.")
            return False
        elif item in self.items:
            self.items.remove(item)
            print(f"{item.capitalize()} has been removed from your inventory.")
            return True
        elif item not in self.items:
            print("You don't have it!")
            return False

    def change_stat(self, stat, value: int):
        self.stats[f'{stat}'] += value
        effect = "gained"
        if value < 0:
            effect = "lost"
        print(f"You have {effect} {value} {stat} points and now you have {self.stats[stat]}!")
