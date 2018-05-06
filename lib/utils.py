def print_text(text="", center=False):
    # width of text to be printed
    print_width = 150

    lines = text.split("\n")
    list_lines = []
    for line in lines:
        while len(line) > print_width:
            last_space_pos = line[:print_width].rfind(" ")
            to_print = line[:last_space_pos]
            line = line[last_space_pos + 1:]
            if center:
                list_lines.append(to_print.center(print_width))
            else:
                list_lines.append(to_print)

        if center:
            list_lines.append(line.center(print_width))
        else:
            list_lines.append(line)

    ret = "\n".join(list_lines)
    print(ret)


def make_break():
    input("[PRESS ENTER]")
    print()


def direction_to_name(loc):
    locations = {"n": "North", "e": "East", "s": "South", "w": "West", "ne": "Northeast", "se": "Southeast",
                 "sw": "Southwest", "nw": "Northwest"}
    return locations[loc]


def name_to_direction(loc):
    locations = {'north': 'n', 'east': 'e', 'south': 's', 'west': 'w', 'northeast': 'ne', 'southeast': 'se',
                 'southwest': 'sw', 'northwest': 'nw'}
    return locations[loc.lower().strip()]
