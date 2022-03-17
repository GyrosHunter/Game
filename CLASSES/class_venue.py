from CLASSES.class_location import Location


class Venue(Location):

    def __init__(self, features: dict):
        super().__init__(features)

        self.use = features["use"]

    def show_self(self):
        return self.description

    def use_venue(self):
        return self.use

    def enter_venue(self):
        return self.enter

    def exit_venue(self):
        return f"You've exited the {self.name}."
