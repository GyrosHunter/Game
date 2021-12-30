import csv


class Location:
    all_directions = ("east", "west", "south", "north")

    def __init__(self, coordinates, name):
        self.coordinates = coordinates
        self.name = name
        self.actions = {}
        with open(f"./TXT/{self.name}.txt", 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                if row:
                    decision, action = row
                    self.actions[decision] = action

        if self.actions["items"]:
            self.items = [item.replace('_', ' ') for item in self.actions["items"].split(' ')]
        else:
            self.items = []

        if self.actions["people"]:
            self.people = [person.replace('_', ' ') for person in self.actions["people"].split(' ')]
        else:
            self.people = []

        self.directions = []
        for direction in self.all_directions:
            if self.actions[direction]:
                self.directions.append(direction)

    def __repr__(self):
        return f"You are at the {self.name}."

    def enter(self):
        return f"{self.actions['enter']}"

    def exit(self, direction):
        if self.actions[direction]:
            return f"You are leaving {self.name} and now {self.actions[direction]}"
        return "You can't go there."

    def look_around(self):
        return f"{self.actions['look_around']}"

    def show_items(self):
        if self.items:
            items = ', '.join(self.items)
            return f"After a quick look-around you notice the following objects available in this location: {items}."
        return "No items can be found here."

    def show_people(self):
        if self.people:
            people = ', '.join(self.people)
            return f"The following people are present here: {people}."
        return "The is no one here."

    def show_directions(self):
        directions = ', '.join(self.directions)
        return f"You can travel in the following directions: {directions}."

    def remove_item(self, item):
        if item in self.items:
            self.items.remove(item)
        else:
            return "There is no such item here."

    def remove_person(self, person):
        if person in self.people:
            self.people.remove(person)
            return f"{person.title()} is no longer here."
        return "There is no such person here."

    @property
    def return_items(self):
        return self.items

    @property
    def return_people(self):
        return self.people

    @property
    def return_directions(self):
        return self.directions


crossroads = Location("B4", "crossroads")

# Test remove item

# print(crossroads.return_items)
# print(crossroads.remove_item("john"))
# print(crossroads.return_items)
#
# # Test remove person
#
# print(crossroads.return_people)
# print((crossroads.remove_person("John Doe")))
# print(crossroads.return_people)

# print(crossroads.show_items())
# print(crossroads.show_people())
# print(crossroads.remove_person("Jack Daniels"))
# print(crossroads.show_people())
# print(crossroads.remove_person("John Doe"))
# print(crossroads.show_people())
# print(crossroads.show_directions())

# print(crossroads.return_items)
# print(crossroads.return_people)
# print(crossroads.return_directions)
