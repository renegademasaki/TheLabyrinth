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