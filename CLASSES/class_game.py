import pickle
import os
from CLASSES.class_ContentGenerator import ContentGenerator


class Game:
    generator = ContentGenerator()
    all_directions = ("east", "west", "south", "north")

    def __init__(self):
        self.current_location = None
        self.base_location = None
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
        self.game_run = input("What is your choice: ")
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

    def save_game(self):
        save_name = input("Name your save file: ").lower()
        if os.path.isfile(f"SAVE/{save_name}.pickle"):
            decision = None
            while decision not in ("y", "n"):
                decision = input("Save already exists. Do you want to overwrite this file(y/n)? ")
            if decision == "y":
                with open(f"SAVE/{save_name}.pickle", "wb") as file:
                    save_game = (self.player, self.locations, self.items, self.npcs, self.venues, self.current_location)
                    pickle.dump(save_game, file)
                    print(f"Your game has been saved.")
            else:
                self.save_game()
        else:
            with open(f"SAVE/{save_name}.pickle", "wb") as file:
                save_game = (self.player, self.locations, self.items, self.npcs, self.venues, self.current_location)
                pickle.dump(save_game, file)
                print(f"Your game has been saved at {save_name}.pickle.")

    def load_game(self):
        if len(os.listdir("SAVE")) == 0:
            print("The are no saved games!")
            return self.start_menu()
        print("Here is the list of saved games:\n")
        for i, filename in enumerate(os.listdir("SAVE")):
            print(f"{i + 1}. {filename[:-7]}")
        print("")
        load_name = input("Which game would you like to load: ").lower()
        if os.path.isfile(f"SAVE/{load_name}.pickle") is False:
            print("File does not exist exist!")
        else:
            with open(f"SAVE/{load_name}.pickle", "rb") as file:
                save_game = pickle.load(file)
                self.player, self.locations, self.items, self.npcs, self.venues, self.current_location = save_game

            print(f"{self.player.name}, your game has been loaded!\n")
            self.current_location.enter_message()
            self.run_game()

    def run_game(self):
        while self.game_run:
            self.get_player_input()

            if self.player_input in ("q", "quit"):
                self.quit_game()

            elif self.player_input == "save":
                self.save_game()

            elif self.player_input == "load":
                self.load_game()

            elif self.player_command == "info":
                self.info()

            elif self.player_command in ["look"[:i] for i in range(len("look") + 1)]:
                self.look_at()

            elif self.player_command in self.all_directions:
                self.exit_location()

            # PLAYER

            elif self.player_command in ["stats"[:i] for i in range(2, len("items") + 1)]:
                return self.player.show_stats()

            elif self.player_command in ["skills"[:i] for i in range(2, len("items") + 1)]:
                return self.player.show_skills()

            # ITEMS

            elif self.player_command in ["items"[:i] for i in range(1, len("items") + 1)]:
                self.show_items()

            elif self.player_input in self.current_location.items:
                self.current_location.remove_item(self.player_input)
                self.player.add_item(self.player_input)

            elif self.player_command in ["discard"[:i] for i in range(len("discard") + 1)]:
                self.discard_item()

            elif self.player_command in ["inventory"[:i] for i in range(len("inventory") + 1)]:
                self.player.show_inventory()

            elif self.player_command in ["show"[:i] for i in range(len("show") + 1)]:
                self.show_stats()

            # VENUES

            elif self.player_command in ["venues"[:i] for i in range(1, len("venues") + 1)]:
                self.show_venues()

            elif self.player_input in self.current_location.venues:
                self.enter_venue()

            elif self.player_command == "exit":
                self.exit_venue()

            # PEOPLE

            elif self.player_command in ["people"[:i] for i in range(len("people") + 1)]:
                self.show_people()

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

    def info(self):
        print(f"You are {self.current_location.name_reference}.")

    def look_at(self):
        if self.player_target in self.all_directions:
            return self.current_location.look_direction(self.player_target)
        elif self.player_target in ["around"[:i] for i in range(len("around") + 1)]:
            return self.current_location.look_around()
        else:
            print("Where would you like to look?")

    def exit_location(self):
        if self.current_location.available_directions:
            if self.player_command in self.current_location.available_directions:
                self.change_current_location(self.player_command)
            else:
                print(self.current_location.directions[self.player_command])
        else:
            print(self.base_location.directions[self.player_command])

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

    def show_people(self):
        if self.current_location.people:
            self.current_location.show_people()
        else:
            print("There is no one here!")

    def show_venues(self):
        if self.current_location.venues:
            self.current_location.show_venues()
        else:
            print("Sorry, nothing interesting here.")

    def enter_venue(self):
        if self.player_input in self.current_location.venues:
            self.base_location = self.current_location
            self.current_location = self.venues[self.player_input]
            self.current_location.enter_venue()
        else:
            print("What would you like to enter?")

    def exit_venue(self):
        self.current_location.exit_venue()
        self.current_location = self.base_location
