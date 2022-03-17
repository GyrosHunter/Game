
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
        return self.enter

    def show_available_directions(self):
        directions = ', '.join(self.available_directions)
        return f"You can travel in the following directions: {directions}."

    def look_around(self):
        return self.description

    def look_direction(self, direction: str):
        return self.directions[direction]

    def show_items(self):
        if self.items:
            return f"Items {self.name_reference}:"
        else:
            return f"No items available {self.name_reference}"

    def add_item(self, item: str):
        self.items.append(item)

    def remove_item(self, item: str):
        if item in self.items:
            self.items.remove(item)
        else:
            return "There is no such item here."

    def show_people(self):
        if self.people:
            return f"People {self.name_reference}:"
        else:
            return "There is no one here!"

    def add_person(self, person: str):
        self.people.append(person)

    def remove_person(self, person: str):
        if person in self.people:
            self.people.remove(person)
        else:
            print("There is no such person here.")

    def show_venues(self):
        if self.venues:
            return f"Venues {self.name_reference}:"
        else:
            return "There are no venues here."

    def add_venue(self, venue: str):
        self.venues.append(venue)

    def remove_venue(self, venue: str):
        if venue in self.venues:
            self.venues.remove(venue)

    def exit(self, direction: str) -> str:
        return self.exit_locations[direction]
