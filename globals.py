# importing DB settings
from lib.database import FunDb

connection = FunDb.connect()
cur = connection.cursor()

# Global variables
verbs = ["go", "walk", "move", "chat", "talk", "look", "examine", "view", "directions", "direction", "inventory", "i",
         "help", "h", "quit", "q", "ask",
         "take",
         "buy",
         "eat",
         "drink",
         "ride",
         "play",
         "wait",
         "north", "n",
         "northeast", "ne",
         "east", "e",
         "southeast", "se",
         "south", "s",
         "southwest", "sw",
         "west", "w",
         "northwest", "nw",
         "read"]

prepositions = ["to", "at", "in", "with"]
debug = False

days = 1
asks = 0
location = "1"

name = ""
name_id = 0

night = False

victory = False
