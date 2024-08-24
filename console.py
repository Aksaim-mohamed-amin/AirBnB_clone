#!/usr/bin/python3
"""The console for AirBnB clone"""

import cmd


class HBNBCommand(cmd.Cmd):
    """Define the functionality of the HBNB console"""
    prompt = '(hbnb) '

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


if __name__ == '__main__':
    HBNBCommand().cmdloop()
