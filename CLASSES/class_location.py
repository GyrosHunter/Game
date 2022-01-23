from utils import print_slow


class Location:

    def __init__(self, features: dict):
        self.name = features["name"]
        self.coordinates = features["coordinates"]
        self.name_reference = features["name_reference"]

        self.enter = features["enter"]
        self.description = features["description"]

        if "directions" in features:
            self.directions = features["directions"]
        if "available_directions" in features:
            self.available_directions = features["available_directions"]
        if "exit_locations" in features:
            self.exit_locations = features["exit_locations"]

        self.items = features["items"]
        self.people = features["people"]
        self.venues = features["venues"]

    def __repr__(self):
        return self.name

    def enter_message(self):
        print_slow(self.enter)

    def show_available_directions(self):
        directions = ', '.join(self.available_directions)
        print_slow(f"You can travel in the following directions: {directions}.")

    def look_around(self):
        print_slow(self.description)

    def look_direction(self, direction: str):
        print(self.directions[direction])

    def show_items(self):
        items = ', '.join(self.items)
        print(f"Items available {self.name_reference}: {items}.")

    def add_item(self, item: str):
        self.items.append(item)

    def remove_item(self, item: str):
        if item in self.items:
            self.items.remove(item)
        else:
            print("There is no such item here.")

    def show_people(self):
        people = ', '.join(self.people)
        print(f"The following people are present {self.name_reference}: {people}.")

    def add_person(self, person: str):
        self.people.append(person)

    def remove_person(self, person: str):
        if person in self.people:
            self.people.remove(person)
        else:
            print("There is no such person here.")

    def show_venues(self):
        venues = ', '.join(self.venues)
        print(f"Venues available in this location: {venues}.")

    def add_venue(self, venue: str):
        self.venues.append(venue)

    def remove_venue(self, venue: str):
        if venue in self.venues:
            self.venues.remove(venue)

    def exit(self, direction: str) -> str:
        print(f"You decided to go {direction}...")
        return self.exit_locations[direction]
