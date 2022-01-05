from CLASSES.class_ContentGenerator import ContentGenerator


class Item:
    _Generator = ContentGenerator()
    max_durability = 100
    base_stats = ("attack", "defense", "intelligence", "health", "durability", "weight")

    def __init__(self, name):

        self.features = self._Generator.generate_from_txt(name)
        self.name = name
        self.description = self.features['description']

        if self.features["stats"]:
            item_stats = [stat for stat in self.features["stats"].split(' ')]
            self.stats = {self.base_stats[i]: int(item_stats[i]) for i in range(0, len(self.base_stats))}
        else:
            self.stats = dict.fromkeys(self.base_stats, "N/A")

    def __repr__(self):
        return self.description

    def show_stats(self):
        print(f"Here are the stat modifiers of {self.name}:")
        print(f"Attack:       {self.stats['attack']}")
        print(f"Defense:      {self.stats['defense']}")
        print(f"Intelligence: {self.stats['intelligence']}")
        print(f"Health:       {self.stats['health']}")
        print(f"Durability:   {self.stats['durability']}")
        print(f"Weight:       {self.stats['weight']}")
