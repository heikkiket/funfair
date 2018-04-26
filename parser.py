import tsd
import mysql.connector

db = mysql.connector.connect(host="127.0.0.1",
                      user="dbuser",
                      passwd="dbpass",
                      db="gddpeli",
                      buffered=True)


verbs = ["go", "walk",
         "ask", "chat", "talk", "buy", "eat", "drink", "ride", "look", "play", "wait",
         "inventory", "i", "help"]
prepositions = ["to", "at", "in"]

def process_sentence(sentence):
    print()
    print("sentence:", sentence)
    words = sentence.split()
    verb = ""
    object =""
    indirect_object =""
    if len(words) == 0:
        print("You gave no sentence")
        return 0

    if verbs.count(words[0]) is not 0:
        verb = words.pop(0)

        #if there is a preposition after a verb ("talk to" etc.)
        if(prepositions.count(words[0]) is not 0):
            del words[0]

        for word in words:
            if(prepositions.count(word) is not 0):
                index= words.index(word)
                del words[index]

                indirect_object = ' '.join(words[index:])
                break;
            object += word + ' '

        print("verb:", verb)
        print("object:", object)
        print("indirect_object:", indirect_object)
        print()
        return 1
    else:
        print("I don't understand what '", words[0], "' means.", sep='')
        print()
        return 0

#x=tsd.location(4)

#lause = "ask bumper car operator to a cafeteria"
#process_sentence(lause)

#lause2 = "walk north"
#process_sentence(lause2)

#lause3 = "talk to a cafe keeper in the cafeteria"
#process_sentence(lause3)

#lause="h"

#while(lause is not ""):
#    lause = input("Give a sentence (Empty line finishes): ")
#    process_sentence(lause)

db.rollback()
