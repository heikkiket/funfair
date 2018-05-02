import parser
import globals as g
import tips
from lib import utils

# importing DB settings
from lib.database import FunDb

connect = FunDb.connect()


# Dmitri
def direct_to_name(loc):
    locations = {"n": "North", "e": "East", "s": "South", "w": "West", "ne": "Northeast", "se": "Southeast",
                 "sw": "Southwest", "nw": "Northwest"}
    return locations[loc]


# aliohjelmat


def prologue():
    utils.print_text("\nThere is a funfair in town...the game begins.\n\nDAY NUMBER: " + str(g.days))
    utils.print_text(
        "MORNING\n\nThe town's own newspaper, Takaseudun Sanomat, has succeeded on putting out a new issue.\n“THE FISHING FESTIVAL MIGHT TAKE PLACE AT THE MARKET PLACE INSTEAD OF THE LOCAL LAKE”\nWhatever. You decide to go to the funfair.\n")
    look(location)
    return


def epilogue():
    return


def night():
    g.asks = 0
    g.days = g.days + 1
    if g.days > 3:
        final()
    else:
        utils.print_text("\nNow it’s late and you have to go to work. The funfair is closing down.\n\nNIGHT TIME\n")
        utils.print_text(
            "At night you work at the warehouse. When having a break at the yard of the warehouse you see a distant glow from the closed funfair: the employees have set up campfire…\n")
        utils.print_text("DAY NUMBER: " + str(g.days))
        if g.days == 1:
            utils.print_text(
                "MORNING\n\nThe town's own newspaper, Takaseudun Sanomat, has succeeded on putting out a new issue.\n“A LOCAL DEER SUSPECTED OF SPEEDING”\nWhatever. You decide to go to the funfair.\n")
        if g.days == 2:
            utils.print_text(
                "MORNING\n\nThe town's own newspaper, Takaseudun Sanomat, has succeeded on putting out a new issue.\n“TOWN MUSEUM WANTS TO EVICT DOGS CAMPING ON THE MUSEUM YARD”\nWhatever. You decide to go to the funfair.\n")
    location = "1"
    look(location)
    return


def final():
    utils.print_text("The campfire!! The END")
    return


def look(loc):
    cur = connect.cursor()
    sql = "SELECT Name, Description, Details FROM Places where Place_Id=" + str(loc) + ";"
    cur.execute(sql)
    if cur.rowcount >= 1:
        for row in cur.fetchall():
            utils.print_text("\n" + row[0] + "\n\n" + row[1] + "\n\n" + row[2] + "\n\n")
    return


def show_passage(loc):
    cur = connect.cursor()
    sql = "SELECT Description FROM Directions WHERE Direction_id IN (SELECT direction_id FROM Has_passages WHERE place_id =" + str(
        loc) + ")Order by direction_id ASC LIMIT 10;"
    cur.execute(sql)
    if cur.rowcount >= 1:
        utils.print_text("From here you can go: ")
        for row in cur.fetchall():
            utils.print_text(row[0])
    return


def ask(person, where):
    # split connections
    connections_1, connections_2 = tips.split_connections(tips.connections)
    print("Connection 1: "+ str(connections_1))
    print("Connection 2: "+ str(connections_2))
    cur = connect.cursor()
    person_2 = ""
    #get person_2 id
    sql = "SELECT Person_Id FROM Persons WHERE Place_Id = " + str(where) + ";"
    cur.execute(sql)
    if cur.rowcount >= 1:
        for row in cur.fetchall():
            person_2 = row[0]
    print("You tried:" + str(person) + " and " + str(person_2))
    if str(person) in connections_1 and str(person_2) in connections_1:
        utils.print_text("It’s a successful pair!")
        tips.connected_names = tips.connected_names + 1
    elif str(person) in connections_2 and str(person_2) in connections_2:
        utils.print_text("It’s a successful pair!")
        tips.connected_names = tips.connected_names + 1
    else:
        utils.print_text("You failed making a pair")
    if tips.connected_names == 2:
        utils.print_text("You have made two connections! No reason to wander around anymore. It's time to enjoy the campfire with all the funfair employees and hear what they have to say.")
        g.days = 4
        final()
    g.asks = g.asks + 1
    if g.asks > 1:
        night()
    return


def chat():
    cur = connect.cursor()
    sql = "SELECT line_text FROM Line LEFT JOIN Persons On Persons.`Person_Id` = Line.`Person_Id` WHERE Alias like '%" + obj + "%' AND Line.`Place_Id` = " + str(location) + " AND Line.`Item_Id` is null ORDER BY RAND() LIMIT 1;"
    cur.execute(sql)
    if cur.rowcount >= 1:
        for row in cur:
            utils.print_text(row[0])
            utils.print_text(tips.give_tip())
    else:
        utils.print_text("The person you want to chat with is not here")
    return


def buy(item):
    
    return item


def drink(item):
    return item


def eat(item):
    return item


def ride(rid):
    cur = connect.cursor()
    sql = "SELECT ACTION FROM Places Where Place_Id =" + str(location) + ";"
    cur.execute(sql)
    if cur.rowcount >= 1:
        for row in cur:
            utils.print_text(row[0])
    return


def play():
    utils.print_text("You play a game")
    # randomize game??
    return


def wait():
    utils.print_text("What on earth are you waiting for?")
    return


def inventory():
    cur = connect.cursor()
    # Need to change "1" at the end of this line
    sql = "select Items.Name, Places.Name from Items,Item_types,Places where Items.Itemtype_Id=Item_types.Itemtype_Id and Item_types.Place_Id=Places.Place_Id and Items.Player_Id=\"1\""
    cur.execute(sql)
    if cur.rowcount >= 1:
        utils.print_text("\nYou are holding:\n")
        for row in cur.fetchall():
            utils.print_text(row[0] + " from " + row[1])
    else:
        utils.print_text("\nYou are holding nothing\n")
    utils.print_text("\n")
    return


def helpme():
    utils.print_text("Print some help here")
    return


def move(loc, direction):
    destination = location
    cur = connect.cursor()
    sql = "SELECT `Has_passagesPlace_Id` FROM `Has_passages` WHERE `Direction_Id`= '" + direction + "' AND `Place_Id` = " + str(
        loc) + ";"
    cur.execute(sql)
    if cur.rowcount >= 1:
        for row in cur.fetchall():
            destination = row[0]
    return destination


# main loop

# clear the screen
utils.print_text("\n" * 100)


# temp addition, can be deleted later
# persons = getalias("persons")
# utils.print_text(persons)
# items = getalias("items")
# utils.print_text(items)
# places = getalias("places")
# utils.print_text(places)

# generate connections and tips
tips.create_connections()
tips.generate_tips()

if g.debug is True:
    print("Connections: " + str(tips.connections))

# player location
location = "1"

prologue()

action = ""
while action != "quit" and action != "q" and g.days < 4:
    # days muuttuja < 4 / exit
    sentence = input("What will you do? ")
    ret = parser.process_sentence(sentence)
    action = ret["verb"]
    obj = ret["object"]
    iobj = ret["indirect"]

    # look [location]
    if action in ["look", "examine", "view"]:
        look(location)
    # directions
    if action in ["directions", "direction"]:
        show_passage(location)
    # move

    if action in ["go", "walk", "move"] and obj in ["e", "n", "ne", "nw", "s", "se", "sw", "w", "east", "north",
                                                    "northeast", "northwest", "south", "southwest", "west"]:
        newlocation = move(location, obj)
        location = newlocation
        look(location)

    if action in ["e", "n", "ne", "nw", "s", "se", "sw", "w", "east", "north", "northeast", "northwest", "south",
                  "southwest", "west"]:
        newlocation = move(location, action)
        location = newlocation
        look(location)

    # ask/take [person] to [place]
    if action == "ask" or action == "take" and ret["direct_person_id"] != 0 and ret["indirect_place_id"] != 0 and location != ret["indirect_place_id"]:
        SELECT
        Person_Id, Place_Id
        From
        Persons
        WHERE
        Connectable = 1
        AND
        Person_Id = 1
        AND
        NOT
        Persons.Place_Id = 13
        AND
        EXISTS
        (Select Places.Place_Id From Persons
        JOIN Places ON Persons.Place_Id = Places.Place_Id
        WHERE Connectable = 1 AND Places.Place_ID=13);

        person = ret["direct_person_id"]
        where = ret["indirect_place_id"]
        wrong = "There is something wrong with what you're asking (person or place where you're asking to go"
        if location in [2, 3, 5, 6, 7, 11, 12] and where in [2, 3, 5, 6, 7, 11, 12] and person in [1, 2, 3, 4, 5, 6, 7]:
            if location == 2 and where == 2:
                utils.print_text(wrong)
            elif location == 3 and where == 3:
                utils.print_text(wrong)
            elif location == 5 and where == 5:
                utils.print_text(wrong)
            elif location == 6 and where == 6:
                utils.print_text(wrong)
            elif location == 7 and where == 7:
                utils.print_text(wrong)
            elif location == 11 and where == 11:
                utils.print_text(wrong)
            elif location == 12 and where == 12:
                utils.print_text(wrong)
            elif location == 2 and person != 1:
                utils.print_text(wrong)
            elif location == 3 and person != 4:
                utils.print_text(wrong)
            elif location == 5 and person != 3:
                utils.print_text(wrong)
            elif location == 6 and person != 5:
                utils.print_text(wrong)
            elif location == 7 and person != 2:
                utils.print_text(wrong)
            elif location == 11 and person != 7:
                utils.print_text(wrong)
            elif location == 12 and person != 6:
                utils.print_text(wrong)
            else:
                ask(person, where)
        else:
            utils.print_text(wrong)
            
    # buy [item]
    if action == "buy" and ret["direct_item_id"] != 0:
        buy(obj)
    # drink [item]
    # eat [item]
    # chat/talk to/with [person]
    if action == "chat" or action == "talk" and ret["direct_person_id"] != 0:
        if g.debug:
            utils.print_text(location)
            utils.print_text(obj)
        chat()
    # buy [item]
    # drink [item]
    # eat [item]
    # ride [ride]
    if action == "ride" and obj in ["carousel", "roller", "wormster", "bumper"]:
        ride(location)
    # play [game]
    if action == "play" and location == 7:
        play()
    if action == "play" and location != 7:
        utils.print_text("You have to go to the game hall to play games")
    # wait
    if action == "wait":
        wait()
    # inventory []
    if action in ["i", "inventory"]:
        inventory()
    # help
    if action in ["help", "h"]:
        helpme()

epilogue()
