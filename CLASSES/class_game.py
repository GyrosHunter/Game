from CLASSES.class_ContentGenerator import ContentGenerator


class Game:
    generator = ContentGenerator()

    def __init__(self):
        self.current_location = None
        self.locations = None
        self.npcs = None
        self.items = None
        self.player = None
        self.structures = None

    def start_new_game(self):
        generator = ContentGenerator()
        self.locations, self.npcs, self.items, self.structures = generator.class_generator()
        self.player = generator.character_generator()
        self.current_location = self.locations["crossroads"]
        print('')
        return self.current_location.enter_message()

    def ask_for_action(self):
        print('')
        player_input = input(f"<What would you like to do now?> ").lower()
        words = [word for word in player_input.split(' ')]
        command, target = words[0], ' '.join(words[i] for i in range(1, len(words)))

        # Look around
        if player_input in ("look around", "la"):
            self.current_location.look_around()

        # Look at direction
        elif command in ("look", "l"):
            if target in self.current_location.all_directions:
                return self.current_location.look_direction(target)
            else:
                print("Where would you like to look?")

        # Exit location
        elif player_input in self.current_location.all_directions:
            if player_input in self.current_location.available_directions:
                self.change_current_location(player_input)
            else:
                print(self.current_location.directions[player_input])

        # PLAYER

        # Show player's statistics
        elif player_input == "stats":
            return self.player.show_stats()

        # Show player's skills
        elif player_input == "skills":
            return self.player.show_skills()

        # ITEMS

        # Show items in the location
        elif player_input in ("it", "items", "show items"):
            self.current_location.show_items()

        # Take item
        elif player_input in self.current_location.items:
            self.current_location.remove_item(player_input)
            self.player.add_item(player_input)

        # Discard item
        elif command in ("discard", "d") and target:
            if target not in self.player.items:
                return self.player.remove_item(target)
            self.player.remove_item(target)
            self.current_location.add_item(target)

        # Show inventory
        elif player_input in ("inventory", "i", "in", "inv"):
            self.player.show_items()

        # Show item or structure description and stats
        elif command in ("show", "s"):
            if target in self.player.items or target in self.current_location.items:
                return self.items[target].show_self(), self.items[target].show_stats()
            elif target in self.current_location.structures:
                return self.structures[target].show_self()
            else:
                print("There is no such thing here!")

        # STRUCTURES

        # Show structures in the location
        elif player_input in ("str", "structures", "show structures"):
            self.current_location.show_structures()

        # PEOPLE

        # Show people
        elif player_input in ("people", "show people", "npcs", "npcs", "p"):
            self.current_location.show_people()

    def change_current_location(self, direction: str):
        new_location = self.current_location.exit(direction)
        self.current_location = self.locations[new_location]
        return self.current_location.enter_message()

    # def end_game(self):
    #     print("You have quit the game!")
    #     return False
