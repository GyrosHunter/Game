from CLASSES.class_game import Game

game = Game()
game.start_game()

run = True
while run:
    game.ask_for_action()
