from CLASSES.class_ContentGenerator import ContentGenerator


class Game:
    generator = ContentGenerator()

    all_directions = ("east", "west", "south", "north")
    exit_commands = ("q", "quit", "exit")

    def __init__(self):
        self.current_location = None
        generator = ContentGenerator()
        self.locations, self.npcs, self.items = generator.class_generator()
        self.player = generator.character_generator()

    def first_run(self):
        self.current_location = self.locations["crossroads"]
        self.current_location.items = self.current_location.get_items()
        self.current_location.people = self.current_location.get_people()
        self.current_location.structures = self.current_location.get_structures()
        self.current_location.available_directions = self.current_location.get_available_directions()
        return self.current_location.enter()

    def ask_for_action(self):
        player_input = input("What would you like to do now: ")

        if player_input == "look around":
            self.current_location.look_around()

        elif player_input in self.exit_commands:
            self.end_game()

        elif player_input in self.all_directions:
            if player_input in self.current_location.available_directions:
                self.change_current_location(player_input)
            else:
                self.current_location.exit(player_input)

    def change_current_location(self, direction: str):
        new_location = self.current_location.exit(direction)
        self.current_location = self.locations[new_location]

    def end_game(self):
        pass
