#!/usr/bin/python3
"""The console for AirBnB clone"""

import cmd
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    """Define the functionality of the HBNB console"""
    prompt = '(hbnb) '

    cls = {'BaseModel': BaseModel}

    def emptyline(self):
        """
        Override emptyline method to do nothing when an empty line is entered.
        """
        pass

    def do_quit(self, args):
        """Quit the programe"""
        return True

    def help_quit(self):
        """Print the help documentation for quit"""
        print('Quit command to exit the program\n')

    def do_EOF(self, args):
        """Quit the programe in case of end of file"""
        return True

    def help_EOF(self):
        """Print the help documentation for EOF"""
        print('Exit the program\n')

    def do_create(self, class_name):
        """Creates a new instance, saves it and prints the id"""
        if not class_name:
            print('** class name missing **')
            return

        if class_name not in self.cls:
            print('** class doesn\'t exist **')
            return

        model = self.cls[class_name]()
        print(model.id)
        storage.save()

    def help_create(self):
        """Print the help documentation for create"""
        print('Usage: create <model>')
        print('Creates a new instance of any model, saves it to JSON file and')
        print('prints the id of the new model\n')

    def do_show(self, args):
        """Prints the string representation of an instance"""
        if not args:
            print('** class name missing **')
            return

        class_name = args.split()[0]
        if class_name not in self.cls:
            print('** class doesn\'t exist **')
            return

        if len(args.split()) < 2:
            print('** instance id missing **')
            return

        id = args.split()[1]
        key = f"{class_name}.{id}"

        if key not in storage.all().keys():
            print('** no instance found **')
            return

        print(storage.all()[key])

    def help_show(self):
        """Print the help documentation for show method"""
        print('Usage: show <class name> <instance id>')
        print('Prints the string representation of an instance based on id\n')

    def do_destroy(self, args):
        """Deletes an instance based on the class name and id"""
        if not args:
            print('** class name missing **')
            return

        class_name = args.split()[0]
        if class_name not in self.cls:
            print('** class doesn\'t exist **')
            return

        if len(args.split()) < 2:
            print('** instance id missing **')
            return

        id = args.split()[1]
        key = f"{class_name}.{id}"

        if key not in storage.all().keys():
            print('** no instance found **')
            return

        del(storage.all()[key])
        storage.save()

    def help_destroy(self):
        """Print the help documentation for destroy method"""
        print('Usage: destroy <class name> <instance id>')
        print('Deletes an instance based on the class name and id\n')

    def do_all(self, args):
        """Prints all string representation of all instances"""
        models = []

        if args:
            class_name = args.strip()
            if class_name not in self.cls:
                print('** class doesn\'t exist **')
                return
            else:
                for key, model in storage.all().items():
                    if key.split('.')[0] == class_name:
                        models.append(str(storage.all()[key]))
        else:
            for model in storage.all().values():
                models.append(str(model))

        print(models)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
