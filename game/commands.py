from rich.console import Console
from rich.table import Table
from rich.panel import Panel

class CommandParser:
  def __init__(self, game_engine):
    self.game_engine = game_engine
    self.console = Console()
    self.commands = {
      "north": self.move_command,
      "south": self.move_command,
      "east": self.move_command,
      "west": self.move_command,
      "help": self.help_command,
      "look": self.look_command,
      "inventory": self.inventory_command,
      "inv": self.inventory_command,
      "take": self.take_command,
      "drop": self.drop_command,
      "examine": self.examine_command,
      #"use": self.use_command,
      #"talk": self.talk_command,
      #"give": self.give_command,
      #"open": self.open_command,
      "quit": self.quit_command,
      "exit": self.quit_command
    }

  
  
  def parse_command(self, command_string):
    """Parse a command string and execute the corresponding command"""
    words = command_string.lower().split()
    if not words:
      return

    command = words[0]
    args = words[1:] if len(words) > 1 else []

    if command in self.commands:
      self.commands[command](command, *args)
    else:
      self.console.print("[red]Invalid command. Type 'help' for a list of commands.[/red]")

  def help_command(self, *args):
    """Display a list of available commands"""
    help_table = Table(title="Available Commands", show_header=True, header_style="bold magenta")
    help_table.add_column("Command", style="cyan")
    help_table.add_column("Description", style="white")

    commands_help = {
      "north/south/east/west": "Move in that direction",
      "look": "Look around the current room",
      "inventory/inv": "Display the items in your inventory",
      "take <item>": "Pick up an item and add to your inventory",
      "drop <item>": "Drop an item from your inventory",
      "examine <item>": "Look closely at an item",
      "use <item>": "Use an item in your inventory",
      "talk [choice]": "Talk to a character",
      "give <item>": "Give an item to a character",
      "open <container>": "Open a container or chest",
      "help": "Display this help message",
      "quit/exit": "Exit the game"
    }

    for command, description in commands_help.items():
      help_table.add_row(command, description)

    self.console.print(help_table)

  def move_command(self, direction):
    """Handle movement commands"""
    current_room = self.game_engine.player.current_room

    # Check if the direction is valid
    # ***CODE FOR SOLVED PUZZLE MAY NEED TO BE EDITED***
    if direction in current_room.locked_exits:
      room, puzzle = current_room.locked_exits[direction]
      if puzzle.is_solved:
        current_room.unlock_direction(direction)
      else:
        self.console.print("[red]That path is locked.[/red]")
        return

    # Move the player to the new room
    if self.game_engine.player.move(direction):
      self.game_engine.clear_screen()
      self.console.print(f"[green]You move {direction.capitalize()}[/green]")
    else:
      self.console.print("[red]You can't go that way.[/red]")

  def look_command(self, *args):
    """Look around the current room"""
    self.game_engine.clear_screen()
    self.game_engine.display_room()

  def inventory_command(self, *args):
    """Display the player's inventory"""
    inventory = self.game_engine.player.get_inventory()
    if inventory:
      self.console.print("\n[yellow]Your inventory:[/yellow]")
      for item in inventory:
        self.console.print(f"- {item.name}")
    else:
      self.console.print("\n[yellow]Your inventory is empty.[/yellow]")

  def take_command(self, command, *args):
    """Handle taking items"""
    if not args:
      self.console.print("[red]What do you want to take?[/red]")
      return

    item_name = " ".join(args)
    current_room = self.game_engine.player.current_room
    item = current_room.get_item(item_name)

    if item:
      if item.can_take:
        current_room.remove_item(item_name)
        self.game_engine.player.add_to_inventory(item)
        self.console.print(f"[green]You take the {item.name}.[/green]")
      else:
        self.console.print("[red]You can't take that.[/red]")
    else:
      self.console.print("[red]You don't see that here.[/red]")

  def drop_command(self, command, *args):
    """Handle dropping items"""
    if not args:
      self.console.print("[red]What do you want to drop?[/red]")
      return

    item_name = " ".join(args)
    current_room = self.game_engine.player.current_room

    for item in self.game_engine.player.inventory():
      if item.name.lower() == item_name.lower():
        self.game_engine.player.remove_from_inventory(item)
        current_room.add_item(item)
        self.console.print(f"[green]Dropped: {item.name}.[/green]")
        return

    self.console.print("[red]You don't have that item.[/red]")

  def examine_command(self, command, *args):
    """Handle examining items"""
    if not args:
      self.console.print("[red]What do you want to examine?[/red]")
      return

    item_name = " ".join(args)
    current_room = self.game_engine.player.current_room

    # Check inventory first
    for item in self.game_engine.player.inventory():
      if item.name.lower() == item_name.lower():
        self.console.print(f"\n[yellow]{item.name}[/yellow]")
        self.console.print(item.examine())
        if isinstance(item, Container) and item.is_open:
          contents = item.get_contents()
          if contents:
            self.console.print("\n[yellow]Contents:[/yellow]")
            for content_item in contents:
              self.console.print(f"- {content_item.name}")
        return

    # Check room
    item = current_room.get_item(item_name)
    if item:
      self.console.print(f"\n[yellow]{item.name}[/yellow]")
      self.console.print(item.examine())
      if isinstance(item, Container) and item.is_open:
        contents = item.get_contents()
        if contents:
          self.console.print("\n[yellow]Contents:[/yellow]")
          for content_item in contents:
            self.console.print(f"- {content_item.name}")
    else:
      self.console.print("[red]You don't see that here.[/red]")

  def quit_command(self, *args):
    """Exit the game"""
    self.game_engine.quit_game()