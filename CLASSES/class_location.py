class Location:
    all_directions = ("east", "west", "south", "north")

    def __init__(self, features: dict):

        self.features = features
        self.name = self.features["name"]
        self.coordinates = self.features["coordinates"]
        self.name_reference = self.features["name_reference"]

        self.available_directions = []
        for direction in self.all_directions:
            if self.features[f"{direction}_exit_location"]:
                self.available_directions.append(direction)

        if self.features["items"]:
            self.items = [item.replace('_', ' ') for item in self.features["items"].split(' ')]
        else:
            self.items = []

        if self.features["people"]:
            self.people = [person.replace('_', ' ') for person in self.features["people"].split(' ')]
        else:
            self.people = []

        if self.features["structures"]:
            self.structures = [structure.replace('_', ' ') for structure in self.features["structures"].split(' ')]
        else:
            self.structures = []

        self.exit_locations = {}
        for direction in self.available_directions:
            self.exit_locations[direction] = self.features[f"{direction}_exit_location"].replace('_', ' ')

    def __repr__(self):
        return self.name

    def enter(self):
        print(f"{self.features['enter']}")

    def show_available_directions(self):
        directions = ', '.join(self.available_directions)
        print(f"You can travel in the following directions: {directions}.")

    def get_available_directions(self):
        return self.available_directions

    def look_around(self):
        print(f"{self.features['description']}")

    def show_items(self):
        if self.items:
            items = ', '.join(self.items)
            print(f"After a quick look-around you notice the following objects available in this location: {items}.")
        else:
            print("No items can be found here.")

    def get_items(self):
        return self.items

    def add_item(self, item: str):
        self.items.append(item)

    def remove_item(self, item: str):
        if item in self.items:
            self.items.remove(item)
        else:
            print("There is no such item here.")

    def show_people(self):
        if self.people:
            people = ', '.join(self.people)
            print(f"The following people are present {self.name_reference}: {people}.")
        else:
            print("The is no one here.")

    def get_people(self):
        return self.people

    def add_person(self, person: str):
        self.people.append(person)

    def remove_person(self, person: str):
        if person in self.people:
            self.people.remove(person)
        else:
            print("There is no such person here.")

    def show_structures(self):
        if self.structures:
            structures = ', '.join(self.structures)
            print(f"You see: {structures}.")
        else:
            print("The is absolutely nothing here.")

    def get_structures(self):
        return self.structures

    def add_structure(self, structure: str):
        self.structures.append(structure)

    def remove_structure(self, structure: str):
        if structure in self.structures:
            self.structures.remove(structure)

    def exit(self, direction: str) -> str:
        if self.features[f"{direction}_exit_location"]:
            print(f"You are leaving {self.name} and now {self.features[direction]}")
            return self.exit_locations[direction]
        print(f"{self.features[direction]}")
