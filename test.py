from CLASSES.class_location import Location
from CLASSES.class_player import Player
from CLASSES.class_NPC import NPC
from CLASSES.class_item import Item

crossroads = Location("crossroads")
Old_Beggar = NPC("Old Beggar")
Bad_Motherfucker = Player("roamer", "Bad", "Motherfucker", 38)
blade = Item("blade")

print(crossroads)
print(Old_Beggar)
print(Bad_Motherfucker)
blade.show_stats()
