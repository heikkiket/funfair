#Global variables
verbs = ["go", "walk", "move",
         "ask", "chat", "talk", "buy", "eat", "drink", "ride", "look", "play", "wait",
         "inventory", "i", "help", "quit", "directions", "q", "e", "n", "ne", "nw", "s", "se",
         "sw", "w", "east", "north", "northeast", "northwest", "south", "southwest", "west"]
prepositions = ["to", "at", "in", "with", "the"]
debug = True

#importing DB settings
from lib.database import FunDb
connect=FunDb.connect()

#muuttujat

#days
#asks
