# importing DB settings
from lib.database import FunDb
connect = FunDb.connect()

# Global variables
verbs = ["go", "walk", "move",
         "ask", "take", "chat", "talk", "buy", "eat", "drink", "ride", "look", "examine", "view", "play", "wait",
         "inventory", "i", "help", "h", "quit", "directions", "direction", "q", "e", "n", "ne", "nw", "s", "se",
         "sw", "w", "east", "north", "northeast", "northwest", "south", "southwest", "west"]
prepositions = ["to", "at", "in", "with"]
debug = True

days = 1
asks = 0
name = ""
