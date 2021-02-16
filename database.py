import mysql.connector as MC

"""This class is for connect to the database.
"""
class Database():

    def __init__(self):
        self.db = MC.connect(host = 'localhost', port = 3308, database = 'instagram_V2', user = 'root', password = '')
        self.cursor = self.db.cursor()

    """This method get the datas of the databaase.
    """
    def queryFetchall(self, sql):
        self.cursor.execute(sql)
        request =  self.cursor.fetchall()
        self.cursor.close()
        return request

    """This method insert the datas into the database.
    """
    def queryInsert(self, sql, params=None):
        self.cursor.execute(sql, params)
        self.db.commit()
        self.cursor.close()
