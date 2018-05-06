import parser
import globals as g
import tips
from lib import utils
import random

# importing DB settings
cur = g.cur

# aliohjelmat

def main_menu():
    utils.print_text()
    utils.print_text("F U N F A I R   A F F A I R", True)
    utils.print_text("2018", True)
    utils.print_text("Dmitri Tsyganok, Suvi Sihvola, Heikki Ketoharju", True)
    utils.print_text("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    g.name = input("How can I call you? ")

    cur.execute("SELECT ifnull(MAX(Player_Id),0) + 1 from Player;")
    g.name_id = cur.fetchone()[0]
    query = "INSERT INTO Player(Player_Id, Name, Score, Place_Id) values (" + str(
        g.name_id) + ", '" + g.name + "', 0, (select Place_Id from Places where Name='Warehouse'));"
    cur.execute(query)


def prologue():
    clear_screen()
    utils.print_text("Hello, " + str(g.name) + ", and welcome! Let's play!")
    utils.print_text("\nThere is a funfair in town...the game begins.\n\nDAY NUMBER: " + str(g.days))
    utils.make_break()
    newspaper()
    look(g.location)
    return


def epilogue(success):
    if success:
        utils.print_text("You have joined the Tivoli Söderholm and moved far away from the town and started to travel " \
                         "with funfair. You’ve traveled around Finland lived a happy life ever after.")
    else:
        utils.print_text("In the morning when you are returning from the night shift you notice that the field is " \
                         "empty. You can still barely see few last trucks with funfair logos moving away in the another " \
                         "end of the town main street.\n" \
                         "The summer is soon over and you think how your life is still the same it was when you was a" \
                         "teenager, hoping to get away from this town.")


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
            "At night you work at the warehouse. When having a break at the yard of the warehouse you see a distant glow " \
            "from the closed funfair: the employees have set up campfire…\n")

        utils.make_break()
        utils.print_text("DAY NUMBER: " + str(g.days))
        newspaper()
        utils.make_break()
    g.location = "1"
    look(g.location)
    return


def final():
    global location
    utils.make_break()
    if tips.connected_names == 2:
        location = "13"
        # Bring everyone to the campfire
        sql = "UPDATE Persons SET Place_Id=13"
        # cur.execute(sql)

        g.night = True
        g.victory = True
        utils.print_text(
            "You are entering a campfire place, where everyone of a funfair staff members gathered together " \
            "around the fire. A busy couple of working days are behind and everyone is relaxing and having " \
            "a friendly chat with each other. Somebody is laughing. There is a buzz in the air. As soon " \
            "as you enter the area everyone calms down. You approach the fire. Birgitta, the funfair " \
            "director, rises up.")
    else:
        utils.print_text("The campfire!! The END You lose :(")
    return


def newspaper(from_where=""):
    # TODO print_text can be pulled from the DB
    # SELECT Line_text FROM Line WHERE Item_Id = %(newspaper_id)s ORDER BY RAND() LIMIT 1
    sql = "SELECT Line_text FROM Line, Items, Item_types WHERE Line.Item_Id = Items.Item_Id and Items.Itemtype_Id=Item_types.Itemtype_Id and Item_types.Name='Newspaper' ORDER BY RAND() LIMIT 1"
    cur.execute(sql)
    print_text = cur.fetchone()[0].upper()
    if from_where:
        utils.print_text("\nToday's headline of Takaseudun Sanomat is:\n\n\"" + print_text+"\"\n")
    else:
        utils.print_text(
            "Morning! \n\nThe town's own newspaper, Takaseudun Sanomat, has succeeded on putting out a new issue.\n\n\""
            + print_text + "\"\n\nWhatever. You decide to go to the funfair.\n")


def look(loc):
    if g.night:
        description = "Description_night"
        details = "Details_night"
    else:
        description = "Description"
        details = "Details"

    sql = "SELECT Name, %s, %s FROM Places where Place_Id='%s'" % (description, details, str(loc))
    cur.execute(sql)
    if g.debug:
        print(cur._executed)
    if cur.rowcount >= 1:
        for row in cur.fetchall():
            utils.print_text("\n" + row[0] + "\n\n" + row[1] + "\n\n" + row[2] + "\n\n")
    return


def show_passage(loc):
    sql = "select Directions.Description, Places.Name from Has_passages, Directions, Places " \
          "where Has_passages.Direction_Id = Directions.Direction_Id and Has_passages.Has_passagesPlace_Id=Places.Place_Id" \
          " and Has_passages.Place_Id=" + str(loc) + " order by Directions.Description asc;"
    # sql = "SELECT Description FROM Directions WHERE Direction_id IN (SELECT direction_id FROM Has_passages WHERE place_id =" + str(
    #    loc) + ")Order by direction_id ASC LIMIT 10;"
    cur.execute(sql)
    if cur.rowcount >= 1:
        utils.print_text("\nFrom here you can go: \n")
        for row in cur.fetchall():
            utils.print_text("\"" + row[0] + "\" to get to \""+ row[1] + "\"")
        utils.print_text("\n")
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
        text = "You took " + str(person_2_name) + " to visit"
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
    g.location = where

    if made_connections == 4:
        utils.print_text(
            "You have made two connections! No reason to wander around anymore. It's time to enjoy the campfire " \
            "with all the funfair employees and hear what they have to say.")
        g.days = 4
        final()

    if g.asks > 1:
        night()
    return


def chat():
    sql = "SELECT line_text FROM Line LEFT JOIN Persons On Persons.`Person_Id` = Line.`Person_Id` " \
          "WHERE Alias like '%" + obj + "%' AND Line.`Place_Id` = " + str(g.location) + " AND Line.`Item_Id` is null " \
                                                                                      "ORDER BY RAND() LIMIT 1;"
    cur.execute(sql)
    if cur.rowcount >= 1:
        for row in cur:
            utils.print_text(row[0])
            utils.print_text(tips.give_tip(ret['direct_person_id']))
    else:
        utils.print_text("The person you want to chat with is not here")
    return


def buy(item):
    sql = "SELECT Itemtype_Id FROM Item_types WHERE Alias LIKE '%" + item + "%' AND Place_Id = " + str(g.location) + ";"
    cur.execute(sql)
    if cur.rowcount >= 1:
        for row in cur:
            item_id = row[0]
            sql = "SELECT Name FROM Item_types WHERE Alias LIKE '%" + item + "%';"
            cur.execute(sql)
            if cur.rowcount >= 1:
                for row in cur:
                    item_name = row[0]
                    sql = "INSERT INTO Items(Item_Id, Name, Itemtype_Id, Player_Id) SELECT MAX(Item_Id) + 1, + '" + item_name + "' , " + str(
                        item_id) + ", " + str(g.name_id) + " FROM Items;"
                    cur.execute(sql)
                    sql = "SELECT Line_Text FROM Line Where Item_Id = " + str(item_id) + " ORDER BY RAND() LIMIT 1;"
                    cur.execute(sql)
                    for row in cur:
                        utils.print_text(row[0])
    else:
        utils.print_text("You cannot buy " + item + " from here")
    return


def drink(item):
    sql = "SELECT * FROM Items WHERE Itemtype_Id = " + str(item) + " AND Player_Id = " + str(g.name_id) + ";"
    cur.execute(sql)
    if cur.rowcount >= 1:
        action = "drink"
        sql = "SELECT Description From Item_types_Action WHERE Action = '" + action + "' and Itemtype_Id = " + str(
            item) + ";"
        cur.execute(sql)
        if cur.rowcount >= 1:
            for row in cur:
                utils.print_text(row[0])
                sql = "DELETE FROM Items WHERE Itemtype_Id =" + str(
                    item) + " and Player_Id = " + str(g.name_id) + " ORDER BY RAND() LIMIT 1;"
                cur.execute(sql)
    else:
        utils.print_text("You cannot drink what you don't have")

    return


def eat(item):
    sql = "SELECT * FROM Items WHERE Itemtype_Id = " + str(item) + " AND Player_Id = " + str(g.name_id) + ";"
    cur.execute(sql)
    if cur.rowcount >= 1:
        action = "eat"
        sql = "SELECT Description From Item_types_Action WHERE Action = '" + action + "' and Itemtype_Id = " + str(
            item) + ";"
        cur.execute(sql)
        if cur.rowcount >= 1:
            for row in cur:
                utils.print_text(row[0])
                sql = "DELETE FROM Items WHERE Itemtype_Id =" + str(
                    item) + " and Player_Id = " + str(g.name_id) + " ORDER BY RAND() LIMIT 1;"
                cur.execute(sql)
    else:
        utils.print_text("You cannot eat what you don't have")
    return


def ride():
    sql = "SELECT * FROM Items WHERE Itemtype_Id = 1 AND Player_Id = " + str(g.name_id) + ";"
    cur.execute(sql)
    if cur.rowcount >= 1:
        sql = "SELECT ACTION FROM Places Where Place_Id =" + str(g.location) + ";"
        cur.execute(sql)
        if cur.rowcount >= 1:
            for row in cur:
                utils.print_text(row[0])
                sql = "DELETE FROM Items WHERE Itemtype_Id = 1 and Player_Id = " + str(
                    g.name_id) + " ORDER BY RAND() LIMIT 1;"
                cur.execute(sql)
    else:
        utils.print_text("You don't have any ride tickets")
    return


def play(game):
    win = random.randint(1, 4)

    if game == "bottle pyramid":
        bottle_pyramid(win)
    elif game == "pull-a-string" or game == "pull string":
        win = 1
        pull_a_string(win)
    elif game == "climb ladder":
        climb_ladder(win)
    else:
        utils.print_text("What game do you want to play? Possible games are:")
        utils.print_text("    Bottle pyramid\n    Pull-a-string\n    Climb the ladder")
        return

    if win == 1:
        sql = "SELECT Name, Itemtype_Id From Item_types Where Itemtype_Id = 2 OR Itemtype_Id = 16 OR Itemtype_Id = 17 ORDER BY RAND() LIMIT 1;"
        cur.execute(sql)
        if cur.rowcount >= 1:
            for row in cur:
                utils.print_text("You win "+ str(row[0]) + "! Amazing!")
                item_name = row[0]
                item_id = row[1]
                sql = "INSERT INTO Items(Item_Id, Name, Itemtype_Id, Player_Id) SELECT MAX(Item_Id) + 1, + '" + item_name + "' , " + str(
                item_id) + ", " + str(g.name_id) + " FROM Items;"
                cur.execute(sql)
               
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
    utils.print_text("\nINVENTORY\n")
    sql = "Select Name FROM Persons Where Is_Connected = '1'"
    cur.execute(sql)
    if cur.rowcount >= 1:
        utils.print_text("Connected:")
        for row in cur.fetchall():
            utils.print_text(str(row[0]))
    else:
        utils.print_text("No connections")

    sql = "SELECT Line_text FROM Line WHERE Is_tip=1 AND Is_said=1"
    cur.execute(sql)
    if g.debug:
        print(cur._executed)
    utils.print_text("\nYou have got following tips:")
    if cur.rowcount >= 1:
        for row in cur.fetchall():
            utils.print_text('"' + str(row[0]) +'"')
        utils.print_text("(Remember: some tips can be false)")
    else:
        utils.print_text("No tips.")

    sql = "select Items.Name, Places.Name from Items,Item_types,Places where Items.Itemtype_Id=Item_types.Itemtype_Id and " \
          "Item_types.Place_Id=Places.Place_Id and Items.Player_Id= " + str(g.name_id) + ";"
    cur.execute(sql)
    if cur.rowcount >= 1:
        utils.print_text("\nYou are holding:\n")
        for row in cur.fetchall():
            utils.print_text(row[0] + " from " + row[1])
    else:
        utils.print_text("\nYou are holding nothing\n")
    utils.print_text("\n")
    return


def helpme(comm=""):
    if comm in g.verbs:
        outtext = ""

        if comm in ["go", "walk", "move"]:
            outtext = " [direction]\" to move yourself to one of the 8 directions"
        if comm in ["chat", "talk"]:
            outtext = " [person]\" to chat with that person"
        if comm in ["look", "examine", "view"]:
            outtext = "\" to look around yourself and find out where you are"
        if comm in ["directions", "direction"]:
            outtext = "\" to find out possible directions to move next"
        if comm in ["inventory", "i"]:
            outtext = "\" to find out what is in your pockets"
        if comm in ["help", "h"]:
            outtext = "\" to find some help on commands possible in this game"
        if comm in ["quit", "q"]:
            outtext = "\" to quit the game without saving your name into the \"Hall of Fame\""
        if comm in ["ask", "take"]:
            outtext = " [person] to [place]\" to ask this person to follow you to that place"
        if comm == "buy":
            outtext = "\" to buy different items"
        if comm == "eat":
            outtext = "\" to eat different products"
        if comm == "drink":
            outtext = "\" to drink different drinks"
        if comm == "ride":
            outtext = "\" to rides different fun rides"
        if comm == "play":
            outtext = "\" to play different games in Game Hall"
        if comm in ["e", "n", "ne", "nw", "s", "se", "sw", "w", "east", "north", "northeast", "northwest", "south",
                    "southwest", "west"]:
            outtext = "\" to move into that direction"

        if outtext:
            utils.print_text("\n\nUse command \"" + comm + outtext + "\n\n")
        return
    elif not comm:
        utils.print_text("\nSome commands you could find useful:\n")
        utils.print_text(str(','.join(g.verbs[0:3])))
        utils.print_text(str(','.join(g.verbs[3:5])))
        utils.print_text(str(','.join(g.verbs[5:8])))
        utils.print_text(str(','.join(g.verbs[8:10])))
        utils.print_text(str(','.join(g.verbs[10:12])))
        utils.print_text(str(','.join(g.verbs[12:14])))
        utils.print_text(str(','.join(g.verbs[14:16])))
        utils.print_text(str(','.join(g.verbs[16:18]) + " [person] to [place]"))
        utils.print_text(str('\n'.join(g.verbs[18:23])))
        utils.print_text("\nFor moving use compass points:\n")
        utils.print_text(str(', '.join(g.verbs[24::])))
        utils.print_text('\n')
        utils.print_text("Help with a certain command: help [command]""\n")
        
        return
    else:
        utils.print_text("I cannot find help for this command!")
        return

    return


def move(loc, direction):
    destination = g.location

    if len(direction) > 2:
        direction = utils.name_to_direction(direction)

    sql = "SELECT `Has_passagesPlace_Id`, Locked, Lock_message  FROM `Has_passages` WHERE `Direction_Id`= '" + direction + "' AND `Place_Id` = " + str(
        loc) + ";"
    cur.execute(sql)

    if cur.rowcount >= 1:
        for row in cur.fetchall():
            destination = row[0]
            # Locked == True
            if row[1] == 1:
                utils.print_text(row[2])
                destination = g.location

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
g.location = "1"

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
        look(g.location)
    # directions
    if action in ["directions", "direction"]:
        show_passage(g.location)
    # move
    if action in ["go", "walk", "move"] and obj in ["e", "n", "ne", "nw", "s", "se", "sw", "w", "east", "north",
                                                    "northeast", "northwest", "south", "southwest", "west"]:
        newlocation = move(g.location, obj)
        g.location = newlocation
        look(g.location)
    if action in ["e", "n", "ne", "nw", "s", "se", "sw", "w", "east", "north", "northeast", "northwest", "south",
                  "southwest", "west"]:
        newlocation = move(g.location, action)
        g.location = newlocation
        look(g.location)
    # ask/take [person] to [place]
    if action == "ask" or action == "take":
        wrong = "There is something wrong with what you're asking (person or place where you're asking to go)"
        if obj == "":
            utils.print_text("Could you specify who who would you like to take somewhere?")
        elif "direct_person_id" in ret and "indirect_place_id" in ret:
            if ret["direct_person_id"] != 0 and ret["indirect_place_id"] != 0 and g.location != ret["indirect_place_id"]:
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
            itemtype_id = ret["direct_item_id"]
            action = "buy"
            sql = "SELECT * FROM `Item_types_Action` WHERE Itemtype_Id = " + str(
                itemtype_id) + " AND Action = '" + action + "';"
            cur.execute(sql)
            if cur.rowcount >= 1:
                buy(obj)
        else:
            utils.print_text("Don't be silly, that's not something you can buy from here")
    # drink [item]
    if action == "drink":
        if obj == "":
            utils.print_text("You have to be a bit more specific")
        elif "direct_item_id" in ret:
            itemtype_id = ret["direct_item_id"]
            action = "drink"
            sql = "SELECT * FROM `Item_types_Action` WHERE Itemtype_Id = " + str(
                itemtype_id) + " AND Action = '" + action + "';"
            cur.execute(sql)
            if cur.rowcount >= 1:
                drink(itemtype_id)
            else:
                utils.print_text("That is not drinkable")

    # eat [item]
    if action == "eat":
        if obj == "":
            utils.print_text("You have to be a bit more specific")
        elif "direct_item_id" in ret:
            itemtype_id = ret["direct_item_id"]
            action = "eat"
            sql = "SELECT * FROM `Item_types_Action` WHERE Itemtype_Id = " + str(
                itemtype_id) + " AND Action = '" + action + "';"
            cur.execute(sql)
            if cur.rowcount >= 1:
                eat(itemtype_id)
            else:
                utils.print_text("That is not edible")
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
            if ret["direct_place_id"] == g.location:
                if g.location in [3, 4, 6]:
                    ride()
                else:
                    utils.print_text("Excuse me?")
            else:
                utils.print_text("There is nothing for you to ride here")
        else:
            utils.print_text("Are you nuts?")
    # play [game]
    if action == "play" and g.location == 7:
        play(obj)
    if action == "play" and g.location != 7:
        utils.print_text("You have to go to the game hall to play games")
    # wait
    if action == "wait":
        wait()
    # inventory []
    if action in ["i", "inventory"]:
        inventory()
    # help
    if action in ["help", "h"]:
        helpme(obj)
    # read newspaper
    if action == "read" and obj == "newspaper":
        newspaper("from_main")
    if action == "iwannawin":
        tips.connected_names = 2
        final()
if action not in ["quit", "q"]:
    epilogue(g.victory)
else:
    utils.print_text("See you soon again!")
