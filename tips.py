# Tips system
from lib.database import FunDb
import globals as g
import random

randint = random.randint

cursor = g.cur

# connections in number forms and by names
connections = []
connected_names = 0
connected_pair = []

# Amount of different tips
positive_tips = 1
negative_tips = 3
false_tips = 1
tips = []

first_tip = True


def create_connections():
    global connections
    query = "SELECT Person_Id FROM Persons WHERE Connectable=1 ORDER BY RAND() LIMIT 4"
    cursor.execute(query)
    result = cursor.fetchall()
    raw_connections = []
    for i in result:
        raw_connections.append(i[0])
    half = len(raw_connections) // 2
    connections = [raw_connections[:half], raw_connections[half:]]

    for connection in connections:
        query1 = "UPDATE Persons " \
                "SET Connects_Person_Id=CASE Person_Id " \
                "WHEN %(id1)s THEN %(id2)s " \
                "WHEN %(id2)s THEN %(id1)s " \
                "END " \
                "WHERE Person_Id IN(%(id1)s, %(id2)s)"
        cursor.execute(query1, {'id1': connection[0], 'id2': connection[1]})
    return 0


def succesful_connection(connection):
    for person_id in connection:
        cursor.execute("UPDATE Persons SET Is_Connected=1 WHERE Person_Id=%s", (person_id,))
    del(connections[connections.index(connection)])
    create_tip('positive')


# this function is not used anywhere, but the SQL is too great to be deleted...
def get_names():
    query = "SELECT DISTINCT Persons1.Name AS Person1, Persons2.Name AS Person2 FROM Persons AS Persons1 "\
            "JOIN Persons As Persons2 ON Persons1.Person_Id=Persons2.Connects_Person_Id "

    cursor.execute(query)
    return cursor.fetchall()


def generate_tips():
    global positive_tips
    global negative_tips

    for i in range(positive_tips):
        create_tip('positive')
    for i in range(negative_tips):
        create_tip('negative')
    for i in range(false_tips):
        create_tip('false')
    random.shuffle(tips)


def create_tip(tip_type):

    if tip_type == 'negative':
        connected = False
        is_positive = 0
    elif tip_type == 'positive':
        connected = True
        is_positive = 1
    elif tip_type == 'false':
        connected = randint(0, 1)
        if connected:
            is_positive = 0
        else:
            is_positive = 1
    else:
        return ''

    ids = random_pair(connected)

    query = "SELECT Text FROM Line_templates WHERE Positive =" + str(is_positive) + " ORDER BY RAND() LIMIT 1"
    cursor.execute(query)
    result = cursor.fetchall()
    line_template = result[0][0]

    query = "SELECT Name FROM Persons WHERE Person_ID IN " + str(ids)
    cursor.execute(query)
    result = cursor.fetchall()
    names = (result[0][0], result[1][0])

    line = line_template % names

    while True:
        person_id = randint(1, 8)
        if ids.count(person_id) == 0:
            break

    cursor.execute("SELECT MAX(Lines_Id) From Line")
    result = cursor.fetchall()
    line_id = result[0][0] + 1

    query = "INSERT INTO Line (Lines_Id, Line_Text, Person_Id, Connects_Person_Id, Is_tip) VALUES (%s, %s, %s, %s, 1)"
    cursor.execute(query, (line_id, line, person_id, ids[0]))


def random_pair(connected):
    pair = []
    if connected:
        query = "Select Person_Id FROM Persons Where NOT Connects_Person_Id IS NULL AND Is_Connected = '0'" \
                "ORDER BY RAND() LIMIT 1"
        cursor.execute(query)
        result = cursor.fetchall()
        for connection in connections:
            if result[0][0] in connection:
                pair = connection
        return tuple(pair)
    else:
        query = "Select Person_Id FROM Persons Where Connects_Person_Id IS NULL AND Connectable='1'" \
                "ORDER BY RAND() LIMIT 2"
        cursor.execute(query)
        result = cursor.fetchall()

        return result[0][0], result[1][0]


def give_tip(person_id):
    global first_tip

    result = ""
    found_row = False
    query = "SELECT Lines_Id, Line_text FROM Line WHERE Is_tip = 1 AND Person_Id=%s ORDER BY RAND () LIMIT 1"
    cursor.execute(query, (person_id,))

    if cursor.rowcount > 0:
        result = cursor.fetchall()
        line_id = result[0][0]
        result = result[0][1]
        found_row = True

    propability = randint(0, (4 - g.days))

    if propability == 1 or first_tip is True:
        if found_row:
            cursor.execute("UPDATE Line SET Is_said='1' WHERE Lines_Id=%s", (line_id,))
            first_tip = False
    else:
        result = ""

    return result


def show_tips():
    sql = "SELECT Line_text, Person_Id FROM Line WHERE Is_tip = 1"
    cursor.execute(sql)
    if cursor.rowcount > 0:
        for row in cursor.fetchall():
            print(row)
