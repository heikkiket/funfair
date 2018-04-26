import mysql.connector
db = mysql.connector.connect(host="127.0.0.1",
                      user="dbuser",
                      passwd="dbpass",
                      db="gddpeli",
                      buffered=True)


def move (location, where):
    cur = db.cursor()
    return

def location (where):
    cur=db.cursor()
    sql="SELECT Description, Details FROM Places where Place_Id="+str(where)+";"
    cur.execute(sql)
    for row in cur:
        print (row[0])
        print (row[1])
    return
    
    
