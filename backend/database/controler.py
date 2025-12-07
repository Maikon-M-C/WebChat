from .db import conn


class Controler:

    def __init__(self):
        self.conn = conn
        self.collection_name = 'user'

    def create_user(self, data):
        exist1 = self.get_user(('email', '==', data['email']))
        exist2 = self.get_user(('username', '==', data['username']))

        if list(exist1) or list(exist2):
            return None

        result = self.conn.collection(self.collection_name).add(data)
        result = self.read_user(result[1].id)
        return result

    def get_user(self, query=None):
        if query is None:
            result = self.conn.collection(self.collection_name).stream()
        else:
            result = self.conn.collection(self.collection_name).where(*query).stream()
        return result

    def update_user(self, user_id, data):
        result = self.conn.collection(self.collection_name).document(user_id).update(data)
        return result

    def delete_user(self, user_id):
        result = self.conn.collection(self.collection_name).document(user_id).delete()
        return result
    
    def read_user(self, user_id):
        result = self.conn.collection(self.collection_name).document(user_id).get()
        return result
    
    def read_all_users(self):
        result = self.conn.collection(self.collection_name).stream()
        return result
