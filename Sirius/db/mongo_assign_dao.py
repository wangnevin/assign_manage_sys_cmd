from db.mongo_db import client
from bson.objectid import ObjectId

class MongoAssignDao:
    def insert(self, title, student, content):
        try:
            client.sirius.assign.insert_one({"title": title, "student": student, "content": content})
        except Exception as e:
            print(e)

    def search_id(self, content):
        try:
            result = client.sirius.assign.find_one({"content":content})
            return str(result["_id"])
        except Exception as e:
            print(e)

    def update(self, id, title, content):
        try:
            client.sirius.assign.update_one({"_id": ObjectId(id)}, {"$set": {"title": title, "content": content}})
        except Exception as e:
            print(e)

    def get_content(self, content_id):
        try:
            result = client.sirius.assign.find_one({"_id": ObjectId(content_id)})
            return result["content"]
        except Exception as e:
            print(e)

    def delete_assign(self, content_id):
        try:
            client.sirius.assign.delete_one({"_id": ObjectId(content_id)})
        except Exception as e:
            print(e)
