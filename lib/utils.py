def print_text(text=""):
    # width of text to be printed
    print_width = 150

    lines = text.split("\n")
    list_lines = []
    for line in lines:
        words = line.split()
        form_string = ""
        for word in words:
            if len(form_string) < print_width:
                form_string += " " + word
            else:
                list_lines.append(form_string.strip())
                form_string = word

        # append last line
        list_lines.append(form_string.strip())

    ret = "\n".join(list_lines)
    print(ret)


    #print(text)

def make_break():
    input("[PRESS ENTER]")
    print()