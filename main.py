import parser
import globals as g
import tips
from lib import utils
import random

# importing DB settings
from lib.database import FunDb

connect = FunDb.connect()
cur = connect.cursor()


# aliohjelmat

def main_menu():
    utils.print_text()
    utils.print_text("F U N F A I R   A F F A I R", True)
    utils.print_text("2018", True)
    utils.print_text("Dmitri Tsyganok, Suvi Sihvola, Heikki Ketoharju", True)
    utils.print_text("\n\n\n\n\n")
    g.name = input("How can I call you? ")

    # result = cur.execute("SELECT ifnull(MAX(Player_Id),0) + 1 from Player;")
    # result.
    # result_list = result.fetchall()
    # result_list[0][0]

    query = "INSERT INTO Player(Player_Id, Name, Score, Place_Id) SELECT ifnull(MAX(Player_Id),0) + 1, '"+g.name+"', 0, " \
            "(select Place_Id from Places where Name=\"Warehouse\") from Player;"
    print(query)
    cur.execute(query)


def prologue():

    clear_screen()
    utils.print_text("Hello, " + str(g.name) + ", and welcome! Let's play!")
    utils.print_text("\nThere is a funfair in town...the game begins.\n\nDAY NUMBER: " + str(g.days))
    utils.make_break()
    newspaper()
    look(location)
    return


def epilogue():
    utils.print_text("You have joined the Tivoli Söderholm and moved far away from the town and started to travel with funfair. You’ve traveled around Finland lived a happy life ever after.")
    return


def clear_screen():
    utils.print_text("\n" * 100)


def night():
    g.asks = 0
    g.days = g.days + 1
    if g.days > 3:
        final()
    else:
        utils.print_text("\nNow it’s late and you have to go to work. The funfair is closing down.")
        utils.make_break()
        utils.print_text("\n\nNIGHT TIME\n")
        utils.print_text(
            "At night you work at the warehouse. When having a break at the yard of the warehouse you see a distant glow from the closed funfair: the employees have set up campfire…\n")

        utils.make_break()
        utils.print_text("DAY NUMBER: " + str(g.days))
        newspaper()
        utils.make_break()
    look(location)
    return


def final():
    global location
    utils.make_break()
    if tips.connected_names == 2:
        location = "13"
        utils.print_text("You are entering a campfire place, where everyone of a funfair staff members gathered together around the fire. A busy couple of working days are behind and everyone is relaxing and having a friendly chat with each other. Somebody is laughing. There is a buzz in the air. As soon as you enter the area everyone calms down. You approach the fire. Birgitta, the funfair director, rises up.")

    else:
        utils.print_text("The campfire!! The END You lose :(")
    return


def newspaper():
    # TODO print_text can be pulled from the DB
    # SELECT Line_text FROM Line WHERE Item_Id = %(newspaper_id)s ORDER BY RAND() LIMIT 1
    if g.days == 1:
        print_text = "THE FISHING FESTIVAL MIGHT TAKE PLACE AT THE MARKET PLACE INSTEAD OF THE LOCAL LAKE"
    if g.days == 2:
        print_text = "TOWN MUSEUM WANTS TO EVICT DOGS CAMPING ON THE MUSEUM YARD"
    utils.print_text(
        "MORNING\n\nThe town's own newspaper, Takaseudun Sanomat, has succeeded on putting out a new issue.\n\n\""+print_text+"\"\n\nWhatever. You decide to go to the funfair.\n")
    location = "1"


def look(loc):
    sql = "SELECT Name, Description, Details FROM Places where Place_Id=" + str(loc) + ";"
    cur.execute(sql)
    if cur.rowcount >= 1:
        for row in cur.fetchall():
            utils.print_text("\n" + row[0] + "\n\n" + row[1] + "\n\n" + row[2] + "\n\n")
    return


def show_passage(loc):
    sql = "SELECT Description FROM Directions WHERE Direction_id IN (SELECT direction_id FROM Has_passages WHERE place_id =" + str(
        loc) + ")Order by direction_id ASC LIMIT 10;"
    cur.execute(sql)
    if cur.rowcount >= 1:
        utils.print_text("From here you can go: ")
        for row in cur.fetchall():
            utils.print_text(row[0])
    return


def success(person, where):
    text = "You take " + str(person) + " to visit"
    if where == 2:
        utils.print_text(text + " Elna the Clown. They start planning a show together!")
    elif where == 3:
        utils.print_text(
            text + " the Bumper Car Operator. It's odd but she seems to be in a good mood. She offers the " + str(
                person) + " a ride " \
                          " and this might turn into a friendship")
    elif where == 5:
        utils.print_text(text + " the Security Station. She has been wanting to discuss the weather. " \
                                " " + str(person) + " tells her to cheer up. " \
                                                    "The Security officer can’t hold a smile. They immediately start chatting.")
    elif where == 6:
        utils.print_text(
            text + " the Carousel Operator. She welcomes the company. 'There is a classical consert coming up in the next town we go' she " \
                   " says and they make plans to go together.")
    elif where == 7:
        utils.print_text(
            text + " the Magician smiles and suggests the Pull-a-String where one always wins. The magician has such a charisma, how " \
                   "could the " + str(person) + " resist. The prize is Funfair themed playing cards. Amazing!")
    elif where == 11:
        utils.print_text(
            text + " the Candy Shop Keeper. She has wanted to try to make a giant candy floss but needs help. " + str(
                person) + " offers assistance and children who " \
                          "enter the Candy Shop are thrilled!")
    else:
        utils.print_text(text + " the Cafe Keeper. Peter hugs " + str(
            person) + " and they drink coffee and and split a chocolate brownie.")
    return


def ask(person, where):
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

    success_to_connect = False

    # Get already made connections
    sql = "Select Person_Id FROM Persons Where NOT Connects_Person_Id IS NULL AND Is_Connected = '1'"
    cur.execute(sql)
    made_connections = cur.fetchall()

    if tuple([person]) in made_connections and tuple([person_2]) in made_connections:
        utils.print_text("You have already connected this pair")
        success_to_connect = True

    # Test new connection
    for connection in tips.connections:
        if person in connection and person_2 in connection:
            success(person_2_name, where)
            tips.succesful_connection(connection)
            success_to_connect = True
            if len(tips.connections) > 0:
                utils.print_text("Excellent! One more connection to make.")

    # Print no success -message
    if not success_to_connect:
        text = "You take " + str(person_2_name) + " to visit"
        if where == 2:
            utils.print_text(text + " Elna at the Open-Air Stage. Elna starts her show, but " + str(
                person_2_name) + " doesn’t seem to like it at all.")
        elif where == 3:
            utils.print_text(text + " the Bumper Car Operator. She is yelling at some teens and even though " + str(
                person_2_name) + " would like to " \
                                 "have a ride " + str(person_2_name) + " does not want to bother her.")
        elif where == 5:
            utils.print_text(text + " the Security Officer. No words are exchanged. " + str(
                person_2_name) + " leaves before they have a change to talk")
        elif where == 6:
            utils.print_text(
                text + " the Carousel Operator. At the moment she fed up with everyting and when she sees " + str(
                    person_2_name) + "" \
                                     " she rolls her eyes. 'I will not operate the Carousel for you!'")
        elif where == 7:
            utils.print_text(text + " the Magician, who smiles wickedly. The " + str(
                person_2_name) + " seems to be against all things magic in general.")
        elif where == 11:
            utils.print_text(text + " the Candy Shop Keeper. " + str(
                person_2_name) + " has a sugarless diet and is really struggling to keep strong around all the candies.")
        else:
            utils.print_text(text + " to visit Cafe Keeper. Peter greets you and offers coffee but " + str(
                person_2_name) + " has already had a cup.")
        utils.print_text("You failed making a pair")


    g.asks = g.asks + 1
    # update players location
    location = where

    if made_connections == 4:
        utils.print_text(
            "You have made two connections! No reason to wander around anymore. It's time to enjoy the campfire with all the funfair employees and hear what they have to say.")
        g.days = 4
        final()

    if g.asks > 1:
        night()
    return


def chat():
    sql = "SELECT line_text FROM Line LEFT JOIN Persons On Persons.`Person_Id` = Line.`Person_Id` " \
          "WHERE Alias like '%" + obj + "%' AND Line.`Place_Id` = " + str(location) + " AND Line.`Item_Id` is null " \
                                                                                      "ORDER BY RAND() LIMIT 1;"
    cur.execute(sql)
    if cur.rowcount >= 1:
        for row in cur:
            utils.print_text(row[0])
            utils.print_text(tips.give_tip(ret['direct_person_id']))
    else:
        utils.print_text("The person you want to chat with is not here")
    return

# Need to change Player_Id later if not 1
def buy(item):
    sql = "SELECT Itemtype_Id FROM Item_types WHERE Alias LIKE '%" + item + "%' AND Place_Id = " + str(location) + ";"
    cur.execute(sql)
    if cur.rowcount >= 1:
        for row in cur:
           item_id = row[0]
           sql = "UPDATE Items SET Player_Id = 1 WHERE Item_Id = " + str(item_id) + ";"
           cur.execute(sql)
           sql = "SELECT Name FROM Item_types WHERE Alias LIKE '%" + item + "%';"
           cur.execute(sql)
           if cur.rowcount >= 1:
               for row in cur:
                   utils.print_text("You bought " + row[0])
    else:
        utils.print_text("You cannot buy " + item + " from here")
                                                                                                       
    return

def drink(item):
    return item


def eat(item):
    return item


def ride():
    sql = "SELECT ACTION FROM Places Where Place_Id =" + str(location) + ";"
    cur.execute(sql)
    if cur.rowcount >= 1:
        for row in cur:
            utils.print_text(row[0])
    return


def play(game):
    win = random.randint(1, 4)

    if game == "bottle pyramid":
        bottle_pyramid(win)
    elif game == "pull-a-string" or game == "pull string":
        pull_a_string(win)
    elif game == "climb ladder":
        climb_ladder(win)
    else:
        utils.print_text("What game do you want to play? Possible games are:")
        utils.print_text("    Bottle pyramid\n    Pull-a-string\n    Climb the ladder")
        return

    if win == 1:
        sql = "SELECT Name From Items Where Itemtype_Id = 2 ORDER BY RAND() LIMIT 1;"
        cur.execute(sql)
        if cur.rowcount >= 1:
            utils.print_text("You win!")
            for row in cur:
                utils.print_text("You win " + row[0] + "! Amazing!")

    return

def bottle_pyramid(win):
    if win == 1:
        utils.print_text("You play bottle pyramid and master every throw!")
    else:
        utils.print_text("You play bottle pyramid but it doesn't go very well.")

def pull_a_string(win):
    utils.print_text("You play pull-a-string")

def climb_ladder(win):
    utils.print_text("You play climb the ladder")

def wait():
    utils.print_text("What on earth are you waiting for?")
    return


def inventory():
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
    utils.print_text("Some commands you could find useful:")
    utils.print_text(str(','.join(g.verbs[0:2])))
    utils.print_text(str(','.join(g.verbs[3:4])))
    utils.print_text(str(','.join(g.verbs[5:7])))
    utils.print_text(str(','.join(g.verbs[8:9])))
    utils.print_text(str(','.join(g.verbs[10:11])))
    utils.print_text(str(','.join(g.verbs[12:13])))
    utils.print_text(str(','.join(g.verbs[14:15])))
    utils.print_text(str(''.join(g.verbs[16]) + " [person] to [place]"))
    utils.print_text(str('\n'.join(g.verbs[17:23])))
    utils.print_text("For moving use compass points:")
    utils.print_text(str(','.join(g.verbs[24::])))
    return

def move(loc, direction):
    destination = location

    if len(direction) > 2:
        direction = utils.name_to_direction(direction)
    sql = "SELECT `Has_passagesPlace_Id` FROM `Has_passages` WHERE `Direction_Id`= '" + direction + "' AND `Place_Id` = " + str(
        loc) + ";"
    cur.execute(sql)

    if cur.rowcount >= 1:
        for row in cur.fetchall():
            destination = row[0]

    return destination


# main loop

# clear the screen
clear_screen()

# generate connections and tips
tips.create_connections()
tips.generate_tips()

if g.debug is True:
    tips.show_tips()
    print("Connections: " + str(tips.connections))

# player location
location = "1"

main_menu()

prologue()

action = ""
while action != "quit" and action != "q" and g.days < 4:
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
                sql = "SELECT Person_Id, Place_Id From Persons WHERE Connectable = 1 AND Person_Id ='" + str(
                    person) + "' AND NOT Persons.Place_Id ='" + str(
                    where) + "' AND EXISTS (Select Places.Place_Id From Persons JOIN Places ON Persons.Place_Id = Places.Place_Id WHERE Connectable = 1 AND Places. Place_ID='" + str(
                    where) + "');"
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
    if action == "buy":
        if obj == "":
            utils.print_text("You have to be a bit more specific")
        elif "direct_item_id" in ret:
                buy(obj)
        else:
            utils.print_text("Don't be silly, that's not something you can buy from here")
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
    # drink [item]
    # eat [item]
    # ride [ride]
    if action == "ride":
        if obj == "":
            utils.print_text("You have to be a bit more specific")
        elif "direct_place_id" in ret:
            if ret["direct_place_id"] == location:
                if location == (3 or 4 or 6):
                    ride()
                else:
                    utils.print_text("Excuse me?")
            else:
                utils.print_text("There is nothing for you to ride here")
        else:
            utils.print_text("Are you nuts?")
    # play [game]
    if action == "play" and location == 7:
        play(obj)
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
    if action == "iwannawin":
        tips.connected_names = 2
        final()

epilogue()
