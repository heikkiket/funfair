import parser
import globals

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
    print("Prologue")
    return

def epilogue():
    return

def night():
    print("At night you work at the warehouse. When having a break at the yard of the warehouse you see a distant glow from the closed funfair: the employees have set up campfire…")
    return
          
def final():
    return
          
#def look(location):
#    cur=db.cursor()
#    sql="SELECT Details FROM Places where Place_Id="+str(location)+";"
#    cur.execute(sql)
#    for row in cur:
#        print (row[0])
#    return
                  
def look(location):         
    cur=connect.cursor()
    sql="SELECT Name, Description, Details FROM Places where Place_Id="+str(location)+";"
    cur.execute(sql)
    if cur.rowcount>=1:
        for row in cur.fetchall():
            print ("\n"+row[0]+"\n\n"+row[1]+"\n\n"+row[2]+"\n\n")
    return

def show_passage(location):
    cur=connect.cursor()
    sql="SELECT Description FROM Directions WHERE Direction_id IN (SELECT direction_id FROM has_passages WHERE place_id ="+str(location)+")Order by direction_id ASC LIMIT 10;"
    cur.execute(sql)
    if cur.rowcount>=1:
        print ("From here you can go: ")
        for row in cur.fetchall() :
            print (row[0])
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
    cur=connect.cursor()
    sql="select Items.Name, Places.Name from Items,Item_types,Places where Items.Itemtype_Id=Item_types.Itemtype_Id and Item_types.Place_Id=Places.Place_Id and Items.Player_Id=\"1\"";
    cur.execute(sql)
    if cur.rowcount>=1:
        print ("\nYou are holding:\n")
        for row in cur.fetchall():
            print (row[0]+" from "+row[1])
    else:
        print ("\nYou are holding nothing\n")
    print ("\n")
    return
def help():
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
print ("\n"*100)


#temp addition, can be deleted later
persons=getalias("persons")
print (persons)
items=getalias("items")
print (items)
places=getalias("places")
print (places)



#playr location
location = "1"
look(location)

action = ""
while action != "quit" and action != "q":
# days muuttuja < 4 / exit
    sentence = input("What will you do? ")
    ret=parser.process_sentence(sentence)
    action=ret[0]
# look [location]
    if (action=="look" or action=="examine" or action=="view"):
        look(location)
# diretions
    if (action=="directions"):
        show_passage(location)
# move
    if (action=="n"):
        newlocation = move(location,action)
        location = newlocation
        look(location)
       
# ask/take [person] to [place]
# chat/talk to/with [person]
# buy [item]
# drink [item]
# eat [item]
# ride [ride]
# play [game]
# wait
# inventory []
    if (action=="i" or action=="inventory"):
        inventory()

# help
# e, w, s, n, etc direction
