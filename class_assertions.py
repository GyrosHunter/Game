from class_location import Location
import unittest


class LocationTests(unittest.TestCase):

    def setUp(self):
        self.location = Location("TestLocation")

    def test_location(self):
        self.assertEqual(self.location.coordinates, "A0")
        self.assertEqual(self.location.name, "TestLocation")

    def test_repr(self):
        self.assertEqual(repr(self.location), "You are at the TestLocation.")

    def test_enter(self):
        self.assertEqual(self.location.enter(), None)

    def test_show_available_directions(self):
        self.assertEqual(self.location.show_available_directions(), None)

    def test_look_around(self):
        self.assertEqual(self.location.look_around(), None)

    def test_show_items(self):
        self.assertEqual(self.location.show_items(), None)

    def test_show_people(self):
        self.assertEqual(self.location.show_people(),None)

    def test_show_structures(self):
        self.assertEqual(self.location.show_structures(),None)

    def test_exit(self):
        self.assertEqual(self.location.exit("north"), "north test location")
        self.assertEqual(self.location.exit("south"), None)

    def test_remove_item(self):
        self.assertEqual(self.location.remove_item("jack"), None)
        self.assertEqual(self.location.remove_item("item4"), None)

    def test_remove_person(self):
        self.assertEqual(self.location.remove_person("jack"), None)
        self.assertEqual(self.location.remove_person("person1"), None)

    def test_remove_structure(self):
        self.assertEqual(self.location.remove_structure("jack"), None)
        self.assertEqual(self.location.remove_structure("Test structure 1"), None)


if __name__ == "__main__":
    unittest.main()
