from class_location import Location
import unittest


class LocationTests(unittest.TestCase):

    def setUp(self):
        self.location = Location("B4", "TestLocation")

    def test_location(self):
        self.assertEqual(self.location.coordinates, "B4")
        self.assertEqual(self.location.name, "TestLocation")

    def test_repr(self):
        self.assertEqual(repr(self.location), "You are at the TestLocation.")

    def test_enter(self):
        self.assertEqual(self.location.enter(), "Test, you are entering TestLocation.")

    def test_exit(self):
        self.assertEqual(self.location.exit("north"),
                         "You are leaving TestLocation and now Test, you are going north.")
        self.assertEqual(self.location.exit("south"), "You can't go there.")

    def test_look_around(self):
        self.assertEqual(self.location.look_around(), "Test, you are taking a quick look-around.")

    def test_show_items(self):
        self.assertEqual(self.location.show_items(), "After a quick look-around you notice the following objects "
                                                     "available in this location: item1, item2, item3, item4.")

    def test_show_people(self):
        self.assertEqual(self.location.show_people(),
                         "The following people are present here: person1, person2, person3.")

    def test_show_directions(self):
        self.assertEqual(self.location.show_directions(),
                         "You can travel in the following directions: east, west, north.")

    def test_remove_item(self):
        self.assertEqual(self.location.remove_item("jack"), "There is no such item here.")
        self.assertEqual(self.location.remove_item("item4"), None)

    def test_remove_person(self):
        self.assertEqual(self.location.remove_person("jack"), "There is no such person here.")
        self.assertEqual(self.location.remove_person("person1"), "Person1 is no longer here.")


if __name__ == "__main__":
    unittest.main()
