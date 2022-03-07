import pymongo
import configparser

config = configparser.ConfigParser()
config.read('config.ini')
server_port = config['ports']['server']


cs = config['mongodb']['cs']
db = config['mongodb']['db']
tbl = config['mongodb']['tbl']
tbl_support = config['mongodb']['tbl_support']  #  table that holds global information like Max(last) ID given


class MongoDB():
    def __init__(self, connection_string, database, table):
        self.client = pymongo.MongoClient(connection_string)
        self.db = self.client[database]
        self.tbl_employee = self.db[table]
        self.tbl_support = self.db[tbl_support]  # support table

    def add(self, data):
        self.tbl_employee.insert_one(data)

    def remove(self, data):
        d = self.tbl_employee.delete_one(data)
        return d.deleted_count

    def find(self, data={}):
        """
        :param data: data to find, or all data if param is empty
        :return: data from employee table
        """
        find = self.tbl_employee.find(data)
        return find

    def getMaxID(self):
        """
        :return: int of last ID
        """
        return self.tbl_support.find_one({"id_number": {"$exists": "true"}})['id_number']

    def updateID(self):
        """
        updates new id in support DB
        :return: new ID
        """
        newID = self.getMaxID() + 1
        self.tbl_support.update_one({"id_number": {"$exists": "true"}}, {"$set": {"id_number": newID}})
        return newID


class Record:
    def __init__(self, first, last):
        self.first = first
        self.last = last


if __name__ == '__main__':
    m = MongoDB(cs, db, tbl)
    m.add({'first': 'Dvir','last':'Noiman', "id_number": m.updateID()})

    for rec in m.find():
        print(rec)
    # m.remove({'name': 'Dvir'})

    f = m.find({"id_number": {'$exists': 1}})
    #  add here if nothing found start with 0, if not add 1 and return it in the class def above
    for i in f:
        first = i["first"]
        last = i["last"]
        id = i["id_number"]
        print(f'Name: {first} {last} Id Number: {id}')


    print(m.getMaxID())

    m.updateID()
    print(m.getMaxID())