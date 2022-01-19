class Venue:

    def __init__(self, features: dict):

        self.name = features["name"]
        self.description = features["description"]
        self.use = features["use"]

    def __repr__(self):
        return self.name

    def show_self(self):
        print(self.description)

    def use_self(self):
        print(self.use)

    def enter_self(self):
        print(f"You have entered the {self.name}")

    def exit_self(self):
        print(f"You've exited the {self.name}")
