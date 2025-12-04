from db import conn


class Controler:

    def __init__(self):
        self.conn = conn
        self.collection_name = 'user'

    def create_user(self, data):
        result = self.conn.collection(self.collection_name).add(data)
        return result

    def get_user(self):
        result = self.conn.collection(self.collection_name).where('alice', '==', '').stream() 
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


controler = Controler()
usuarios = controler.get_user()

for usuario in usuarios:
    r = controler.read_user(usuario.id)
    print(f'{usuario.id} => {r.to_dict()}')
