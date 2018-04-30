import globals
# importing DB settings
from lib.database import FunDb

connect = FunDb.connect()


def process_sentence(sentence):
    if globals.debug is True:
        print()
        print("sentence:", sentence)
    words = sentence.split()
    verb = ""
    object = ""
    indirect_object = ""
    if len(words) == 0:
        print("You gave no sentence")
        return {}

    if globals.verbs.count(words[0]) is not 0:
        verb = words.pop(0)

        if len(words) == 0:
            return {"verb": verb, "object": "", "indirect": ""}

        # if there is a preposition after a verb ("talk to" etc.)
        if globals.prepositions.count(words[0]) is not 0:
            del words[0]

        for word in words:
            if globals.prepositions.count(word) is not 0:
                index = words.index(word)
                del words[index]

                indirect_object = ' '.join(words[index:])
                break
            object += word + ' '

        verb = verb.strip()
        object = object.strip()
        indirect_object = indirect_object.strip()

        if globals.debug is True:
            print("verb:", verb)
            print("object:", object)
            print("indirect_object:", indirect_object)
            print()
        for_return = {"verb": verb, "object": object, "inderect": indirect_object}
        for_return.update(getalias(object))
        return for_return
    else:
        print("I don't understand what '", words[0], "' means.", sep='')
        print()
        return


def getalias(obj):
    aliases = {}
    cur = connect.cursor()
    # checking persons
    sql = "select Person_Id, Alias from Persons where Alias is not null;"
    cur.execute(sql)
    if cur.rowcount >= 1:
        for row in cur.fetchall():
            for alias in row[1].split(";"):
                if alias == obj:
                    aliases.update({"person": row[0]})
    # cheking items
    sql = "select Item_Id, Alias from Items where Alias is not null;"
    cur.execute(sql)
    if cur.rowcount >= 1:
        for row in cur.fetchall():
            for alias in row[1].split(";"):
                if alias == obj:
                    aliases.update({"item": row[0]})
    # cheking places
    sql = "select Place_Id, Alias from Places where Alias is not null;"
    cur.execute(sql)
    if cur.rowcount >= 1:
        for row in cur.fetchall():
            for alias in row[1].split(";"):
                if alias == obj:
                    aliases.update({"place": row[0]})
    return aliases


print(process_sentence("go elna to carousel"))
