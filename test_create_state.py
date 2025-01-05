import unittest
import MySQLdb
from io import StringIO
import sys
from your_console_module import HBNBCommand  # Adjust this import to your console module

class TestMySQL(unittest.TestCase):

    def setUp(self):
        """Set up MySQL connection for the tests."""
        self.db = MySQLdb.connect(
            user="hbnb_test", 
            passwd="hbnb_test_pwd", 
            db="hbnb_test_db", 
            host="localhost"
        )
        self.cursor = self.db.cursor()

    def test_create_state(self):
        """Test creating a new state and check if the record is added to the database."""
        
        # Get the initial number of records in the states table
        self.cursor.execute("SELECT COUNT(*) FROM states;")
        initial_count = self.cursor.fetchone()[0]

        # Simulate the console command to create a new state
        console_input = "create State name='California'\n"
        console_output = StringIO()
        sys.stdout = console_output
        HBNBCommand().onecmd(console_input)  # This runs the command from your console

        # Get the number of records after the command
        self.cursor.execute("SELECT COUNT(*) FROM states;")
        final_count = self.cursor.fetchone()[0]

        # Check if one record was added
        self.assertEqual(final_count, initial_count + 1)

    def tearDown(self):
        """Clean up the test database."""
        self.cursor.execute("DELETE FROM states WHERE name='California';")
        self.db.commit()

    @classmethod
    def tearDownClass(cls):
        """Close MySQL connection."""
        cls.db.close()

if __name__ == '__main__':
    unittest.main()
