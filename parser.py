import globals

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

    if globals.verbs.count(words[0]) is not 0:
        verb = words.pop(0)

        #if there is a preposition after a verb ("talk to" etc.)
        if(globals.prepositions.count(words[0]) is not 0):
            del words[0]

        for word in words:
            if(globals.prepositions.count(word) is not 0):
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