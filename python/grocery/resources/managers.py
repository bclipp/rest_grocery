from flask_restful import Resource, reqparse
import sqlite3


class Manager(Resource):
    TABLE_NAME = 'managers'
    parser = reqparse.RequestParser()

    def get(self, id):
        item = self.find_by_id(id)
        if item:
            return item
        return {'message': 'Manager not found'}, 404

    @classmethod
    def find_by_id(cls, id):
        connection = sqlite3.connect('database.db')
        cursor = connection.cursor()
        query = "SELECT * FROM {table} WHERE id=?".format(table=cls.TABLE_NAME)
        result = cursor.execute(query, (id,))
        row = result.fetchone()
        connection.close()
        if row:
            return {'manager': {'store': row[0],
                                'id': row[1],
                                'first_name': row[2],
                                'last_name': row[3]}}

    def post(self, id):
        if self.find_by_name(id):
            return {'message': "An manager with id '{}' already exists.".format(id)}
        data = Manager.parser.parse_args()
        manager = {'id': id,
                   'store': data['store'],
                   'first_name': data['first_name'],
                   'last_name': data['last_name']}
        try:
            Manager.insert(manager)
        except:
            return {"message": "An error occurred inserting the manager."}
        return manager

    @classmethod
    def insert(cls, manager):
        connection = sqlite3.connect('database.db')
        cursor = connection.cursor()
        query = "INSERT INTO {table} VALUES(?, ?,?,?)".format(table=cls.TABLE_NAME)
        cursor.execute(query, (manager['id'],
                               manager['store'],
                               manager['first_name'],
                               manager['last_name']))
        connection.commit()
        connection.close()

    def delete(self, name):
        connection = sqlite3.connect('database.db')
        cursor = connection.cursor()
        query = "DELETE FROM {table} WHERE name=?".format(table=self.TABLE_NAME)
        cursor.execute(query, (name,))
        connection.commit()
        connection.close()
        return {'message': 'Item deleted'}

    def put(self, id):
        data = Manager.parser.parse_args()
        manager = self.find_by_name(id)
        updated_manager = manager = {'id': id,
                                     'store': data['store'],
                                     'first_name': data['first_name'],
                                     'last_name': data['last_name']}
        if manager is None:
            try:
                Manager.insert(updated_manager)
            except:
                return {"message": "An error occurred inserting the manager."}
        else:
            try:
                Manager.update(updated_manager)
            except:
                return {"message": "An error occurred updating the manager."}
        return updated_manager

    @classmethod
    def update(cls, manager):
        connection = sqlite3.connect('database.db')
        cursor = connection.cursor()
        query = "UPDATE {table} SET ssc=? WHERE name=?".format(table=cls.TABLE_NAME)
        cursor.execute(query, (manager['ssc'], manager['id']))
        connection.commit()
        connection.close()


class ManagerList(Resource):
    TABLE_NAME = 'managers'

    def get(self):
        connection = sqlite3.connect('database.db')
        cursor = connection.cursor()
        query = "SELECT * FROM {table}".format(table=self.TABLE_NAME)
        result = cursor.execute(query)
        managers = []
        for row in result:
            managers.append({'store': row[0],
                             'id': row[1],
                             'first_name': row[2],
                             'last_name': row[3]})
        connection.close()
        return {'managers': managers}
