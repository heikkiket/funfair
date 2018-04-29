import parser
import globals as g
import tips
from lib import utils

#importing DB settings
from lib.database import FunDb
connect=FunDb.connect()


#Dmitri
def direct_to_name (loc):
    location={"n":"North","e":"East","s":"South","w":"West","ne":"Northeast","se":"Southeast","sw":"Southwest","nw":"Northwest"}
    return location[loc]

def getalias (fromname):
    if fromname=="persons":
        fromname="Persons"
        idfield="Person_Id"
    elif fromname=="items":
        fromname="Item_types"
        idfield="Itemtype_Id"
    elif fromname=="places":
        fromname="Places"
        idfield="Place_Id"
    else:
        fromname="Persons"
        idfiled="Person_Id"       
    aliases={}
    cur=connect.cursor()
    sql="select "+idfield+", Alias from "+fromname+" where Alias is not null;"
    cur.execute(sql)
    if cur.rowcount>=1:
        for row in cur.fetchall():
            for alias in row[1].split(";"):
                aliases.update({alias:row[0]})
    return aliases

#aliohjelmat

def prologue():
    utils.print_text("\nThere is a funfair in town...the game begins.\n\nDAY NUMBER: " + str(g.days))
    utils.print_text("MORNING\n\nThe town's own newspaper, Takaseudun Sanomat, has succeeded on putting out a new issue.\n“THE FISHING FESTIVAL MIGHT TAKE PLACE AT THE MARKET PLACE INSTEAD OF THE LOCAL LAKE”\nWhatever. You decide to go to the funfair.\n")
    look(location)
    return

def epilogue():
    return

def night():
    g.asks = 0
    g.days = g.days +1
    if g.days>3:
        final()
    else:
        utils.print_text("\nNow it’s late and you have to go to work. The funfair is closing down.\n\nNIGHT TIME\n")
        utils.print_text("At night you work at the warehouse. When having a break at the yard of the warehouse you see a distant glow from the closed funfair: the employees have set up campfire…\n")
        utils.print_text("DAY NUMBER: " + str(g.days))
        if g.days == 1:
            utils.print_text("MORNING\n\nThe town's own newspaper, Takaseudun Sanomat, has succeeded on putting out a new issue.\n“A LOCAL DEER SUSPECTED OF SPEEDING”\nWhatever. You decide to go to the funfair.\n")
        if g.days == 2:
            utils.print_text("MORNING\n\nThe town's own newspaper, Takaseudun Sanomat, has succeeded on putting out a new issue.\n“TOWN MUSEUM WANTS TO EVICT DOGS CAMPING ON THE MUSEUM YARD”\nWhatever. You decide to go to the funfair.\n")
    return

def final():
    utils.print_text("The campfire!! The END")
    return
                  
def look(location):         
    cur=connect.cursor()
    sql="SELECT Name, Description, Details FROM Places where Place_Id="+str(location)+";"
    cur.execute(sql)
    if cur.rowcount>=1:
        for row in cur.fetchall():
            utils.print_text("\n"+row[0]+"\n\n"+row[1]+"\n\n"+row[2]+"\n\n")
    return

def show_passage(location):
    cur=connect.cursor()
    sql="SELECT Description FROM Directions WHERE Direction_id IN (SELECT direction_id FROM Has_passages WHERE place_id ="+str(location)+")Order by direction_id ASC LIMIT 10;"
    cur.execute(sql)
    if cur.rowcount>=1:
        utils.print_text("From here you can go: ")
        for row in cur.fetchall() :
            utils.print_text(row[0])
    return

def ask(person, place):
    
    utils.print_text("One ask used")
    g.asks = g.asks +1
    if g.asks>1:
        night()
    return

def chat():
    utils.print_text(tips.give_tip())
    cur=connect.cursor()
    sql="SELECT line_text FROM Line LEFT JOIN Persons On persons.`Person_Id` = line.`Person_Id` WHERE Alias = '"+ obj +"' AND line.`Place_Id` = "+str(location)+" ORDER BY RAND() LIMIT 1;"
    cur.execute(sql)
    if cur.rowcount>=1:
        for row in cur:
            utils.print_text(row[0])
    else:
        utils.print_text("The person you want to chat with is not here")
    return
def buy(item):
    return
def drink(item):
    return
def eat(item):
    return
def ride(ride):
    cur=connect.cursor()
    sql="SELECT ACTION FROM Places Where Place_Id ="+str(location)+";"
    cur.execute(sql)
    if cur.rowcount>=1:
        for row in cur:
            utils.print_text(row[0])
    return
def play():
    utils.print_text("You play a game")
    #randomize game??
    return
def wait():
    utils.print_text("What on earth are you waiting for?")
    return
def inventory():
    cur=connect.cursor()
    sql="select Items.Name, Places.Name from Items,Item_types,Places where Items.Itemtype_Id=Item_types.Itemtype_Id and Item_types.Place_Id=Places.Place_Id and Items.Player_Id=\"1\"";
    cur.execute(sql)
    if cur.rowcount>=1:
        utils.print_text("\nYou are holding:\n")
        for row in cur.fetchall():
            utils.print_text(row[0]+" from "+row[1])
    else:
        utils.print_text("\nYou are holding nothing\n")
    utils.print_text("\n")
    return
def help():
    utils.print_text("Print some help here")
    return

def move(location, direction):
    destination=location
    cur=connect.cursor()
    sql = "SELECT `Has_passagesPlace_Id` FROM `Has_passages` WHERE `Direction_Id`= '"+ direction +"' AND `Place_Id` = "+str(location)+";"
    cur.execute(sql)
    if cur.rowcount>=1:
        for row in cur.fetchall():
            destination = row[0]
    return destination

#main loop

#clear the screen
utils.print_text("\n"*100)

#temp addition, can be deleted later
persons=getalias("persons")
utils.print_text(persons)
items=getalias("items")
utils.print_text(items)
places=getalias("places")
utils.print_text(places)

#playr location
location = "1"

prologue()

action = ""
while action != "quit" and action != "q" and g.days<4:
# days muuttuja < 4 / exit
    sentence = input("What will you do? ")
    ret=parser.process_sentence(sentence)
    action=ret[0]
    obj=ret[1]
    iobj=[2]
# look [location]
    if (action in ["look", "examine", "view"]):
        look(location)
# diretions
    if (action=="directions"):
        show_passage(location)
# move

    if (action in ["go","walk","move"] and obj in ["e", "n", "ne", "nw", "s", "se", "sw", "w", "east", "north", "northeast", "northwest", "south", "southwest", "west"]):
        newlocation = move(location,obj)
        location = newlocation
        look(location)
        
    if (action in ["e", "n", "ne", "nw", "s", "se", "sw", "w", "east", "north", "northeast", "northwest", "south", "southwest", "west"]):
        newlocation = move(location,action)
        location = newlocation
        look(location)
       
# ask/take [person] to [place]
    if (action=="ask" or action=="take" and obj in [persons] and iobj in [places]):
        ask(obj, iobj)
# chat/talk to/with [person]
    if (action=="chat" or action=="talk" and obj in [persons]):
        utils.print_text(location)
        utils.print_text(obj)
        chat()
# buy [item]
# drink [item]
# eat [item]
# ride [ride]
    if (action=="ride" and obj in ["carousel", "roller", "wormster", "bumper"]):
        ride(location)
# play [game]
    if (action=="play" and location==7):
        play()
    if (action=="play" and location!=7):
        utils.print_text("You have to go to the game hall to play games")
# wait
    if (action=="wait"):
        wait()
# inventory []
    if (action in ["i","inventory"]):
        inventory()
# help
    if (action in ["help", "h"]):
        help()
epilogue()
