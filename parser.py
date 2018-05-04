import globals
from lib import utils
from lib.database import FunDb

connect = FunDb.connect()


def process_sentence(sentence):
    if globals.debug is True:
        utils.print_text()
        utils.print_text("sentence: " + sentence)
    words = sentence.split()
    verb = ""
    object = ""
    indirect_object = ""
    if len(words) == 0:
        utils.print_text("You gave no sentence")
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

        object = remove_articles(object)
        indirect_object = remove_articles(indirect_object)

        if globals.debug is True:
            utils.print_text("verb: " + verb)
            utils.print_text("object: " + object)
            utils.print_text("indirect_object: " + indirect_object)
            utils.print_text()
        for_return = {"verb": verb, "object": object, "indirect": indirect_object}

        # checking if objects are not empty
        if object:
            for_return.update(get_alias(object, 1))
        if indirect_object:
            for_return.update(get_alias(indirect_object, 2))

        if globals.debug is True:
            utils.print_text(str(for_return))
        return for_return
    else:
        utils.print_text("I don't understand what '" + words[0] + "' means.")
        utils.print_text()
        return


def get_alias(obj, id=1):
    sql1 = "select Person_Id, Alias from Persons where Alias is not null;"
    sql2 = "select Items.Item_id, Item_types.Alias from Items, Item_types where Items.Itemtype_Id=Item_types.Itemtype_Id and Item_types.Itemtype_Id is not null;"
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
    if obj is not '' and aliases == {}:
        utils.print_text("I don't understand what '" + obj + "' means.")
        utils.print_text()
    return aliases


def get_alias_from_db(sql, to, obj):
    return_alias = {}
    cur = connect.cursor()
    cur.execute(sql)
    if cur.rowcount >= 1:
        for row in cur.fetchall():
            for alias in row[1].split(";"):
                if alias.strip() == obj:
                    return_alias.update({to: row[0]})
    return return_alias


def remove_articles(string):
    articles = ["the", "a", "an"]
    words = string.split()
    index = 0
    while index < len(words):
        if articles.count(words[index]) is not 0:
            del (words[index])
        else:
            index += 1

    string = ' '.join(words)
    string = string.strip()
    return string
