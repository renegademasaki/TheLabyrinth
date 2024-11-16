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
      "take": self.take_command,
      "drop": self.drop_command,
      "examine": self.examine_command,
      "use": self.use_command,
      "talk": self.talk_command,
      "give": self.give_command,
      "open": self.open_command,
      "quit": self.quit_command,
      "exit": self.quit_command
    }

  def parse_command(self, command_string):
    """Parse a command string and execute the corresponding command"""
    words = command_string.lower().split()
    if not words:
      return

  #a bunch of code I don't understand
  