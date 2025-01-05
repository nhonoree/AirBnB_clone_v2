import sys
import cmd
from models import storage
from models.state import State
from models.place import Place
import uuid
from datetime import datetime


class HBNBCommand(cmd.Cmd):
    """Command interpreter for AirBnB"""

    prompt = '(hbnb) '  # Command prompt
    
    def __init__(self):
        super().__init__()
        self.classes = {'State': State, 'Place': Place}

    def do_create(self, arg):
        """Creates a new instance of a class and prints its id"""
        if not arg:
            print("** class name missing **")
            return
        args = arg.split(" ")
        class_name = args[0]

        if class_name not in self.classes:
            print("** class doesn't exist **")
            return

        new_instance = self.classes[class_name]()
        for item in args[1:]:
            try:
                key, value = item.split("=")
                if value[0] == '"' and value[-1] == '"':
                    value = value[1:-1].replace("_", " ")
                elif '.' in value:
                    value = float(value)
                else:
                    value = int(value)
                setattr(new_instance, key, value)
            except ValueError:
                continue

        new_instance.save()
        print(new_instance.id)

    def do_all(self, arg):
        """Prints all instances of a class"""
        if arg:
            if arg not in self.classes:
                print("** class doesn't exist **")
                return
            objects = storage.all(self.classes[arg])
        else:
            objects = storage.all()
        
        instances = []
        for obj in objects.values():
            instances.append(str(obj))
        print(instances)

    def emptyline(self):
        """Handles empty lines in the command line"""
        pass

    def do_quit(self, arg):
        """Quit the command interpreter"""
        return True

    def do_EOF(self, arg):
        """Handle EOF"""
        return True

if __name__ == '__main__':
    HBNBCommand().cmdloop()
