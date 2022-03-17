import pickle
import os
from CLASSES.class_ContentGenerator import ContentGenerator


class Game:
    generator = ContentGenerator()
    all_directions = ("east", "west", "south", "north")

    def __init__(self):
        self.saved_games = None
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

    def new_game(self):
        generator = ContentGenerator()
        self.locations, self.npcs, self.items, self.venues, self.player = generator.class_generator_new(
            source='TEXT')
        self.current_location = self.locations["crossroads"]
        self.current_location.enter_message()

    def auto_save(self):
        self.save_file("auto_save")
        # print("Autosave complete.")

    def continue_previous_game(self):
        if os.path.isfile(f"SAVE/auto_save.pickle"):
            self.load_file("auto_save")
            return f"{self.player.name}, your game has been loaded!"
        else:
            return "There is no game to continue!"

    def show_saves(self):
        self.saved_games = [filename[:-7] for filename in os.listdir("SAVE")]
        return self.saved_games

    def save_file(self, filename: str):
        with open(f"SAVE/{filename}.pickle", "wb") as file:
            saved_game = self.locations, self.npcs, self.items, self.venues, self.player, self.current_location, \
                         self.base_location
            pickle.dump(saved_game, file)
            return f"{filename.title()} saved successfully."

    def load_file(self, filename: str):

        if filename == "auto_save" and os.path.isfile(f"SAVE/auto_save.pickle") is False:
            return "There no game to continue!"

        with open(f"SAVE/{filename}.pickle", "rb") as file:
            loaded_game = pickle.load(file)
            self.locations, self.npcs, self.items, self.venues, self.player, self.current_location, \
                self.base_location = loaded_game
            return f"{filename.title()} loaded successfully."

    def run_game(self, command):

        self.auto_save()
        self.get_player_input(command)

        if self.player_command in ["look"[:i] for i in range(len("look") + 1)]:
            return self.look_at()

        elif self.player_command in self.all_directions:
            return self.exit_location()

        # PLAYER

        elif self.player_command in ["stats"[:i] for i in range(2, len("items") + 1)]:
            return self.player.show_stats()

        elif self.player_command in ["skills"[:i] for i in range(2, len("items") + 1)]:
            return self.player.show_skills()

        # ITEMS

        elif self.player_input in self.current_location.items:
            self.current_location.remove_item(self.player_input)
            return self.player.add_item(self.player_input)

        elif self.player_command in ["discard"[:i] for i in range(len("discard") + 1)]:
            return self.discard_item()

        # VENUES

        elif self.player_command in ["venues"[:i] for i in range(1, len("venues") + 1)]:
            return self.current_location.show_venues()

        elif self.player_input in self.current_location.venues:
            self.enter_venue()

        elif self.player_command == "exit":
            self.exit_venue()

        # PEOPLE

        elif self.player_command in ["people"[:i] for i in range(len("people") + 1)]:
            return self.current_location.show_people()

        else:
            return "Come again?"

    def get_player_input(self, command):
        self.player_input = command.lower()
        words = [word for word in self.player_input.split(' ')]
        self.player_command, self.player_target = words[0], ' '.join(words[i] for i in range(1, len(words)))

    def exit_game(self):
        self.game_run = False

    def look_at(self):
        if self.player_target in self.all_directions:
            return self.current_location.look_direction(self.player_target)
        elif self.player_target in ["around"[:i] for i in range(len("around") + 1)]:
            return self.current_location.look_around()
        else:
            return "Where would you like to look?"

    def exit_location(self):
        if self.current_location.available_directions:
            if self.player_command in self.current_location.available_directions:
                return self.change_current_location(self.player_command)
            else:
                return self.current_location.directions[self.player_command]
        else:
            return self.base_location.directions[self.player_command]

    def change_current_location(self, direction: str):
        new_location = self.current_location.exit(direction)
        self.current_location = self.locations[new_location]
        return f"You decided to go {direction}."

    def discard_item(self):
        if self.player_target not in self.player.items:
            return self.player.remove_item(self.player_target)
        self.current_location.add_item(self.player_target)
        return self.player.remove_item(self.player_target)

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
