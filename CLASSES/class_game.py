from CLASSES.class_ContentGenerator import ContentGenerator


class Game:
    generator = ContentGenerator()

    def __init__(self):
        self.current_location = None
        self.locations = None
        self.npcs = None
        self.items = None
        self.player = None
        self.venues = None
        self.game_run = None
        self.player_input = None
        self.player_command = None
        self.player_target = None

    def game_intro(self):
        print('')
        print("Welcome to the Game!")
        self.start_menu()

    def start_menu(self):
        print('')
        print("Start New Game (press 1)")
        print("Load Game      (press 2)")
        print("Quit game      (press 3)")
        print('')
        self.game_run = "1"  # input("What is you choice: ")
        if self.game_run == "1":
            self.new_game()
        elif self.game_run == "2":
            self.load_game()
        elif self.game_run == "3":
            self.quit_game()
        else:
            print("Choose one of the given options!")
            self.start_menu()

    def new_game(self):
        generator = ContentGenerator()
        self.locations, self.npcs, self.items, self.venues, self.player = generator.class_generator_new(
            source='TEXT')
        self.current_location = self.locations["crossroads"]
        print('')
        print("INTRO TEXT")
        print('')
        self.current_location.enter_message()
        self.run_game()

    def load_game(self):
        self.new_game()
        pass

    def run_game(self):
        while self.game_run:
            self.get_player_input()

            if self.player_input in ("q", "quit", "exit"):
                self.quit_game()

            elif self.player_input in ("look around", "look a", "la"):
                self.current_location.look_around()

            elif self.player_command in ["look"[:i] for i in range(len("look")+1)]:
                self.look_at_direction()

            elif self.player_input in self.current_location.all_directions:
                self.exit_location()

            # PLAYER

            elif self.player_input in ["stats"[:i] for i in range(2, len("items") + 1)]:
                return self.player.show_stats()

            elif self.player_input in ["skills"[:i] for i in range(2, len("items") + 1)]:
                return self.player.show_skills()

            # ITEMS

            elif self.player_input in ["items"[:i] for i in range(1, len("items") + 1)]:
                self.show_items()

            elif self.player_input in self.current_location.items:
                self.current_location.remove_item(self.player_input)
                self.player.add_item(self.player_input)

            elif self.player_command in ("discard", "d") and self.player_target:
                self.discard_item()

            elif self.player_input in ["inventory"[:i] for i in range(len("inventory") + 1)]:
                self.player.show_inventory()

            elif self.player_command in ["show"[:i] for i in range(len("show") + 1)]:
                self.show_stats()

            # VENUES

            elif self.player_input in ["venues"[:i] for i in range(1, len("venues") + 1)]:
                self.current_location.show_venues()

            # PEOPLE

            elif self.player_input in ("people", "show people", "npcs", "npcs", "p"):
                self.current_location.show_people()

            else:
                print("Come again?")

    def get_player_input(self):
        print('')
        self.player_input = input(f"<What would you like to do now?> ").lower()
        words = [word for word in self.player_input.split(' ')]
        self.player_command, self.player_target = words[0], ' '.join(words[i] for i in range(1, len(words)))

    def quit_game(self):
        print('')
        print('Thanks for playing. See you next time!')
        print('')
        self.game_run = False

    def look_at_direction(self):
        if self.player_target in self.current_location.all_directions:
            return self.current_location.look_direction(self.player_target)
        else:
            print("Where would you like to look?")

    def exit_location(self):
        if self.player_input in self.current_location.available_directions:
            self.change_current_location(self.player_input)
        else:
            print(self.current_location.directions[self.player_input])

    def change_current_location(self, direction: str):
        new_location = self.current_location.exit(direction)
        self.current_location = self.locations[new_location]
        return self.current_location.enter_message()

    def discard_item(self):
        if self.player_target not in self.player.items:
            return self.player.remove_item(self.player_target)
        self.player.remove_item(self.player_target)
        self.current_location.add_item(self.player_target)

    def show_stats(self):
        if self.player_target in self.player.items or self.player_target in self.current_location.items:
            return self.items[self.player_target].show_self(), self.items[self.player_target].show_stats()
        elif self.player_target in self.current_location.venues:
            return self.venues[self.player_target].show_self()
        else:
            print("There is no such thing here!")

    def show_items(self):
        if self.current_location.items:
            self.current_location.show_items()
        else:
            print("There are no items here!")
