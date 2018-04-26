import parser
import globals



#clear the screen
print ("\n"*100)

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
    cur=connect.cursor()
    sql="SELECT Name, Description, Details FROM Places where Place_Id="+str(location)+";"
    cur.execute(sql)
    if cur.rowcount>=1:
        for row in cur.fetchall():
            print ("\n"+row[0]+"\n\n"+row[1]+"\n\n"+row[2]+"\n\n")
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
action = ""
while action != "quit":
# days muuttuja < 4 / exit

    sentence = input("What will you do? ")
    ret=parser.process_sentence(sentence)
    action=ret[0]
# look [location]
    if (action=="look" or action=="examine" or action=="view"):
        look(4)
        
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
