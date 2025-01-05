import unittest
import MySQLdb
from io import StringIO
from console import HBNBCommand
import sys


class TestStateCommand(unittest.TestCase):

    def setUp(self):
        # Set up a MySQL connection
        self.conn = MySQLdb.connect(
            user="hbnb_test", passwd="hbnb_test_pwd", db="hbnb_test_db"
        )
        self.cursor = self.conn.cursor()
        self.initial_count = self._get_states_count()

    def tearDown(self):
        # Clean up
        self.cursor.close()
        self.conn.close()

    def _get_states_count(self):
        self.cursor.execute("SELECT COUNT(*) FROM states")
        return self.cursor.fetchone()[0]

    def test_create_state(self):
        # Run the command to create a new state
        command = 'create State name="California"'
        sys.stdin = StringIO(command)
        HBNBCommand().onecmd(command)

        # Check if the state was added
        self.conn.commit()
        self.assertEqual(self._get_states_count(), self.initial_count + 1)


if __name__ == "__main__":
    unittest.main()
