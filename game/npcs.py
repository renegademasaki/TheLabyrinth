#from .player import Player
from .commands import CommandParser
from .items import Item

class NPC:
  def __init__(self, name, description, dialogue_options):
    self.name = name
    self.description = description
    self.dialogue_options = dialogue_options
    self.current_dialogue_state = "initial"
    self.inventory = []

  def talk(self):
    """Get current dialogue options"""
    return self.dialogue_options.get(self.current_dialogue_state, {})

  def respond(self, choice):
    """Handle player's dialogue choice."""
    current_options = self.dialogue_options.get(self.current_dialogue_state, {})
    if choice in current_options:
        response, next_state = current_options[choice]
        self.current_dialogue_state = next_state
        return response
    return "The goblin doesn't understand what you mean."

  def receive_item(self, item):
    """Handle receiving an item from the player."""
    self.inventory.append(item)
    # Special responses for valuable items
    if item.name in ["Silver Coin"]:
        self.current_dialogue_state = "received_valuable"
        return f"""Oooh! Shiny! {item.name} make Grock very happy! *does a little dance*
        You take rusty old key in return! *he gives you [green]rusty key[/green]*"""
        self.game_engine.player.add_to_inventory(rusty key)
    return f"Grock take {item.name}. Thanks, maybe..."

  @classmethod
  def from_dict(cls, data, dialogue_options):
    """Create an NPC from a dictionary."""
    npc = cls(
        name=data['name'],
        description=data['description'],
        dialogue_options=dialogue_options
    )
    npc.current_dialogue_state = data['current_dialogue_state']
    return npc

# Create the goblin's dialogue options
GOBLIN_DIALOGUE = {
    "initial": {
        "1": ("*The goblin scratches his head* Me Grock! Me like shiny things! You got shinies?", "about_shinies"),
        "2": ("Why you here? This MY courtyard!", "territory"),
        "3": ("Bye bye, strange tall person!", "initial")
    },
    "about_shinies": {
        "1": ("Grock collect ALL shinies! Gold, silver, pretty rocks... *eyes gleam*", "collection"),
        "2": ("You bring Grock shinies, Grock be happy! Maybe share secrets...", "initial"),
        "3": ("Bye bye! Come back with shinies!", "initial")
    },
    "territory": {
        "1": ("Grock live here long time. Find MANY shinies!", "about_shinies"),
        "2": ("You seem okay. We share courtyard. Maybe...", "initial"),
        "3": ("Go away now! Unless you got shinies...", "initial")
    },
    "collection": {
        "1": ("Grock have BIG collection! *proudly pats pocket with holes*", "about_shinies"),
        "2": ("Most shinies fall through pocket holes... *looks sad*", "initial"),
        "3": ("Bye bye! Help Grock find more shinies!", "initial")
    },
    "received_valuable": {
        "1": ("Grock LOVE new shiny! Thank you!", "about_shinies"),
        "2": ("You good friend! Bring more shinies!", "initial"),
        "3": ("Grock go count shinies now. Bye!", "initial")
    }
}

def create_goblin():
  """Create a goblin NPC with predefined dialogue"""
  return NPC(
    "Grock",
    "A small, green goblin with a mischievous grin and pockets full of holes.",
    GOBLIN_DIALOGUE
  )