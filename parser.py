verbs = ["talk", "look", "ask", "walk"]
prepositions = ["to", "at", "in"]

def process_sentence(sentence):
    print()
    print("sentence:", sentence)
    words = sentence.split()
    verb = ""
    object =""
    indirect_object =""
    if len(words) == 0:
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
        return 0

lause = "ask bumper car operator to a cafeteria"
process_sentence(lause)

lause2 = "walk north"
process_sentence(lause2)

lause3 = "talk to a cafe keeper in the cafeteria"
process_sentence(lause3)