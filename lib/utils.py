import .globals as g


def print_text(text=""):
    lines = text.split("\n")
    list_lines = []
    for line in lines:
        words = line.split()
        form_string = ""
        for word in words:
            if len(form_string) < g.print_width:
                form_string += " " + word
            else:
                list_lines.append(form_string.strip())
                form_string = word

        # append last line
        list_lines.append(form_string.strip())

    ret = "\n".join(list_lines)
    print(ret)


    #print(text)
