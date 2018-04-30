# Database connection
import mysql.connector


class FunDb:
    @staticmethod
    def connect():
        db = mysql.connector.connect(host="127.0.0.1",
                                     user="dbuser",
                                     passwd="dbpass",
                                     db="funfair",
                                     buffered=True)
        return db
