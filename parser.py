import globals

def process_sentence(sentence):
    if globals.debug == True:
        print()
        print("sentence:", sentence)
    words = sentence.split()
    verb = ""
    object =""
    indirect_object =""
    if len(words) == 0:
        print("You gave no sentence")
        return ['', '', '']

    if globals.verbs.count(words[0]) is not 0:
        verb = words.pop(0)

        if len(words) == 0:
            return [verb, '','']

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

        if globals.debug == True:
            print("verb:", verb)
            print("object:", object)
            print("indirect_object:", indirect_object)
            print()
        return [verb, object, indirect_object]
    else:
        print("I don't understand what '", words[0], "' means.", sep='')
        print()
        return ['', '', '']