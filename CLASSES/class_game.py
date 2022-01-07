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
        self.current_location = self.locations["crossroads"]

    def start_game(self):
        return self.current_location.enter()

    def ask_for_action(self):
        player_input = input("What would you like to do now: ").lower()
        words = [word for word in player_input.split(' ')]
        words = [words[0], ' '.join(words[i] for i in range(1, len(words)))]

        # Take a look-around
        if player_input == "look around":
            self.current_location.look_around()

        # Show items
        elif player_input in ("items", "show items"):
            self.current_location.show_items()

        # Take item
        elif player_input in self.current_location.items:
            self.current_location.remove_item(player_input)
            self.player.add_item(player_input)

        # Discard item
        elif words[0] in ("discard", "d") and words[1]:
            if words[1] not in self.player.items:
                return self.player.remove_item(words[1])
            self.player.remove_item(words[1])
            self.current_location.add_item(words[1])

        # Show inventory
        elif player_input in ("inventory", "i", "in" "inv"):
            self.player.show_items()

        # Show item
        elif words[0] in ("show", "s"):
            if words[1] in self.player.items:
                return self.items[f"{words[1]}"].show_self()
            else:
                print("There is no such item here!")

        # Show people
        elif player_input in ("people", "show people", "npcs", "npcs"):
            self.current_location.show_people()

        # Exit location
        elif player_input in self.all_directions:
            if player_input in self.current_location.available_directions:
                self.change_current_location(player_input)
            else:
                self.current_location.exit(player_input)

        # Exit game
        # elif player_input in self.exit_commands:
        #     self.end_game()

    def change_current_location(self, direction: str):
        new_location = self.current_location.exit(direction)
        self.current_location = self.locations[new_location]

    # def end_game(self):
    #     print("You have quit the game!")
    #     return False
