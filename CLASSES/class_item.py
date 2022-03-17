class Item:
    max_durability = 100

    def __init__(self, features: dict):

        self.name = features["name"]
        self.description = features["description"]
        self.stats = features["stats"]

    def __repr__(self):
        return self.name

    def show_stats(self):
        print(f"Here are the stats of {self.name}:\n")
        print(f"Attack:       {self.stats['attack']}")
        print(f"Defense:      {self.stats['defense']}")
        print(f"Intelligence: {self.stats['intelligence']}")
        print(f"Health:       {self.stats['health']}")
        print(f"Durability:   {self.stats['durability']}")
        print(f"Weight:       {self.stats['weight']}")

    def show_self(self):
        return self.description

    def destroy_self(self):
        print(f"{self.name} has been destroyed.")
