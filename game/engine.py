from rich.console import Console
from rich.panel import Panel
from rich.text import Text
import os
import sys
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
        self.console.print("\nType 'help' for a list of commands.\n", style='yellow')

    def game_loop(self):
        """Main game loop"""
        while self.is_running:
            self.display_room()
            self.console.print("\nWhat would you like to do? ", end="")
            command = input().lower().strip()

            if command:
                self.command_parser.parse_command(command)

    def display_room(self):
        """Display current room description and available exits"""
        room = self.player.current_room
        self.console.print(Panel(room.description, title=room.name, style="blue"))

        # Display available exits
        all_exits = []
        # Add normal exits
        if room.exits:
            all_exits.extend([f"[green]{direction}[/green]" for direction in room.exits.keys()])
        # Add locked exits
        if room.locked_exits:
            all_exits.extend([f"[red]{direction}[/red] (locked)" for direction in room.locked_exits.keys()])

        if all_exits:
            self.console.print(f"\nExits: {', '.join(all_exits)}")
        else:
            self.console.print("\nExits: none")

    def quit_game(self):
        """Exit the game"""
        self.console.print("\nThanks for playing!", style="bold green")
        self.is_running = False
        sys.exit(0)

    def start(self):
        """Start the game"""
        self.clear_screen()
        self.display_welcome()
        self.game_loop()

