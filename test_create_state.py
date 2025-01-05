import unittest
from models.state import State
from models import storage


class TestState(unittest.TestCase):
    """ Test class for State class """

    def test_instance(self):
        """ Test if an instance of State is created correctly """
        state = State()
        self.assertIsInstance(state, State)

    def test_name(self):
        """ Test the name attribute of State """
        state = State()
        self.assertTrue(hasattr(state, "name"))
        state.name = "California"
        self.assertEqual(state.name, "California")

    def test_save(self):
        """ Test if the save method works correctly """
        state = State()
        state.name = "California"
        state.save()
        state_dict = storage.all()
        self.assertIn(f"State.{state.id}", state_dict)

    def test_delete(self):
        """ Test if the delete method works correctly """
        state = State()
        state.name = "California"
        state.save()
        state_id = state.id
        state.delete()
        state_dict = storage.all()
        self.assertNotIn(f"State.{state_id}", state_dict)

    def test_reload(self):
        """ Test if the reload method loads the saved object correctly """
        state = State()
        state.name = "California"
        state.save()
        storage.reload()
        state_dict = storage.all()
        self.assertIn(f"State.{state.id}", state_dict)

    def test_create_state(self):
        """ Test creating a new State object and saving it """
        state = State(name="California")
        state.save()
        state_dict = storage.all()
        self.assertIn(f"State.{state.id}", state_dict)
        self.assertEqual(state_dict[f"State.{state.id}"].name, "California")

    def test_invalid_create_state(self):
        """ Test creating a new State object with invalid data """
        state = State(name="California")
        state.save()
        state_dict = storage.all()
        self.assertNotEqual(state_dict[f"State.{state.id}"].name, "Texas")

    def test_get_state_count(self):
        """ Test getting the count of states in the storage """
        initial_count = len(storage.all())
        state = State(name="California")
        state.save()
        new_count = len(storage.all())
        self.assertEqual(new_count, initial_count + 1)

    def test_state_instance(self):
        """ Test creating multiple states and checking their types """
        state1 = State(name="California")
        state2 = State(name="Texas")
        state1.save()
        state2.save()
        state_dict = storage.all()
        self.assertIsInstance(state1, State)
        self.assertIsInstance(state2, State)
        self.assertIn(f"State.{state1.id}", state_dict)
        self.assertIn(f"State.{state2.id}", state_dict)
