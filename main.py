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
    look(location)
    return


def final():
    if tips.connected_names == 2:
        utils.print_text("The campfire!! The END You win!")
    else:
        utils.print_text("The campfire!! The END You lose :(")
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

def success(person, where):
    text = "You take " + str(person) + " to visit "
    if where == 2:
        utils.print_text(text + " Elna the Clown. They start planning a show together!")
    elif where == 3:
        utils.print_text(text + " the Bumper Car Operator. It's odd but she seems to be in a good mood. She offers the " + str(person) + " a ride "\
        " and this might turn into a friendsip")
    elif where == 5:
        utils.print_text(text + " the Security Station. She has been wanting to discuss the weather. " \
        " "+ str(person) + " tells her to cheer up. "\
        "The Security officer can’t hold a smile. They immediately start chatting.")
    elif where == 6:
        utils.print_text(text + " the Carousel Operator. She welcomes the company. 'There is a classical consert coming up in the next town we go' she "\
        " says and they make plans to go together.")
    elif where == 7:
        utils.print_text(text + " the Magician smiles and suggests the Pull-a-String where one always wins. The magician has such a charisma, how "\
        "could the "+ str(person_2_name) + " resist. The prize is Funfair themed playing cards. Amazing!")
    elif where == 11:
        utils.print_text(text + " the Candy Shop Keeper. She has wanted to try to make a giant candy floss but needs help. " + str(person) + " offers assistance and children who "\
        "enter the Candy Shop are thrilled!")
    else:
        utils.print_text(text + " the Cafe Keeper. Peter hugs " + str(person) + " and they drink coffee and and split a chocolate brownie.")
    return

def ask(person, where):
    print("Connection 1: "+ str(connections_1))
    print("Connection 2: "+ str(connections_2))
    cur = connect.cursor()
    person_2 = ""
    sql = "SELECT Person_Id FROM Persons WHERE Place_Id = " + str(where) + ";"
    cur.execute(sql)
    if cur.rowcount >= 1:
        for row in cur.fetchall():
            person_2 = row[0]
            print("You tried:" + str(person) + " and " + str(person_2))
    sql = "SELECT Name FROM Persons WHERE Person_Id = " + str(person) + ";"
    cur.execute(sql)
    if cur.rowcount >= 1:
        for row in cur.fetchall():
            person_2_name = row[0]
    if str(person) in connections_1 and str(person_2) in connections_1:
        success(person_2_name, where)
        tips.connected_names = tips.connected_names + 1
        del connections_1[:]
        tips.connected_pair.append(person)
        tips.connected_pair.append(person_2)
        if tips.connected_names == 1:
            utils.print_text("Excellent! One more connection to make.")
    elif person in connection and person_2 in connection
        success(person_2_name, where)
        tips.connected_names = tips.connected_names + 1
        tips.connected_pair.append(person)
        tips.connected_pair.append(person_2)
        del connections_2[:]
        if tips.connected_names == 1:
            utils.print_text("Excellent! One more connection to make.")
    elif str(person) in tips.connected_pair and str(person_2) in tips.connected_pair:
        utils.print_text("You have already connected this pair")
    else:
        text = "You take " + str(person_2_name) + " to visit"
        if where == 2:
            utils.print_text(text + " Elna at the Open-Air Stage. Elna starts her show, but "+ str(person_2_name) + " doesn’t seem to like it at all.")
        elif where == 3:
            utils.print_text(text + " the Bumper Car Operator. She is yelling at some teens and even though " + str(person_2_name) + " would like to "\
            "have a ride "+ str(person_2_name) + " does not want to bother her.")
        elif where == 5:
            utils.print_text(text + " the Security Officer. No words are exchanged. "+ str(person_2_name) + " leaves before they have a change to talk")
        elif where == 6:
            utils.print_text(text + " the Carousel Operator. At the moment she fed up with everyting and when she sees " + str(person_2_name) + ""\
            " she rolls her eyes. 'I will not operate the Carousel for you!'")
        elif where == 7:
            utils.print_text(text + " the Magician, who smiles wickedly. The " + str(person_2_name) + " seems to be against all things magic in general.")
        elif where == 11:
            utils.print_text(text + " the Candy Shop Keeper. " + str(person_2_name) +" has a sugarless diet and is really struggling to keep strong around all the candies.")
        else:
            utils.print_text(text + " to visit Cafe Keeper. Peter greets you and offers coffee but " + str(person_2_name) +" has already had a cup.")
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
connections_1, connections_2 = tips.split_connections(tips.connections)

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
    if action == "ask" or action == "take":
        wrong = "There is something wrong with what you're asking (person or place where you're asking to go)"
        if obj == "":
            utils.print_text("Could you specify who who would you like to take somewhere?")
        elif "direct_person_id" in ret and "indirect_place_id" in ret:
            if ret["direct_person_id"] != 0 and ret["indirect_place_id"] != 0 and location != ret["indirect_place_id"]:
                person = ret["direct_person_id"]
                where = ret["indirect_place_id"]
                cur = connect.cursor()
                sql = "SELECT Person_Id, Place_Id From Persons WHERE Connectable = 1 AND Person_Id ='" + str(person) + "' AND NOT Persons.Place_Id ='" + str(where) + "' AND EXISTS (Select Places.Place_Id From Persons JOIN Places ON Persons.Place_Id = Places.Place_Id WHERE Connectable = 1 AND Places. Place_ID='" + str(where) + "');"
                cur.execute(sql)
                if cur.rowcount == 1:
                    ask(person, where)
                else:
                    utils.print_text(wrong)
            else:
                utils.print_text(wrong)
        else:
            utils.print_text(wrong)

    # buy [item]
    if action == "buy" and ret["direct_item_id"] != 0:
        buy(obj)
    # drink [item]
    # eat [item]
    # chat/talk to/with [person]
    if action == "chat" or action == "talk":
        if obj == "":
            utils.print_text("You have to be a bit more specific")
        elif "direct_person_id" in ret:
            chat()
        else:
            utils.print_text("Are you nuts?")
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
