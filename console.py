#!/usr/bin/python3
"""The console for AirBnB clone"""

import cmd
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models import storage


class HBNBCommand(cmd.Cmd):
    """Define the functionality of the HBNB console"""
    prompt = '(hbnb) '

    cls = {'BaseModel': BaseModel, 'User': User, 'State': State,
           'City': City, 'Amenity': Amenity, 'Place': Place,
           'Review': Review}

    def emptyline(self):
        """
        Override emptyline method to do nothing when an empty line is entered.
        """
        pass

    def precmd(self, line):
        """Handel advanced command syntax"""
        if not ('.' and '(' and ')') in line:
            return line
        else:
            class_name = line.split('.')[0]
            command = line.split('.')[1].split('(')[0]
            args = line.split('(')[1].split(')')[0]
            if ('{' and '}') not in args and ',' in args:
                args = ' '.join(args.split(','))
            elif ('{' and '}' and ',') in args:
                dic = args.split('{')[1].split('}')[0]
                args = ' '.join(args.split('{')[0].split(','))
                args = ' '.join([args, dic])
            return f"{command} {class_name} {args}"


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

    def do_count(self, class_name):
        """Retrieve the number of instances of a class"""
        if not class_name:
            print('** class name missing **')
            return

        if class_name not in self.cls:
            print('** class doesn\'t exist **')
            return

        count = 0
        for obj in storage.all().values():
            if obj.to_dict()['__class__'] == class_name:
                count += 1
        print(count)

    def help_count(self):
        """Print the help ducomentation for the count method"""
        print('Usage: count <class name>')
        print('count the number of instances of a class')

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

    def do_all(self, class_name):
        """Prints all string representation of all instances"""
        models = []

        if class_name:
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

    def help_all(self):
        """Print the help documentation for the method all"""
        print('Usage: all <class name (optional)>')
        print('Will print all the instances of a class')
        print('if the class name is not specified it will print all models\n')

    def do_update(self, args):
        """Update an instance based on class name and id"""
        if not args:
            print('** class name missing **')
            return
        else:
            args = args.split()
            class_name = args[0]

        if class_name not in self.cls:
            print('** class doesn\'t exist **')
            return

        if len(args) < 2:
            print('** instance id missing **')
            return
        else:
            id = args[1]

        key = f"{class_name}.{id}"
        if key not in storage.all().keys():
            print('** no instance found **')
            return

        if len(args) < 3:
            print('** attribute name missing **')
            return
        else:
            attr = args[2]

        if len(args) < 4:
            print('** value missing **')
            return
        else:
            if '"' in ''.join(args[3:]):
                value = ' '.join(args[3:]).split('"')[1]
            else:
                value = args[3]

        key = f"{class_name}.{id}"
        new_dict = storage.all()[key]

        new_dict.__dict__.update({attr: value})
        new_dict.save()

    def help_update(self):
        """Print the hep documentation for the update method"""
        print('Usage: update <class name> <id> <attribute> <value>')
        print('Updates an instance based on the class name and id by adding or',
              'updating attribute')
        print('No spaces are allowed in the value of the attribute,',
              'if you need space the value must be between \'"\'')


if __name__ == '__main__':
    HBNBCommand().cmdloop()
