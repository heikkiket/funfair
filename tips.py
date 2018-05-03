# Tips system
from lib.database import FunDb
import random

randint = random.randint

connect = FunDb.connect()
cursor = connect.cursor()

# connections in number forms and by names
connections = []

# Amount of different tips
positive_tips = 2
negative_tips = 3
false_tips = 1
tips = []

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


#this function is not used anywhere, but the SQL is too great to be deleted...
def get_names():
    query = "SELECT DISTINCT Persons1.Name AS Person1, Persons2.Name AS Person2 FROM Persons AS Persons1 "\
            "JOIN Persons As Persons2 ON Persons1.Person_Id=Persons2.Connects_Person_Id "

    cursor.execute(query)
    return cursor.fetchall()


def generate_tips():
    global positive_tips
    global negative_tips

    for i in range(positive_tips):
        #TODO Positive tips can both be from same pair
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
        person_id = str(randint(1, 7))
        if ids.count(person_id) == 0:
            break

    query = "INSERT INTO Line (Line_Text, Person_Id, Is_tip) VALUES (%s, %s, 1)"
    cursor.execute(query, (line, person_id))


def random_pair(connected):
    if connected:
        id = randint(0, 1)
        return connections[id]
    else:
        while True:
            rand1 = str(randint(1, 7))
            rand2 = str(randint(1, 7))
            if (connections.count(rand1) == 0 or connections.count(rand2) == 0) and rand1 != rand2:
                break
        return rand1, rand2


def give_tip(person_id):
    query = "SELECT Line_text FROM Line WHERE Is_tip = 1 AND Person_Id=%s"
    query = "SELECT Line_text FROM Line WHERE Is_tip = 1 AND Person_Id=%s"
    cursor.execute(query, (person_id,))
    if cursor.rowcount > 0:
        result = cursor.fetchall()
    else:
        result = ""

    if randint(0, 3) > 0:
        result = ""
    return result

create_connections()
