class Location:
    all_directions = ("east", "west", "south", "north")

    def __init__(self, features: dict):

        self.name = features["name"]
        self.coordinates = features["coordinates"]
        self.name_reference = features["name_reference"]

        self.enter = features["enter"]
        self.description = features["description"]
        self.directions = features["directions"]
        self.available_directions = features["available_directions"]
        self.exit_locations = features["exit_locations"]
        self.items = features["items"]
        self.people = features["people"]
        self.structures = features["structures"]

    def __repr__(self):
        return self.name

    def enter_message(self):
        print(self.enter)

    def show_available_directions(self):
        directions = ', '.join(self.available_directions)
        print(f"You can travel in the following directions: {directions}.")

    def get_available_directions(self):
        return self.available_directions

    def look_around(self):
        print(self.description)

    def look_direction(self, direction: str):
        if self.directions[direction]:
            print(self.directions[direction])
        else:
            print("Nothing to see there...")

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
            print(f"Structures in this location: {structures}.")
        else:
            print("Well, no structures here.")

    def get_structures(self):
        return self.structures

    def add_structure(self, structure: str):
        self.structures.append(structure)

    def remove_structure(self, structure: str):
        if structure in self.structures:
            self.structures.remove(structure)

    def exit(self, direction: str) -> str:
        print(f"You decided to go {direction}...")
        return self.exit_locations[direction]
