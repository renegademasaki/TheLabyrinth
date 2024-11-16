from engine import GameEngine

def main():
  """Entry point for the game."""
  game = GameEngine()
  game.start()

if __name__ == '__main__':
  main()



#Some examples of how to use the engine, BE SURE TO DELETE THESE BEFORE SUBMITTING
#engine.hello_world()

print(engine.my_dog.type())
print(engine.my_dog.bark())

print(engine.shawns_dog.type())
print(engine.shawns_dog.bark())

print('This is a change')