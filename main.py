from game.engine import GameEngine
import game.engine

def main():
  """Entry point for the game"""
  game = GameEngine()
  game.start()

if __name__ == '__main__':
  main()



#Some examples of how to use the engine, BE SURE TO DELETE THESE BEFORE SUBMITTING
game.engine.hello_world()

print(game.engine.my_dog.type())
print(game.engine.my_dog.bark())

print(game.engine.shawns_dog.type())
print(game.engine.shawns_dog.bark())

print('This is a change')