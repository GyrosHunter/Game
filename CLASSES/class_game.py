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
        print("Start New Game           (press 1)")
        print("Continue Previous Game   (press 2)")
        print("Load Game                (press 3)")
        print("Quit game                (press q)")
        print('')
        self.game_run = input("What is your choice: ")
        if self.game_run in ("1", "new", "Start New Game"):
            self.new_game()
        elif self.game_run in ("2", "continue", "Continue Previous Game"):
            self.continue_previous_game()
        elif self.game_run in ("3", "load", "Load Game"):
            self.load_game()
        elif self.game_run in ("q", "quit", "exit", "Quit Game"):
            self.exit_game()
        else:
            print("Choose one of the given options!")
            self.start_menu()

    def start_menu_flask(self, command):
        if command in ("1", "new", "Start New Game"):
            self.new_game()
        elif command in ("2", "continue", "Continue Previous Game"):
            self.continue_previous_game()
        elif command in ("3", "load", "Load Game"):
            self.load_game()
        elif command in ("q", "quit", "exit", "Quit Game"):
            self.exit_game()

    def new_game(self):
        generator = ContentGenerator()
        self.locations, self.npcs, self.items, self.venues, self.player = generator.class_generator_new(
            source='TEXT')
        self.current_location = self.locations["crossroads"]
        print('')
        print("The search of the missing whore begins here...")
        print('')
        self.current_location.enter_message()
        self.run_game()

    def auto_save(self):
        self.save_file("auto_save")
        # print("Autosave complete.")

    def continue_previous_game(self):
        if os.path.isfile(f"SAVE/auto_save.pickle"):
            self.load_file("auto_save")
            print(f"{self.player.name}, your game has been loaded!")
            self.current_location.enter_message()
            self.run_game()
        else:
            print("There is no game to continue!\nYou should start a new one!")
            return self.start_menu()

    def save_game(self):
        save_name = input("Name your save file: ").lower()
        if os.path.isfile(f"SAVE/{save_name}.pickle"):
            decision = None
            while decision not in ("y", "n"):
                decision = input("Save already exists. Do you want to overwrite this file(y/n)? ")
            if decision == "y":
                self.save_file(save_name)
                print(f"Your game has been saved.")
            else:
                self.save_game()
        else:
            self.save_file(save_name)
            print(f"Your game has been saved at {save_name}.pickle.")

    def load_game(self):
        if len(os.listdir("SAVE")) == 0:
            print("The are no saved games!")
            if self.current_location:
                pass
            else:
                return self.start_menu()

        print("Here is the list of saved games:\n")
        for i, filename in enumerate(os.listdir("SAVE")):
            print(f"{i + 1}. {filename[:-7]}")
        print("")

        load_name = input("Which game would you like to load: ").lower()
        if os.path.isfile(f"SAVE/{load_name}.pickle") is False:
            print("File does not exist exist!")
            return self.start_menu()
        else:
            self.load_file(load_name)
            print(f"{self.player.name}, your game has been loaded!")
            self.current_location.enter_message()
            self.run_game()

    def save_file(self, filename: str):
        with open(f"SAVE/{filename}.pickle", "wb") as file:
            saved_game = self.locations, self.npcs, self.items, self.venues, self.player, self.current_location,\
                self.base_location
            pickle.dump(saved_game, file)

    def load_file(self, filename: str):
        with open(f"SAVE/{filename}.pickle", "rb") as file:
            loaded_game = pickle.load(file)
            self.locations, self.npcs, self.items, self.venues, self.player, self.current_location,\
                self.base_location = loaded_game

    def run_game(self):
        while self.game_run:
            self.auto_save()
            self.get_player_input()

            if self.player_input in ("q", "quit"):
                self.quit_to_start_menu()

            elif self.player_input == "save":
                self.save_game()

            elif self.player_input == "load":
                self.load_game()

            elif self.player_command == "info":
                self.info()

            elif self.player_command in ["look", "l"]:
                self.look_at()

            elif self.player_command in self.all_directions:
                self.exit_location()

            elif self.player_input in self.current_location.items:
                self.current_location.remove_item(self.player_input)
                return self.player.add_item(self.player_input)

            elif self.player_command in ["discard", "d"]:
                self.discard_item()

            elif self.player_command in ["show"]:
                self.show_stats()

            # VENUES

            elif self.player_command in ["venues"]:
                self.show_venues()

            elif self.player_input in self.current_location.venues:
                self.enter_venue()

            elif self.player_command == "exit":
                self.exit_venue()

            # PEOPLE

            elif self.player_command in ["people"]:
                self.show_people()

            else:
                print("Come again?")

    def get_player_input(self):
        print('')
        self.player_input = input(f"<What would you like to do now?> ").lower()
        print('')
        words = [word for word in self.player_input.split(' ')]
        self.player_command, self.player_target = words[0], ' '.join(words[i] for i in range(1, len(words)))

    def quit_to_start_menu(self):
        decision = input("Are you sure you want to quit the game(y/n): ")
        if decision in ("y", "q"):
            self.auto_save()
            return self.start_menu()
        elif decision == "n":
            pass
        else:
            return self.quit_to_start_menu()

    def exit_game(self):
        self.game_run = False
        print('')
        print('Thanks for playing. See you next time!')
        print('')

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
