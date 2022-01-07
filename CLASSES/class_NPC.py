from CLASSES.class_person import Person


class NPC(Person):
    def __init__(self, features):
        super().__init__(features)

        self.features = features
        self.chat = self.features["talk"]

    def sell_item(self, item: str):
        if item in self.items:
            self.remove_item(item)
            print("Here you are, kind sir!")
            print(f"{self.full_name} hands you over the {item}.")
        else:
            print(f"I have no such thing for sale!")

    def talk(self):
        print(self.chat)
