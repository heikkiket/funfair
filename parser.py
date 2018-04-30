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

        verb = verb.strip().lower()
        object = object.strip().lower()
        indirect_object = indirect_object.strip().lower()

        if globals.debug is True:
            print("verb:", verb)
            print("object:", object)
            print("indirect_object:", indirect_object)
            print()
        for_return = {"verb": verb, "object": object, "indirect": indirect_object}
        for_return.update(get_alias(object, 1))
        for_return.update(get_alias(indirect_object, 2))
        if globals.debug is True:
            print(for_return)
        return for_return
    else:
        print("I don't understand what '", words[0], "' means.", sep='')
        print()
        return


def get_alias(obj, id=1):
    sql1 = "select Person_Id, Alias from Persons where Alias is not null;"
    sql2 = "select Item_Id, Alias from Items where Alias is not null;"
    sql3 = "select Place_Id, Alias from Places where Alias is not null;"

    aliases = {}

    if id == 2:
        aliases.update(get_alias_from_db(sql1, "indirect_person_id", obj))
        aliases.update(get_alias_from_db(sql2, "indirect_item_id", obj))
        aliases.update(get_alias_from_db(sql3, "indirect_place_id", obj))
    else:
        # checking persons
        aliases.update(get_alias_from_db(sql1, "direct_person_id", obj))
        # checking items
        aliases.update(get_alias_from_db(sql2, "direct_item_id", obj))
        # checking places
        aliases.update(get_alias_from_db(sql3, "direct_place_id", obj))
    return aliases


def get_alias_from_db(sql, to, obj):
    return_alias = {}
    cur = connect.cursor()
    cur.execute(sql)
    if cur.rowcount >= 1:
        for row in cur.fetchall():
            for alias in row[1].split(";"):
                if alias == obj:
                    return_alias = {to: row[0]}
    return return_alias


print(process_sentence("go Elna to Carousel"))
