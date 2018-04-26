db = null
verbs = ["go", "walk",
         "ask", "chat", "talk", "buy", "eat", "drink", "ride", "look", "play", "wait",
         "inventory", "i", "help"]
prepositions = ["to", "at", "in"]

def db_connect(database_object):
    db = database_object

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

def test_query():
    cursor = db.cursor()

    query1 = ("SELECT * FROM Pelihahmo")

    cursor.execute(query1)
    result = cursor.fetchall()

    if cursor.rowcount >= 1:
        for row in result:
            print(row)

lause = "ask bumper car operator to a cafeteria"
process_sentence(lause)

lause2 = "walk north"
process_sentence(lause2)

lause3 = "talk to a cafe keeper in the cafeteria"
process_sentence(lause3)

while(lause is not ""):
    lause = input("Give a sentence (Empty line finishes): ")
    process_sentence(lause)