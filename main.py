import parser
import mysql.connector
import globals

#Dmitri
def direct_to_name (loc):
    location={"n":"North","e":"East","s":"South","w":"West","ne":"Northeast","se":"Southeast","sw":"Southwest","nw":"Northwest"}
    return location[loc]

x=direct_to_name("ne")
print ("Hello "+x)

#aliohjelmat

def prologue():
    return 
def epilogue():
    return
def night():
    return
def final():
    return
def look(location):
    print ("Looking in somewhere")
    return
def show_passages(location):
    return
def ask(person, place):
    return
def chat(person):
    return
def buy(item):
    return
def drink(item):
    return
def eat(item):
    return
def ride(ride):
    return
def play(game):
    return
def wait():
    return
def inventory():
    return
def help():
    return
def move(location, direction):
    return

#main loop

while True:
# days muuttuja < 4 / exit

    sentence = input("What will you do? ")
    ret=parser.process_sentence(sentence)
    action=ret[0]
# look [location]
    if (action=="look" or action=="examine" or action=="view"):
        look(1)
# ask/take [person] to [place]
# chat/talk to/with [person]
# buy [item]
# drink [item]
# eat [item]
# ride [ride]
# play [game]
# wait
# inventory []
# help
# e, w, s, n, etc direction
