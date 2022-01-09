from CLASSES.class_game import Game

game = Game()
game.start_new_game()

run = True
while run:
    game.ask_for_action()
