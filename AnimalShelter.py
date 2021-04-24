from pymongo import MongoClient
from bson.objectid import ObjectId


class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """

    def __init__(self, username=None, password=None):
        # Initializing the MongoClient. This helps to
        # access the MongoDB databases and collections.
        if username and password:
            self.client = MongoClient('mongodb://%s:%s@localhost:46000' % (username, password))
        else:
            self.client = MongoClient('mongodb://localhost:46000')
        self.database = self.client['project']

# Complete this create method to implement the C in CRUD.
    def create(self, data):
        if data is not None:
            insert = self.database.animals.insert(data)  # data should be dictionary
            if insert!=0:
                return True
            else:
                return False
        else:
            raise Exception("Nothing to save, because data parameter is empty")


    # Create method to implement the R in CRUD.
    def read(self,criteria=None):

        if criteria:

            data = self.database.animals.find(criteria,{"_id":False})
        else:

            data = self.database.animals.find( {} , {"_id":False})

        return data


    def update_record(self, data):

        if int(choice) is 1:

            query_update = {"name": data}

            new_value = {"$set": {"name": data}}

        else:

            query_update = {"description": data}

            new_value = {"$set": {"description": data}}

            self.database.animals.update_one(query_update, new_value)

        print("data successfully inserted....")



        def remove_record(self, data):

            query_del = {"name": data}

            self.database.animals.delete_one(query_del)

        print('data successfully deleted......')
