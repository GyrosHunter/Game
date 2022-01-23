from CLASSES.class_location import Location


class Venue(Location):

    def __init__(self, features: dict):
        super().__init__(features)

        self.use = features["use"]

    def use_venue(self):
        print(self.use)

    def enter_venue(self):
        print(self.enter)

    def exit_venue(self):
        print(f"You've exited the {self.name}.")
