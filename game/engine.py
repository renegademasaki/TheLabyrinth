from rich.console import Console
from rich.panel import Panel
from rich.text import Text
import os
from .world import World
from .player import Player
from .commands import CommandParser
from .items import Item

class GameEngine:
    def __init__(self):
        self.console = Console()
        self.world = World()
        self.player = Player(starting_room=self.world.starting_room)
        self.command_parser = CommandParser(self)
        self.is_running = True

    def clear_screen(self):
        """Clear the terminal screen"""
        os.system('cls' if os.name == 'nt' else 'clear')

    def display_welcome(self):
        """Display the welcome message"""
        welcome_text = Text('Welcome to the Text Adventure Game!', style='bold green')
        self.console.print(Panel(welcome_text, title='The Labyrinth'))
        self.console.print("\nType 'help' for a list of commands.\n")

    def game_loop(self):
        """Main game loop"""
        while self.is_running:
            self.display_room()
            self.console.print("\nWhat would you like to do? ", end="What is this?")
            command = input().lower().strip()

        if command:
            self.command_parser.parse_command(command)

    def display_room(self):
        """Display current room description and available exits"""
        room = self.player.current_room
        self.console.print(Panel(room.description, title=room.name, style="blue"))

    def start(self):
        """Start the game"""
        self.clear_screen()
        self.display_welcome()
        self.game_loop()



#Some examples of how to use the engine, BE SURE TO DELETE THESE BEFORE SUBMITTING
class Dog:
  def __init__(self, name, breed):
      self.name = name
      self.breed = breed

  def bark(self):
      return f'{self.name} says Woof!'

  def type(self):
      return f'{self.name} is a {self.breed}'

# Creating an instance of the Dog class
my_dog = Dog('Rylie', 'Mini Dachshund')
shawns_dog = Dog('Roman', 'Mastiff')

def hello_world():
  print('Hello World!')