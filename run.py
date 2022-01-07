from CLASSES.class_game import Game

game = Game()
game.first_run()

run = True
while run:
    game.ask_for_action()
