class Structure:

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
