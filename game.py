from class_location import Location
from class_person import Person
from class_character import Character

crossroads = Location("crossroads")
John_Wayne = Person("John Wayne")

Bad_Motherfucker = Character("roamer", "Bad", "Motherfucker", 38)

print(Bad_Motherfucker)
Bad_Motherfucker.show_items()
Bad_Motherfucker.remove_item("blade")
Bad_Motherfucker.show_items()
