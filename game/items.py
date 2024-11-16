class Item:
  def __init__(self, name, description, can_take=True):
    self.name = name
    self.description = description
    self.can_take = can_take