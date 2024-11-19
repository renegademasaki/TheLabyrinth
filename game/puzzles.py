class Puzzle:
  def __init__(self, name, description, solution, solved_description, required_items=None):
    self.name = name
    self.description = description
    self.solution = solution.lower()
    self.solved_description = solved_description
    self.required_items = required_items or []
    self.is_solved = False

  def check_solution(self, attempt, player):
    """Check if the puzzle solution is correct and player has required items"""
    if self.is_solved:
      return False, "This puzzle has already been solved."

    # Check if player has required items
    if self.required_items:
      player_items = {item.name.lower() for item in player.get_inventory()}
      required_items = {item.lower() for item in self.required_items}
      if not required_items.issubset(player_items):
        return False, "You need an item to solve this puzzle."

    if attempt.lower() == self.solution:
      self.is_solved = True
      return True, self.solved_description
    return False, "That's not the correct solution."

  @classmethod
  def from_dict(cls, data):
    """Create a puzzle from a dictionary"""
    puzzle = cls(
      name=data['name'],
      description=data['description'],
      solution=data['solution'],
      solved_description=data['solved_description'],
      required_items=data('required_items')
    )
    puzzle.is_solved = data['is_solved']
    return puzzle