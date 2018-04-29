#Tips system
from lib.database import FunDb
import random

randint = random.randint

connect = FunDb.connect()
cursor = connect.cursor()

# connections in number forms and by names
connections = []
connected_names = []
lines = {'positive': ["I think %s and %s will get along well",
                      "I think %s could get easily along with %s.",
                      "I think %s and %s have a similar sense of humour"],
         'negative': ["I think %s and %s won't get along very well"]}

# Amount of different tips
positive_tips = 2
negative_tips = 3
false_tips = 1
tips = []


def create_connections():
    while len(connections) < 4:
        digit = randint(1,7)
        if connections.count(str(digit)) == 0:
            connections.append(str(digit))

    for i in range(0, len(connections), 2):
        query1 = "UPDATE Persons " \
                "SET Connects_Person_Id=CASE Person_Id " \
                "WHEN '" + connections[i] + "' THEN '" + connections[i + 1] + "' " \
                "WHEN '" + connections[i + 1] + "' THEN '" + connections[i] + "' " \
                "END " \
                "WHERE Person_Id IN('" + connections[i] + "', '" + connections[i + 1] + "')"
        # print(query1)
        cursor.execute(query1)
    return 0


def get_names():
    global connected_names
    query = "SELECT DISTINCT Persons1.Name AS Person1, Persons2.Name AS Person2 FROM Persons AS Persons1 "\
            "JOIN Persons As Persons2 ON Persons1.Person_Id=Persons2.Connects_Person_Id "

    cursor.execute(query)
    connected_names = cursor.fetchall()


def generate_tips():
    global positive_tips
    global negative_tips

    for i in range(positive_tips):
        tips.append(create_tip('positive'))
    for i in range(negative_tips):
        tips.append(create_tip('negative'))
    for i in range(false_tips):
        tips.append(create_tip('false'))
    random.shuffle(tips)


def create_tip(tip_type):

    if tip_type == 'negative':
        connected = False
        line_type = 'negative'
    elif tip_type == 'positive':
        connected = True
        line_type = 'positive'
    elif tip_type == 'false':
        connected = randint(0, 1)
        if connected:
            line_type = 'negative'
        else:
            line_type = 'positive'
    else:
        return ''

    ids = random_pair(connected)
    line = lines[line_type][randint(0, len(lines[line_type]) - 1)]

    query="SELECT Name FROM Persons WHERE Person_ID IN " + str(ids)
    cursor.execute(query)
    result = cursor.fetchall()
    names = (result[0][0], result[1][0])

    return line % names


def random_pair(connected):
    if connected:
        id = randint(0,1)*2
        return connections[id], connections[id+1]
    else:
        while True:
            rand1 = str(randint(1, 7))
            rand2 = str(randint(1, 7))
            if (connections.count(rand1) == 0 or connections.count(rand2) == 0) and rand1 != rand2:
                break
        return rand1, rand2


def give_tip():
    if len(tips) > 0:
        return tips.pop(0)